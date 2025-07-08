class Mobil:
    jumlah_mobil = 0  # Ini adalah variabel kelas

    def __init__(self, merk, model):
        self.merk = merk
        self.model = model
        Mobil.jumlah_mobil += 1 # Setiap kali objek baru dibuat, tambahkan hitungan

    @classmethod
    def get_jumlah_mobil(cls):
        """
        Ini adalah class method.
        Parameter 'cls' secara otomatis merujuk pada kelas Mobil itu sendiri.
        Kita menggunakannya untuk mengakses variabel kelas 'jumlah_mobil'.
        """
        return cls.jumlah_mobil

# Membuat beberapa objek Mobil
mobil1 = Mobil("Toyota", "Avanza")
mobil2 = Mobil("Honda", "CR-V")
mobil3 = Mobil("Suzuki", "Ertiga")

# Memanggil class method untuk mendapatkan jumlah total mobil
# Kita memanggilnya melalui nama kelas, bukan objek
total_mobil_saat_ini = Mobil.get_jumlah_mobil()

print(f"Total mobil yang telah dibuat: {total_mobil_saat_ini}")
# Output: Total mobil yang telah dibuat: 3

print(f"Merk mobil 1: {mobil1.merk}")
# Output: Merk mobil 1: Toyota

print("--------"*10)

print(mobil1.merk)