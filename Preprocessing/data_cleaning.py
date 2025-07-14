import pandas as pd
import json
from pymongo import MongoClient
from pymongo.errors import BulkWriteError

# Load data
df = pd.read_csv('../data/diabetic_data.csv')

# Cleaning
df = df.drop_duplicates()
df = df.dropna(subset=['readmitted'])

for col in ['num_lab_procedures', 'num_procedures', 'num_medications']:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

columns_to_drop = ['encounter_id', 'patient_nbr']
df = df.drop(columns=columns_to_drop, errors='ignore')

df['readmitted_flag'] = df['readmitted'].apply(lambda x: 1 if x == '<30' else 0)
df = df[df['gender'] != 'Unknown/Invalid']
df['gender'] = df['gender'].map({'Female': 0, 'Male': 1})


def parse_age(age_range):
    if isinstance(age_range, str):
        return int(age_range.strip('[]()').split('-')[0]) + 5
    return None


df['age_num'] = df['age'].apply(parse_age)

if 'number_inpatient' in df.columns and 'number_outpatient' in df.columns and 'number_emergency' in df.columns:
    df['total_visits'] = df['number_inpatient'] + df['number_outpatient'] + df['number_emergency']

df.to_csv('../data/cleaned_diabetic_data.csv', index=False)

# Store to MongoDB
with open('../config/mongodb_config.json') as f:
    config = json.load(f)

print("→ Loaded URI:", config["mongodb_uri"])
client = MongoClient(config["mongodb_uri"])
db = client[config["db_name"]]

collection = db[config["collection_name"]]

collection.delete_many({})

records = df.to_dict('records')
BATCH_SIZE = 1000  # adjust this based on your dataset

for i in range(0, len(records), BATCH_SIZE):
    batch = records[i:i + BATCH_SIZE]
    try:
        collection.insert_many(batch)
        print(f"Inserted batch {i // BATCH_SIZE + 1}")
    except BulkWriteError as bwe:
        print("⚠️ Bulk write error:", bwe.details)


print("Data cleaned and inserted into MongoDB Atlas.")
