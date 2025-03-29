from datetime import datetime

agents = [
    {
        "id": 1,
        "name": "HR Assistant",
        "description": "Answers HR-related questions professionally",
        "role": "HR Specialist",
        "created_at": datetime.now().isoformat(),
        "system_prompt": "You are an AI HR assistant.",
        "model": "gemini-pro"
    }
]

conversations = []
messages = []
notifications = []
performance_metrics = {
    "agents": {},
    "daily_stats": []
}