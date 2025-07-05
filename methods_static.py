"""
Metode statis adalah metode yang paling independen dari ketiga jenis metode ini. Mereka tidak peduli dengan instance maupun kelas.
Apa Fungsinya?
Metode statis berfungsi seperti fungsi Python biasa, tetapi secara logis terkait dengan sebuah kelas dan ditempatkan di dalamnya untuk alasan organisasi. Mereka tidak memiliki akses ke atribut instance atau atribut kelas.

Bagaimana Mengidentifikasinya?
Mereka tidak memiliki parameter self atau cls sebagai yang pertama.

Anda harus mendekorasinya dengan @staticmethod.
Kapan Menggunakannya?
Gunakan metode statis ketika:

Metode melakukan tugas utilitas atau perhitungan yang tidak memerlukan data spesifik dari objek atau kelas.

Metode tidak memodifikasi keadaan objek atau keadaan kelas.

Metode bisa saja ditempatkan sebagai fungsi mandiri di luar kelas, tetapi menempatkannya di dalam kelas membuatnya lebih terorganisir dan jelas secara semantik.

"""

class MathUtils:
    @staticmethod
    def add(x, y):
        """
        Metode statis: Menjumlahkan dua angka.
        Tidak membutuhkan self atau cls.
        """
        return x + y

    @staticmethod
    def subtract(x, y):
        """
        Metode statis: Mengurangi dua angka.
        Tidak membutuhkan self atau cls.
        """
        return x - y

    @staticmethod
    def is_even(number):
        """
        Metode statis: Memeriksa apakah angka genap.
        Tidak membutuhkan self atau cls.
        """
        return number % 2 == 0

# Memanggil metode statis melalui nama kelas (cara paling umum)
print(f"5 + 3 = {MathUtils.add(5, 3)}")       # Output: 5 + 3 = 8
print(f"10 - 4 = {MathUtils.subtract(10, 4)}") # Output: 10 - 4 = 6
print(f"Is 7 even? {MathUtils.is_even(7)}")   # Output: Is 7 even? False

# Anda juga bisa memanggilnya melalui instance, tapi ini tidak menambahkan nilai apapun
# Karena mereka tidak beroperasi pada instance data
math_obj = MathUtils()
print(f"Is 8 even (via instance)? {math_obj.is_even(8)}") # Output: Is 8 even (via instance)? True