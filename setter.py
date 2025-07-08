"""
Singkatnya, not isinstance(gaji_baru, (int, float)) akan bernilai True jika gaji_baru BUKAN bertipe int atau float. Ini menangkap kasus di mana gaji_baru mungkin berupa string, list, dictionary, atau tipe data lain yang tidak valid untuk gaji.

"""





class karyawan:
    def __init__(self,nama,umur):
        self._nama = nama
        self._umur = umur

    @property
    def nama (self):
        return self._nama
    
    @nama.setter
    def ganti_nama(self,nama_baru):
        if not isinstance(nama_baru,(str)) :
            raise ValueError("woi nama kocak bukakn angka")
        self._nama =  nama_baru
        
karyawan1 = karyawan("irfan", 12)
print(f"halo nama saya adalah {karyawan1.nama} dan umur saya adalah {karyawan1._umur}")

karyawan1.ganti_nama = "claudia"
print(karyawan1.nama)