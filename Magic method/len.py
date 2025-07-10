"""
digunakan untuk mengukur panjang objek
"""

class list:
    def __init__(self,list_angka):
        self.list = list_angka

    def __len__ (self):
        return len(self.list)
    
list1 = list([1,2,3,3,4,4,55,7])
print(len(list1))
        