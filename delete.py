from cassandra.cluster import Cluster

# buat instance cluster cluster = Cluster([host])
cluster = Cluster()
# koneksi ke keyspace kantor
session = cluster.connect("kantor")

cQuery = "DELETE FROM pegawai WHERE nip='002' "
session.execute(cQuery)
hasil = session.execute("SELECT * FROM pegawai ")
for  data in hasil:
	print(data.nip,'\t',data.nama,'\t',data.alamat,'\t',data.gaji)