"""
__init__ adalah method contruktor yang dimana ketika kita pertamakali membuat objek otomatis kita memanggil objek tersebtut

sytaksinya adalah


class Pengguna:
    def __init__(self, username, email):
        self.username = username   maksud dari self.usernam adalah atribut
        self.email = email
        self.is_aktif = True # Atribut dengan nilai default

user1 = Pengguna("alice", "alice@example.com")
print(user1.username) # alice
print(user1.is_aktif) # True

self memiliki maksud merujuk objek dari class yang sedang dibuat

"""

class produk:
    def __init__(self,berat_produk,harga_produk):
        self.berat = berat_produk
        self.harga = harga_produk

        print(f"produk ini memiliki berat {self.berat} dan harga {self.harga} ")


produkA = produk("23 kg ","23 juta")