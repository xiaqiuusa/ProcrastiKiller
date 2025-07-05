# Productivity Coach API

A Flask-based API that analyzes user task history and provides personalized productivity suggestions using machine learning.

## Features

- **Time Analysis**: Analyzes when you're most productive during the day
- **Duration Prediction**: Estimates average task completion time
- **Priority Suggestions**: Recommends task priority levels
- **Motivational Quotes**: Provides inspiring quotes to boost productivity

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask server:**
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:5000`

## API Endpoints

### POST `/predict-coach-tips`

Analyzes task history and returns productivity suggestions.

#### Request Body

```json
[
  {
    "title": "Write essay",
    "description": "Intro + conclusion",
    "createdAt": "2024-06-25T14:00:00",
    "completed": true,
    "completedAt": "2024-06-25T14:45:00"
  }
]
```

#### Response

```json
{
  "best_time": "Afternoon",
  "average_duration": 28,
  "priority": "Medium",
  "quote": "Discipline beats motivation."
}
```

#### Field Descriptions

- `title`: Task title (string)
- `description`: Task description (string)
- `createdAt`: ISO timestamp when task was created
- `completed`: Boolean indicating if task was completed
- `completedAt`: ISO timestamp when task was completed

### GET `/health`

Health check endpoint to verify API status.

#### Response

```json
{
  "status": "healthy",
  "message": "Productivity Coach API is running"
}
```

## How It Works

### Time of Day Analysis
The API categorizes tasks into four time periods:
- **Morning**: 5:00 AM - 11:59 AM
- **Afternoon**: 12:00 PM - 4:59 PM
- **Evening**: 5:00 PM - 9:59 PM
- **Night**: 10:00 PM - 4:59 AM

### Machine Learning Features
- **Random Forest Classifier**: Predicts task priority based on duration, time, and complexity
- **Productivity Scoring**: Calculates efficiency based on completion time vs. task complexity
- **Pattern Recognition**: Identifies your most productive time periods

### Priority Classification
- **High**: Complex tasks (>60 min or >100 chars description)
- **Medium**: Standard tasks (30-60 min, 50-100 chars)
- **Low**: Quick tasks (<30 min, <50 chars)

## Testing

Run the test script to verify the API:

```bash
python test_api.py
```

This will test both the health check and the main prediction endpoint with sample data.

## Example Usage

### Using curl

```bash
curl -X POST http://localhost:5000/predict-coach-tips \
  -H "Content-Type: application/json" \
  -d '[
    {
      "title": "Write essay",
      "description": "Intro + conclusion",
      "createdAt": "2024-06-25T14:00:00",
      "completed": true,
      "completedAt": "2024-06-25T14:45:00"
    }
  ]'
```

### Using Python requests

```python
import requests

tasks = [
    {
        "title": "Write essay",
        "description": "Intro + conclusion",
        "createdAt": "2024-06-25T14:00:00",
        "completed": True,
        "completedAt": "2024-06-25T14:45:00"
    }
]

response = requests.post('http://localhost:5000/predict-coach-tips', json=tasks)
result = response.json()

print(f"Best time: {result['best_time']}")
print(f"Average duration: {result['average_duration']} minutes")
print(f"Priority: {result['priority']}")
print(f"Quote: {result['quote']}")
```

## Error Handling

The API includes comprehensive error handling:

- **400 Bad Request**: Invalid input format or missing required fields
- **500 Internal Server Error**: Server-side processing errors

All errors return JSON with an `error` field containing a descriptive message.

## Dependencies

- **Flask**: Web framework
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms
- **Werkzeug**: WSGI utilities

## Development

The API is built with:
- **Flask** for the web framework
- **Random Forest** for priority prediction
- **Statistical analysis** for time-of-day optimization
- **JSON** for data exchange

## Future Enhancements

Potential improvements:
- User authentication and personalization
- More sophisticated ML models
- Integration with calendar APIs
- Real-time productivity tracking
- Team productivity analytics 