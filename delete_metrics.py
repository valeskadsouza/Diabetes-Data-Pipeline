from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('health')

session.execute("""
DELETE FROM metrics 
WHERE patient_id = 12345 AND visit_date = '2025-07-10'
""")

print("🗑️ Record deleted.")
