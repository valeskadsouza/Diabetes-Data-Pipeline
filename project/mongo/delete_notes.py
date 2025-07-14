from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Use "mongodb" if running inside Docker
db = client["healthcare"]
notes = db["patient_notes"]

# Step 2: Delete the note for a specific patient_id
result = notes.delete_one({"patient_id": 12345})

# Step 3: Report the result
if result.deleted_count > 0:
    print("Note deleted successfully.")
else:
    print("No note found to delete.")

