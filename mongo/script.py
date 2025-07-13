from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  # Or "mongodb" inside Docker
db = client["healthcare"]  # Database
notes = db["patient_notes"]  # Collection
