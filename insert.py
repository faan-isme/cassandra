from cassandra.cluster import Cluster

# buat instance cluster cluster = Cluster([host])
cluster = Cluster()
# koneksi ke keyspace kantor
session = cluster.connect("kantor")
session.execute("""
			INSERT INTO pegawai (nip, nama, alamat, gaji)
			VALUES ('001','TONY','YOGYA',4000000)
		""")
session.execute("""
			INSERT INTO pegawai (nip, nama, alamat, gaji)
			VALUES (%s, %s, %s, %s)
			""",
			('002','BRUCE','YOGYA',5000000)
		)
session.execute("""
			INSERT INTO pegawai (nip, nama, alamat, gaji)
			VALUES (%(nip)s, %(namapeg)s, %(alamat)s, %(gaji)s)
			""",
			{'nip':'003','gaji':3000000,'namapeg':'STEVE','alamat':'SOLO'}
		)

