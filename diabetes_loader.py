import pandas as pd
from pymongo import MongoClient
from cassandra.cluster import Cluster
from datetime import datetime

# Load CSV
df = pd.read_csv("diabetic_data.csv")

# MongoDB Connection (default)
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["healthcare"]
mongo_col = mongo_db["patient_notes"]


# Cassandra Connection (for Docker Compose network)
cluster = Cluster(['127.0.0.1'])


session = cluster.connect()
session.execute("CREATE KEYSPACE IF NOT EXISTS health WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}")
session.set_keyspace("health")
session.execute("""
    CREATE TABLE IF NOT EXISTS metrics (
        patient_id text,
        visit_date text,
        glucose text,
        PRIMARY KEY (patient_id, visit_date)
    )
""")

# Insert into MongoDB and Cassandra
for _, row in df.iterrows():
    # --- MongoDB ---
    mongo_col.insert_one({
        "patient_id": row["patient_nbr"],
        "note": row["diag_1"],
        "timestamp": datetime.now().isoformat()
    })

    # --- Cassandra ---
    session.execute("""
        INSERT INTO metrics (patient_id, visit_date, glucose)
        VALUES (%s, %s, %s)
    """, (str(row["patient_nbr"]), str(row["admission_type_id"]), str(row["max_glu_serum"])))

print("Data successfully ingested.")
