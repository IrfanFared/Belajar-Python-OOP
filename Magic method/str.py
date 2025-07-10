"""
__str__ adalah sebuah method yang digunakan untuk merepretasikan objek ke dalam string yang mudah dipahami oleh manusia

ketika objek di print akan merepterstasikan objek string
"""
class biodata:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def __str__(self):
        return f"objek ini berisi atribut nama {self.nama} dan umur {self.umur}"

biodata1 = biodata("irfan", 14)
print(biodata1)