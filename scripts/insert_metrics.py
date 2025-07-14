from cassandra.cluster import Cluster
from datetime import date

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('health')

session.execute("""
INSERT INTO metrics (patient_id, visit_date, glucose) 
VALUES (%s, %s, %s)
""", (12345, date(2025, 7, 10), 185.0))

print("✅ Data inserted.")
