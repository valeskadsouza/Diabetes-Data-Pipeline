from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('health')

session.execute("DROP TABLE IF EXISTS metrics")

print("🗑️ Old 'metrics' table dropped.")
