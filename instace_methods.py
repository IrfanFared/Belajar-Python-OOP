"""
metode instace beroperasi pada objek yang dibuat dari kelas
berbeda dengan metode kelas yang beroperasi pada kelas itu sendiri
metode instace biasanya digunakan untuk mengakses atau memanipulssi atribut objek 
berfungsi untu memberikan perilaku khusus pada objek tersebut

Kapan Menggunakannya?
Gunakan metode instance ketika:

Metode perlu berinteraksi dengan atribut unik dari setiap objek (misalnya, nama, usia, saldo).

Metode perlu memanggil metode lain yang juga merupakan bagian dari objek tersebut.

Metode menggambarkan perilaku atau aksi yang dilakukan oleh objek individual.
"""

class BankAccount:
    def __init__(self, owner_name, initial_balance=0):
        # Ini adalah atribut instance, unik untuk setiap objek BankAccount
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Metode instance: Menambahkan uang ke saldo akun ini.
        Menggunakan 'self.balance' untuk mengakses saldo akun spesifik.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance for {self.owner_name}: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Metode instance: Mengurangi uang dari saldo akun ini.
        Memeriksa 'self.balance' dan memodifikasinya.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. New balance for {self.owner_name}: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        """
        Metode instance: Mengembalikan saldo akun ini.
        Mengakses 'self.balance'.
        """
        return self.balance

# Membuat objek BankAccount (instance)
account1 = BankAccount("Alice", 100)
account2 = BankAccount("Bob") # Bob starts with 0 balance

# Memanggil metode instance pada objek account1
account1.deposit(50)
print(f"Alice's current balance: ${account1.get_balance()}")

# Memanggil metode instance pada objek account2
account2.deposit(200)
account2.withdraw(50)
print(f"Bob's current balance: ${account2.get_balance()}")

# Perhatikan bahwa aksi pada account1 tidak mempengaruhi account2, dan sebaliknya.