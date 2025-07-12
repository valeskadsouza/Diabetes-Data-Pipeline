from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

# Use keyspace
session.set_keyspace("health")

# Create table with glucose as FLOAT
session.execute("""
CREATE TABLE IF NOT EXISTS metrics (
    patient_id int,
    visit_date date,
    glucose float,
    PRIMARY KEY (patient_id, visit_date)
)
""")

print("✅ Corrected 'metrics' table created.")
