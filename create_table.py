from cassandra.cluster import Cluster

# buat instance cluster cluster = Cluster([host])
cluster = Cluster()
# koneksi ke keyspace kantor
session = cluster.connect("kantor")
# buat table pegawai jika belum ada
cQuery = """
	CREATE TABLE IF NOT EXISTS pegawai(
		nip text,
		nama text,
		alamat text,
		gaji float,
		PRIMARY KEY (nip))
	"""
# jalankan querynya
session.execute(cQuery)
# siapkan index untuk filtering
session.execute("CREATE INDEX IF NOT EXISTS ON pegawai(alamat)")


