"""
__getitem__(self, key): Akses Item (Indexing). Dipanggil saat Anda mencoba mengakses item menggunakan notasi [] (misalnya, o
"""
class MyDict:
    def __init__(self):
        self._data = {}

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]

my_dict = MyDict()
my_dict["nama"] = "Budi" # memanggil __setitem__
print(my_dict["nama"])   # memanggil __getitem__