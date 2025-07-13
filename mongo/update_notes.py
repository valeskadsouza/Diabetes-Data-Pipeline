from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["healthcare"]
notes = db["patient_notes"]

# Step 2: Update a note
result = notes.update_one(
    {"patient_id": 12345},
    {"$set": {"note": "Updated glucose diagnosis"}}
)

# Step 3: Print result
if result.modified_count > 0:
    print("Note updated successfully.")
else:
    print("No note found to update.")

