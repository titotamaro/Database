import mysql.connector
from mysql.connector import errorcode

namaDB = {
    'user' : 'root',
    'password' : 'cherryblossomtime',
    'host' : 'localhost',
    'database' : 'lat_jcds'
}
try:
    conn = mysql.connector.connect(**namaDB)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Username atau Password Salah")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database Tidak Ditemukan")
    else:
        print("Gagal Koneksi ke Database")
else:            
    # print("Koneksi Berhasil")
    kursor = conn.cursor()
    query1 = "CREATE Table aset_lat (kode char(5), nama char(25), stok int)"
    # query = 'select * from dosen'
    query2 = "SHOW TABLES"
    # untuk memasukkan data string ke dalam database gunakan tanda kutip yang berbeda (1 atau 2 pcs)
    query3 = "INSERT INTO aset_lat values ('25a','Lemari',30)"
    #DESCRIBE --- DESC
    # kursor.execute(query3)
    # out = kursor.fetchall()
    # print(out)
    # untuk CRUD database:
    # conn.commit()
    # for i in kursor:
    #     print(i)

    ## untuk menghapus data
    # query4 = "DELETE from aset_lat where kode='25a'"
    # kursor.execute(query4)

    # update data
    query5 = "update aset_lat set stok=10 where kode='20a'"
    # kursor.execute(query5)
    # conn.commit() # Digunakan jika program melakukan updata / manipulasi data pada database
    # print("Data Terupdate")

    #Alternatif Insert Data
    # sql = "insert into aset_lat (kode, nama, stok) values (%s, %s, %s)"
    # val = ('A21','Sepatu',25)
    # kursor.execute(sql, val)
    # conn.commit()
    # print("data tersimpan")
    sql = "insert into aset_lat (kode, nama, stok) values (%s, %s, %s)"
    val = [('A22','Sepatu',25),('A23', 'Celana', 25)]
    kursor.executemany(sql, val)
    conn.commit()
    print(kursor.rowcount, "data tersimpan")

''' --- Latihan ---
http://digidb.io/digimon-list/

Buat Database Baru (via CMD)

Via Python
Buat Tabel Baru
Masukkan semua Data Digimmon ke dalam tabel baru (341 digimon)
Image = Link Image '''