"""
class abstrak adalah class yang di guanakan untuk kerangka kerja sebuah class turunanaya
class abstrak tidak dapat di buat menjadi objek.tujuan dari kelas ini untuk mendefinisikan method dan varible di kelas turunanya

cara membuat abstrak method
-imprort terlebih dahulu sebua libary atau module bawaan python abc
-kelas haru mewarisi sebuah method abc
- buat dekorator @abstrak method
"""
from abc import ABC, abstractmethod

class bangun_data(ABC): #perlu turanan abc kalo mau buat abstrak method
    @abstractmethod #wajib kasig dekorator
    def luas(self):
        pass

    @abstractmethod
    def area(self):
        pass

class persegi(bangun_data):

    def __init__(self,panjang,lebar):
        super().__init__()
        self.panjang = panjang
        self.lebar = lebar


    def luas(self):
        return self.panjang * self.lebar
    
    def area(self):
        import math # tidak di sarankan
        return math.pi ** 2
    
persegi1 = persegi(12,31)
print(f"{persegi1.luas()}")
print(f'{persegi1.area()}')