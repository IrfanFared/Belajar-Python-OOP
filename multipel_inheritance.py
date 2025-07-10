"""
multiple inheritance adalah sebuah konsep dalam bahasa pemrograman yang di mana sebeuah sub class bisa mewarisi atribut dan method dari lebih dari class parent.
"""

class Kucing_arab:
    def bulu(self):
        print("biru tua")

class kucint_rusia:
    def ekor(self):
        print("ekor panjang")


class anak_kucing(kucint_rusia,Kucing_arab):
    pass


anak_kucing1 = anak_kucing()
anak_kucing1.bulu()
anak_kucing1.ekor()