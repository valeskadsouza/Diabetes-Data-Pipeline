from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('health')

rows = session.execute("SELECT * FROM metrics WHERE patient_id = 12345")

print("📋 Records for patient_id = 12345:")
for row in rows:
    print(f"🩺 Date: {row.visit_date} | Glucose: {row.glucose}")
