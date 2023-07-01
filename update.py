from cassandra.cluster import Cluster

# buat instance cluster cluster = Cluster([host])
cluster = Cluster()
# koneksi ke keyspace kantor
session = cluster.connect("kantor")

cQuery = "UPDATE pegawai SET gaji=3500000 WHERE nip='003' "
session.execute(cQuery)
hasil = session.execute("SELECT * FROM pegawai where nip='003' ")
for  data in hasil:
	print(data.nip,'\t',data.nama,'\t',data.alamat,'\t',data.gaji)

