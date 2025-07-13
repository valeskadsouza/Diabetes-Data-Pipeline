from pymongo import MongoClient
from datetime import datetime

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # or "mongodb" if using Docker Compose
db = client["healthcare"]           # database
notes = db["patient_notes"]         # collection

# Step 2: Insert a sample note
result = notes.insert_one({
    "patient_id": 12345,
    "note": "Patient shows improved glucose control.",
    "timestamp": datetime.now().isoformat()
})

print("Note inserted with ID:", result.inserted_id)

