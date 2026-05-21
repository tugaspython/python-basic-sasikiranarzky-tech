# ==========================================
# FILE: jawaban_mahasiswa.py
# NAMA: [Sasikirana Rizky Ramadhania]
# NIM: [1251100074]
# ==========================================

def tambah(a, b):
    """
    Fungsi untuk menjumlahkan a dan b.
    """
    return a + b
    print(tambah(10, 20))

def kurang(a, b):
    """
    Fungsi untuk mengurangkan a dengan b.
    """
    return a - b 
    print(kurang(15, 15))

def kali(a, b):
    """
    Fungsi untuk mengalikan a dan b.
    """
    return a * b 
    print(kali(5, 8))

def bagi(a, b):
    """
    Fungsi untuk membagi a dengan b.
    """
    if b == 0 : 
        return "Error: Pembagian dengan nol tidak diperbolehkan"
    return a / b 
    print(bagi(10, 2))


print(tambah(10, 20))
print(kurang(15, 15))
print(kali(5, 8))
print(bagi(10, 2))
