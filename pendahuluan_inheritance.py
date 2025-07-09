"""
inheritance adalah salah satu konsep pewarisan di dalam python oop yang memukinkan sebuah childd dapa memwarisi method dari parent clsss
 Mengapa inheritance sangat pengting
- memukinkan sebuah class dapat memwarisi atribut dan method dari class lain .jadinya kita hanya membuat 1 class untuk class lain
- meukinkan kita untuk mengoveride method parent class
- memukinkan kita mengubah memeperluas fungsionlaitas tanpa menguabah struktur kode dari parent class
"""

#contoh

class hewan:
    def __init__(self,nama):
        self.nama = nama

    def suara(self):
        raise NotImplementedError("hewan harus bersuara")
    
class kucing(hewan):
    def __init__(self, nama,suara): #digunakan untuk memangguk metode(kontruktor __init__)
        super().__init__(nama)
        self.suara = suara
    
    def suara(self):
        return print(f"bersuara {self.suara}")
    
kucing1 = kucing("momochan","miaum")



print(kucing1.suara)