"""
Method Resolution Order (MRO)
Method Resolution Order (MRO) adalah konsep fundamental dalam multiple inheritance di Python.
MRO adalah urutan di mana Python mencari metode (dan atribut) dalam hierarki pewarisan ketika sebuah metode dipanggil pada sebuah objek.
Singkatnya, ketika Anda memiliki sebuah kelas yang mewarisi dari beberapa kelas induk, dan beberapa kelas induk tersebut (atau bahkan kelas leluhur yang lebih jauh) memiliki metode dengan nama yang sama, MRO adalah aturan yang menentukan metode mana yang akan dipanggil.
"""

class A:
    def siapa_aku(self):
        print("Saya adalah A")

class B(A):
    def siapa_aku(self):
        print("Saya adalah B")

class C(A):
    def siapa_aku(self):
        print("Saya adalah C")

class D(B, C): # D mewarisi dari B, lalu C
    pass

obj_d = D()
obj_d.siapa_aku() # jadi yang akan dijalanakan sesuai parameter yang pertama

