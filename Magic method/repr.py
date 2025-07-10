"""
__repr__(self): Representasi String untuk Developer. Dipanggil oleh fungsi repr(). Tujuannya adalah memberikan representasi objek yang jelas dan tidak ambigu, idealnya yang dapat digunakan untuk membuat ulang objek tersebut.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(1, 2)
print(repr(p)) # Output: Point(1, 2)

