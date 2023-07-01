from cassandra.cluster import Cluster

# buat instance cluster cluster = Cluster([host])
cluster = Cluster()
# koneksi ke keyspace kantor
session = cluster.connect("kantor")

hasil = session.execute("select * from pegawai where alamat=%s", ["YOGYA"])
for data in hasil:
	print(data.nip,'\t',data.nama,'\t',data.alamat,'\t',data.gaji)

# hasil = session.execute("select * from pegawai")
	