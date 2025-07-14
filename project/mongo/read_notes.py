from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Use "mongodb" if inside Docker
db = client["healthcare"]
notes = db["patient_notes"]

# Step 2: Find and print a note
result = notes.find_one({"patient_id": 12345})

if result:
    print("Found note:")
    print(result)
else:
    print("No note found for patient_id 12345")

