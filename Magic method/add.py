"""
__add__(self, other): Operasi Penambahan. Dipanggil saat Anda menggunakan operator + pada objek Anda.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2 # __add__ dipanggil di sini
print(f"v3: ({v3.x}, {v3.y})") # Output: v3: (4, 6)