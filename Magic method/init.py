"""
 Konstruktor.
 Dipanggil saat Anda membuat instance baru dari sebuah kelas.
 Ini adalah tempat Anda menginisialisasi atribut objek.
"""

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(10) # __init__ dipanggil di sini