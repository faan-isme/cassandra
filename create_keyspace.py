from cassandra.cluster import Cluster

# buat instance cluster cluster = Cluster([host])
# host default adalah 127.0.0.1 atau localhost
cluster = Cluster()
session = cluster.connect("system")
cQuery = """
	CREATE KEYSPACE kantor
	WITH replication = {'class':'SimpleStrategy',
						'replication_factor':3}
	"""
session.execute(cQuery)

