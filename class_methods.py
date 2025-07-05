"""
Metode kelas adalah metode yang "milik" kelas itu sendiri, bukan objek individual. Mereka berguna untuk operasi yang berkaitan dengan kelas secara keseluruhan.
Apa Fungsinya?
Metode kelas memiliki akses ke kelas itu sendiri (melalui parameter cls), dan dapat digunakan untuk mengakses atau memodifikasi atribut kelas (variabel kelas). Mereka juga sangat sering digunakan sebagai konstruktor alternatif (factory methods) untuk membuat instance dari kelas dengan cara yang berbeda dari konstruktor __init__ standar







"""

class Kue:
    # Ini adalah atribut kelas (milik semua kue yang dibuat dari cetakan ini)
    # Ini seperti bahan dasar yang ada di dapur yang akan dipakai semua resep
    DEFAULT_FILLING = "Cokelat"
    TOTAL_KUE_TERBUAT = 0

    def __init__(self, rasa, berat_gram):
        self.rasa = rasa          # Atribut instance: rasa unik kue ini
        self.berat_gram = berat_gram  # Atribut instance: berat unik kue ini
        Kue.TOTAL_KUE_TERBUAT += 1 # Tambah hitungan setiap kue dibuat

    def display_info(self):
        """Metode Instance: Menampilkan info kue spesifik ini."""
        print(f"Ini kue rasa {self.rasa}, berat {self.berat_gram} gram, isi default: {Kue.DEFAULT_FILLING}")

    @classmethod
    def ubah_isi_default(cls, new_filling):
        """
        Metode Kelas: Mengubah isi default untuk SEMUA kue yang akan dibuat
        setelah ini. Ini mengubah 'resep' atau 'cetakan'nya.
        """
        print(f"Mengubah isi default dari '{cls.DEFAULT_FILLING}' menjadi '{new_filling}'.")
        cls.DEFAULT_FILLING = new_filling # Mengubah atribut kelas melalui 'cls'

    @classmethod
    def buat_kue_mini(cls, rasa):
        """
        Metode Kelas (Factory Method): Membuat kue dengan berat standar mini.
        Ini adalah cara alternatif membuat kue.
        """
        print(f"Membuat kue mini rasa {rasa}...")
        # 'cls(rasa, 100)' berarti memanggil konstruktor Kue.__init__(rasa, 100)
        return cls(rasa, 100) # 'cls' di sini adalah referensi ke kelas 'Kue'

    @classmethod
    def get_jumlah_kue(cls):
        """
        Metode Kelas: Mengembalikan total kue yang sudah dibuat.
        Mengakses atribut kelas 'TOTAL_KUE_TERBUAT'
        """
        return cls.TOTAL_KUE_TERBUAT

# --- Bagian 1: Memahami 'cls' untuk Mengakses/Mengubah Atribut Kelas ---

print("--- Demonstrasi Atribut Kelas ---")
kue_biasa1 = Kue("Vanila", 250)
kue_biasa1.display_info() # Output: Ini kue rasa Vanila, berat 250 gram, isi default: Cokelat

# Mengubah isi default menggunakan metode kelas
# Perhatikan, kita memanggilnya dari NAMA KELAS, bukan objek
Kue.ubah_isi_default("Strawberry")

kue_biasa2 = Kue("Cokelat Chip", 300)
kue_biasa2.display_info() # Output: Ini kue rasa Cokelat Chip, berat 300 gram, isi default: Strawberry
                          # Isi default ikut berubah karena kita mengubah 'cetakan'nya

print(f"\nTotal kue yang sudah dibuat: {Kue.get_jumlah_kue()}")


# --- Bagian 2: Memahami 'cls' sebagai Konstruktor Alternatif (Factory Method) ---

print("\n--- Demonstrasi Factory Method ---")
# Daripada membuat kue langsung pakai Kue("Lemon", 100), kita pakai metode kelas
kue_mini_lemon = Kue.buat_kue_mini("Lemon")
kue_mini_lemon.display_info() # Output: Ini kue rasa Lemon, berat 100 gram, isi default: Strawberry

# Membuat kue mini rasa Blueberry
kue_mini_blueberry = Kue.buat_kue_mini("Blueberry")
kue_mini_blueberry.display_info()

print(f"\nTotal kue yang sudah dibuat: {Kue.get_jumlah_kue()}")