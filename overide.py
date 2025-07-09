"""
overide adalah salah satu konsep dalam pewarisan di dalam python oop yang memungkinkan sebuah child class untuk mengubah atau memperluas perilaku dari method yang diwarisi dari parent class. 
dengan mengoveride method,kita dapat memberikan implementasi yang lebih spesifik atau berbeda sesuai dengan kebutuhan child class tersebut
"""
# contoh
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        raise NotImplementedError("Hewan harus bersuara")
class Kucing(Hewan):
    def __init__(self, nama, suara):
        super().__init__(nama)
        self.suara = suara

    def suara(self):
        return f"{self.nama} bersuara {self.suara}" # mengoveride method suara dari parent class Hewan
class Anjing(Hewan):
    def __init__(self, nama, suara):
        super().__init__(nama)
        self.suara = suara

    def suara(self):
        return f"{self.nama} bersuara {self.suara}" # mengoveride method suara dari parent class Hewan      
# contoh penggunaan
kucing1 = Kucing("Momochan", "Miaum")
anjing1 = Anjing("Bobby", "Guk guk")        
print(kucing1.suara())  # Output: Momochan bersuara Miaum
print(anjing1.suara())  # Output: Bobby bersuara Guk guk
# Output: Momochan bersuara Miaum
# Output: Bobby bersuara Guk guk    