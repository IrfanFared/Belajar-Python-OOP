"""
fungsi utama getter adalahha untuk mendapatakan atau mengambil nilai dari atribut sebuah objek
beberapa fungsi umum
- untu mengaakses sebuah nilai dari properti 
- unutk menjaga integritas data encapsulucatuon
- getter bisa  menyertakan logika tamabahan sebelum mengembalikan data
"""

#contoh 

class Biodata:
    def __init__(self,nama,umur):
        self._nama = nama
        self._umur = umur

    @property
    def nama(self):
        return self._umur
    
    @property
    def umur(self):
        return self._umur
    
Biotata_irfan = Biodata("irfan",12)
print(Biotata_irfan.nama) # alih alih menmanggil method kita bisa gunakan seperti itu