"""
Diammond problem adalah sebeuah abiguitas yang terjadi di dalam konsep multipel inheritance yang diakibat sebuah kelas yang mewarisi atribut dan method yang nama variable sama dua kelas induk lalu kelas induk mewarisi kelas kake/nenek
"""
"""
  A (Kakek/Nenek)
     / \
    B   C (Induk 1 & Induk 2)
     \ /
      D (Anak)
Dalam skema ini:

A adalah kelas kakek/nenek (grandparent class).

B dan C adalah kelas induk (parent classes), dan keduanya mewarisi dari A.

D adalah kelas anak (child class) yang mewarisi dari B dan C.
"""

class kakek:
    def tanda(self):
        print("kakek")

class ayah(kakek):
     def tanda(self):
         print("mewarisi kakek 1")

class ibu(kakek):
    def tanda(self):
        print("mewarisi kakek 2")

class anak(ayah,ibu):
    def tanda(self):
        print("mewarisi darah ayah dan ibu")

anak1 = anak()
anak1.tanda()
print(anak.__mro__)


"""
Bagaimana Python Menyelesaikan Diamond Problem? (MRO)
Tidak seperti beberapa bahasa pemrograman lain yang mungkin melarang multiple inheritance atau memerlukan penanganan eksplisit dari ambiguitas semacam ini, Python mengatasi Diamond Problem dengan sangat baik menggunakan sebuah konsep yang disebut Method Resolution Order (MRO).

Seperti yang sudah kita bahas sebelumnya, MRO adalah urutan terdefinisi di mana Python mencari metode dalam hierarki pewarisan. Python menggunakan algoritma C3 Linearization untuk menentukan MRO, yang menghasilkan urutan pencarian yang konsisten dan dapat diprediksi.


Berdasarkan MRO ini, ketika obj_anak.metode_utama() dipanggil, Python akan mencari dalam urutan berikut:

Anak: Apakah Anak memiliki metode_utama? Tidak.

Induk1: Apakah Induk1 memiliki metode_utama? Ya! Jadi, metode_utama dari Induk1 akan dipanggil.
"""
