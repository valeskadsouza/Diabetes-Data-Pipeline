from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])  # Use "cassandra" in Docker
session = cluster.connect()

# Create keyspace
session.execute("""
CREATE KEYSPACE IF NOT EXISTS health 
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
""")

# Set keyspace
session.set_keyspace("health")

# Create table
session.execute("""
CREATE TABLE IF NOT EXISTS metrics (
  patient_id int,
  visit_date date,
  glucose float,
  PRIMARY KEY (patient_id, visit_date)
)
""")

print("✅ Keyspace and table created.")

