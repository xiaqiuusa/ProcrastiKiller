import requests
import json

def test_predict_coach_tips():
    """Test the predict-coach-tips endpoint"""
    
    # Sample task data
    sample_tasks = [
        {
            "title": "Write essay",
            "description": "Intro + conclusion",
            "createdAt": "2024-06-25T14:00:00",
            "completed": True,
            "completedAt": "2024-06-25T14:45:00"
        },
        {
            "title": "Read research paper",
            "description": "Analyze methodology and results",
            "createdAt": "2024-06-25T09:00:00",
            "completed": True,
            "completedAt": "2024-06-25T10:30:00"
        },
        {
            "title": "Prepare presentation",
            "description": "Create slides for team meeting",
            "createdAt": "2024-06-25T16:00:00",
            "completed": True,
            "completedAt": "2024-06-25T17:15:00"
        },
        {
            "title": "Review code",
            "description": "Check pull request and provide feedback",
            "createdAt": "2024-06-25T11:00:00",
            "completed": True,
            "completedAt": "2024-06-25T11:45:00"
        },
        {
            "title": "Plan next week",
            "description": "Organize tasks and set priorities",
            "createdAt": "2024-06-25T20:00:00",
            "completed": True,
            "completedAt": "2024-06-25T20:30:00"
        }
    ]
    
    # API endpoint
    url = "http://localhost:5000/predict-coach-tips"
    
    try:
        # Make POST request
        response = requests.post(url, json=sample_tasks)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ API Test Successful!")
            print("\n📊 Productivity Analysis Results:")
            print(f"Best time for focus: {result['best_time']}")
            print(f"Average task duration: {result['average_duration']} minutes")
            print(f"Suggested priority: {result['priority']}")
            print(f"Motivational quote: \"{result['quote']}\"")
        else:
            print(f"❌ API Test Failed with status code: {response.status_code}")
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure the Flask server is running on localhost:5000")
        print("Run: python app.py")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def test_health_check():
    """Test the health check endpoint"""
    url = "http://localhost:5000/health"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Health check passed!")
            print(f"Status: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Health check failed: Server not running")

if __name__ == "__main__":
    print("🚀 Testing Productivity Coach API")
    print("=" * 40)
    
    # Test health check first
    test_health_check()
    print()
    
    # Test main endpoint
    test_predict_coach_tips() 