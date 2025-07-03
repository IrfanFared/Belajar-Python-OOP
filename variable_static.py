"""
varibel statis adalah variabel yang hanya dimikiki di kelas itu sendiri
hanya satu salinan saja yang berarti sabanyak apapun anda membaut objek.semua objek yang anda buat akan akan bebagi salinan variabel ini
dingungakn sebagai variabek konsta atau bisa digunakan untuk mengitung berapa banya objek yang bisa dibuat
"""

class Kucing:
    # Ini adalah ATRIBUT KELAS (variabel statis)
    # Semua objek Kucing akan berbagi nilai ini
    jumlah_kaki = 4
    populasi_kucing = 0 # Mengikuti berapa banyak objek Kucing yang dibuat

    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna
        # Setiap kali objek Kucing baru dibuat, tambahkan 1 ke populasi_kucing
        Kucing.populasi_kucing += 1 # Mengakses atribut kelas melalui nama kelas

    def info(self):
        print(f"Saya {self.nama}, kucing {self.warna}.")
        print(f"Saya punya {Kucing.jumlah_kaki} kaki.") # Mengakses atribut kelas
        print(f"Total populasi kucing saat ini: {Kucing.populasi_kucing}") # Mengakses atribut kelas

# --- Membuat Objek Kucing ---

kucing1 = Kucing("Kitty", "Oren")
kucing1.info()

print("\n---")

kucing2 = Kucing("Miko", "Hitam")
kucing2.info()

print("\n---")

kucing3 = Kucing("Leo", "Putih")
kucing3.info()

print("\n---")

# Mengakses atribut kelas langsung dari kelas itu sendiri
print(f"Jumlah kaki default untuk kucing: {Kucing.jumlah_kaki}")
print(f"Total kucing di sistem: {Kucing.populasi_kucing}")

# Mengakses atribut kelas dari objek (tetapi ini sebenarnya tetap merujuk ke atribut kelas)
print(f"Kucing 1 (Kitty) mengira ada {kucing1.populasi_kucing} kucing.")