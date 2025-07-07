"""
sebuah private bukan bararti sebuah varibel yang tidak bisa diakses, tetapi sebuah variable yang hanya bisa diakses didalam class itu sendiri.
ya mudahnya private key itu kayak penanda bahwa variable itu hanya bisa diakses didalam class itu sendiri

ada dua privat di python yaitu: satu underscore (_) dan dua underscore (__)
satu underscore itu private key yang bisa diakses didalam class itu sendiri dan didalam subclass    
dua underscore itu private key yang hanya bisa diakses didalam class itu sendiri
"""
# konveisi satu undersire(_)
# kalau ada sebuah variable yang ditandai dengan satu uderscore variabel ini dimaksuakana u
# hanya di pakai  di dalam kelas ini saja. jangan di akses langsung dari luar.
# kita bisa menerobos tapi itu merusak sebua etika dan paterrn yang sudak berlaku

class BIodata_hewan:
    def __init__(self,nama):
        self._nama = nama

    def panggil_nama(self):
        print(f"{self._nama}")


kucing = BIodata_hewan("kucing oren")
kucing.panggil_nama() # ini adalah cara yang benar untuk mengakses sebuah variabele
print(kucing._nama) # ini salah kareana merusah sebuah patern 



"""
Kalau Anda melihat variabel yang diawali dengan dua underscore (__), misalnya __pin_rahasia, ini sedikit lebih "galak". Python akan melakukan name mangling, yaitu mengubah nama asli variabel tersebut. Tujuannya bukan semata-mata melarang akses dari luar,
 tapi lebih untuk menghindari konflik nama jika ada kelas turunan (subclass) yang punya nama variabel sama.
"""
class ATM:
    def __init__(self, pin):
        self.__pin_rahasia = pin # Ini akan di-mangle

    def verifikasi_pin(self, input_pin):
        return self.__pin_rahasia == input_pin

mesin_atm = ATM("12345")
# print(mesin_atm.__pin_rahasia) # Ini akan error! Python tidak mengenali nama ini.

# Untuk mengaksesnya secara "paksa" (yang tidak disarankan):
print(mesin_atm._ATM__pin_rahasia) # Ini bekerja karena sudah di-mangle


    

    