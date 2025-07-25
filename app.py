from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime, timedelta, date
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import json
import random
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

HABIT_PHOTO_FOLDER = 'habit_photos'
os.makedirs(HABIT_PHOTO_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_timestamp(timestamp_str):
    """Parse timestamp string to datetime object"""
    return datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))

def get_time_of_day(hour):
    """Categorize hour into time of day"""
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 22:
        return "Evening"
    else:
        return "Night"

def calculate_duration(created_at, completed_at):
    """Calculate duration in minutes"""
    duration = completed_at - created_at
    return duration.total_seconds() / 60

def extract_features(tasks):
    """Extract features from task history"""
    features = []
    
    for task in tasks:
        created_at = parse_timestamp(task['createdAt'])
        completed_at = parse_timestamp(task['completedAt'])
        
        # Duration in minutes
        duration = calculate_duration(created_at, completed_at)
        
        # Time of day
        hour = created_at.hour
        time_of_day = get_time_of_day(hour)
        
        # Day of week (0=Monday, 6=Sunday)
        day_of_week = created_at.weekday()
        
        # Task length (description length as proxy)
        task_length = len(task.get('description', ''))
        
        features.append({
            'duration': duration,
            'hour': hour,
            'time_of_day': time_of_day,
            'day_of_week': day_of_week,
            'task_length': task_length,
            'completed': 1 if task['completed'] else 0
        })
    
    return features

def predict_best_time(features):
    """Predict best time of day for focus using clustering"""
    if len(features) < 2:
        return "Afternoon"  # Default fallback
    
    # Extract productivity metrics (inverse of duration for completed tasks)
    productivity_scores = []
    time_of_day_counts = {"Morning": [], "Afternoon": [], "Evening": [], "Night": []}
    
    for feature in features:
        if feature['completed']:
            # Lower duration = higher productivity
            productivity = 1 / (feature['duration'] + 1)  # Add 1 to avoid division by zero
            time_of_day_counts[feature['time_of_day']].append(productivity)
    
    # Calculate average productivity for each time of day
    time_productivity = {}
    for time, scores in time_of_day_counts.items():
        if scores:
            time_productivity[time] = np.mean(scores)
        else:
            time_productivity[time] = 0
    
    # Return time of day with highest productivity
    return max(time_productivity.items(), key=lambda x: x[1])[0]

def predict_average_duration(features):
    """Predict average completion duration"""
    completed_durations = [f['duration'] for f in features if f['completed']]
    
    if not completed_durations:
        return 30  # Default 30 minutes
    
    return round(np.mean(completed_durations))

def predict_priority(features):
    """Predict suggested priority using Random Forest"""
    if len(features) < 3:
        return "Medium"  # Default fallback
    
    # Create training data
    X = []
    y = []
    
    for feature in features:
        if feature['completed']:
            X.append([
                feature['hour'],
                feature['day_of_week'],
                feature['task_length'],
                feature['duration']
            ])
            
            # Determine priority based on duration and task length
            if feature['duration'] < 30 and feature['task_length'] < 50:
                y.append(0)  # Low priority
            elif feature['duration'] > 60 or feature['task_length'] > 100:
                y.append(2)  # High priority
            else:
                y.append(1)  # Medium priority
    
    if len(set(y)) < 2:
        return "Medium"  # Not enough variety in training data
    
    # Train Random Forest
    try:
        clf = RandomForestClassifier(n_estimators=10, random_state=42)
        clf.fit(X, y)
        
        # Predict priority for a typical task
        typical_task = [12, 2, 50, 45]  # Afternoon, Wednesday, medium length, 45 min
        prediction = clf.predict([typical_task])[0]
        
        priority_map = {0: "Low", 1: "Medium", 2: "High"}
        return priority_map[prediction]
    except:
        return "Medium"

def get_motivational_quote():
    """Return a random motivational quote"""
    quotes = [
        "Discipline beats motivation.",
        "The only way to do great work is to love what you do.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "The future depends on what you do today.",
        "Don't watch the clock; do what it does. Keep going.",
        "The only limit to our realization of tomorrow is our doubts of today.",
        "It always seems impossible until it's done.",
        "The way to get started is to quit talking and begin doing.",
        "Your time is limited, don't waste it living someone else's life.",
        "The best way to predict the future is to create it."
    ]
    return random.choice(quotes)

