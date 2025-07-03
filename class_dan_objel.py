"""
jadi class itu seperti  cetakan atau bluepirnt yang berisi atribut seperti variable ,method,funtion

objek adalah cetakan yang sudah berisi atribut dari 
"""

class biodata:
    pass # pass  adalah operasi yang memiliki nilai null yan berarrti pyton akan melopati operasi tersebut

biodata_kelas_1 = biodata()
biodata_kelas_1.nama = "Irfan medioker"
biodata_kelas_1.pacar = "claudia"
"""
__dict__ adalaha atribut khusus  yang dimiliki objek dan class yang menyipan dictionary dan nama space dari objek tersebut
"""

print(biodata_kelas_1.__dict__)