def calculate_streak(tasks):
    """Calculate 7-day streak and progress bar"""
    # Get all completed task dates
    completed_dates = set()
    for task in tasks:
        if task.get('completed') and task.get('completedAt'):
            try:
                completed_date = parse_timestamp(task['completedAt']).date()
                completed_dates.add(completed_date)
            except Exception:
                continue
    
    streak = 0
    today = date.today()
    for i in range(7):
        day = today - timedelta(days=i)
        if day in completed_dates:
            streak += 1
        else:
            break
    progress = int((streak / 7) * 100)
    return streak, progress

@app.route('/predict-coach-tips', methods=['POST'])
def predict_coach_tips():
    """Analyze task history and provide productivity suggestions"""
    try:
        # Get input data
        data = request.get_json()
        
        if not data or not isinstance(data, list):
            return jsonify({'error': 'Invalid input format. Expected a list of tasks.'}), 400
        
        # Validate required fields
        for task in data:
            required_fields = ['title', 'description', 'createdAt', 'completed', 'completedAt']
            for field in required_fields:
                if field not in task:
                    return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Extract features from task history
        features = extract_features(data)
        
        if not features:
            return jsonify({'error': 'No valid tasks found in input data.'}), 400
        
        # Generate predictions
        best_time = predict_best_time(features)
        average_duration = predict_average_duration(features)
        priority = predict_priority(features)
        quote = get_motivational_quote()
        
        # Calculate streak and progress
        streak_days, streak_progress = calculate_streak(data)
        
        # Prepare response
        response = {
            'best_time': best_time,
            'average_duration': average_duration,
            'priority': priority,
            'quote': quote,
            'streak_days': streak_days,
            'streak_progress': streak_progress
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Productivity Coach API is running'})

@app.route('/upload-habit-photo', methods=['POST'])
def upload_habit_photo():
    """Accept a photo for a habit and run a placeholder AI check"""
    if 'photo' not in request.files or 'habit_id' not in request.form:
        return jsonify({'error': 'Missing photo or habit_id'}), 400
    file = request.files['photo']
    habit_id = request.form['habit_id']
    habit_title = request.form.get('habit_title', '')
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({'error': 'Invalid or missing file'}), 400
    filename = secure_filename(f"{habit_id}_{file.filename}")
    filepath = os.path.join(HABIT_PHOTO_FOLDER, filename)
    file.save(filepath)

    # --- Placeholder AI logic ---
    # 1. Check if image is likely from Google (filename contains 'google' or random chance)
    if file.filename and ('google' in file.filename.lower() or random.random() < 0.1):
        return jsonify({
            'result': 'fail',
            'confidence': 0.5,
            'filename': filename,
            'message': 'AI detected this image is likely from Google. Please take a real photo.'
        })
    # 2. Check if image correlates with the habit name (random fail for demo)
    if habit_title and random.random() < 0.15:
        return jsonify({
            'result': 'fail',
            'confidence': 0.6,
            'filename': filename,
            'message': f"AI could not verify this photo matches the habit: '{habit_title}'. Please try again with a more relevant photo."
        })
    # Otherwise, pass
    result = 'pass'
    confidence = round(random.uniform(0.85, 0.99), 2)
    return jsonify({
        'result': result,
        'confidence': confidence,
        'filename': filename,
        'message': 'Photo accepted!'
    })

@app.route('/habit_photos/<filename>')
def get_habit_photo(filename):
    return send_from_directory(HABIT_PHOTO_FOLDER, filename)

# --- HTML Endpoints ---
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/app')
def serve_app():
    return send_from_directory('.', 'app.html')

@app.route('/demo')
def serve_demo():
    return send_from_directory('.', 'demo.html')

@app.route('/help')
def serve_help():
    return send_from_directory('.', 'help.html')

@app.route('/about')
def serve_about():
    return send_from_directory('.', 'about.html')

@app.route('/terms')
def serve_terms():
    return send_from_directory('.', 'terms.html')

@app.route('/contact')
def serve_contact():
    return send_from_directory('.', 'contact.html')

@app.route('/privacy')
def serve_privacy():
    return send_from_directory('.', 'privacy.html')

@app.route('/star-demo')
def serve_star_demo():
    return send_from_directory('.', 'star_demo.html')

@app.route('/crafting-demo')
def serve_crafting_demo():
    return send_from_directory('.', 'crafting_demo.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 