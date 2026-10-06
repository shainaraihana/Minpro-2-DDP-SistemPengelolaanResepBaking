import os
import pwinput
from prettytable import PrettyTable

resep = [
    ["Blueberry Cheese Toast", "Toast",
     "Roti Tawar, blueberry, cream cheese, gula",
     "Oleskan cream cheese pada roti tawar, tambahkan blueberry, lalu panggang"],

    ["Tiramisu", "Dessert",
      "Biskuit, kopi, mascarpone, gula, cokelat bubuk",
      "Celupkan biskuit ke kopi, susun dengan krim mascarpone, taburi cokelat bubuk, dinginkan"],

    ["Strawberry Cheese Cookies", "Cookies",
     "Tepung, butter, gula, cream cheese, strawberry",
     "Campur semua bahan, bentuk adonan menjadi bulat, panggang hingga matang"],

    ["Nutella Crepes", "Crepes",
     "Tepung, telur, susu, nutella, gula",
     "Buat adonan crepes, masak di teflon, oleskan nutella, lipat dan sajikan"]
]

akun = {
    "admin": {"password": "adminbaking"},
    "user": {"password": "userbaking"}

}

def login():
    while True:
        print("\n ======== SISTEM LOGIN ========")
        print("1. Admin")
        print("2. User")
        print("3. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            username = input("Masukkan username: ")
            password = pwinput.pwinput("Masukkan password: ")

            if username == "admin" and password == akun["admin"]["password"]:
                print("Login berhasil!")
                return "admin"
            else:
                print("Username atau password salah!")

        elif pilihan == "2":
            username = input("Masukkan username: ")
            password = pwinput.pwinput("Masukkan password: ")

            if username == "user" and password == akun["user"]["password"]:
                print("Login berhasil! Selamat datang, User.")
                os.system("cls")
                return "user"
            else:
                print("Username atau password salah!")

        elif pilihan == "3":
            print("Program selesai. Terimakasih!")
            return "keluar"
        else:
            print("Pilihan tidak valid!")

def lihat_resep():
    print("\n======== DAFTAR RESEP ========")

    if len(resep) == 0:
        print("Belum ada resep. ")
    else:
        tabel = PrettyTable()
        tabel.field_names = [
            "No", 
            "Nama Resep", 
            "Kategori", 
            "Bahan-bahan", 
            "Cara Membuat"
        ]

        for i in range(len(resep)):
            tabel.add_row([
                i + 1,
                resep[i][0],
                resep[i][1],
                resep[i][2],
                resep[i][3]
            ])
        print(tabel)

while True:
    username = login()

    if username == "keluar":
        break

    if username == "admin":
        while True:
            print("\n======== SISTEM PENGELOLAAN RESEP BAKING ========")
            print("1. Lihat Semua Resep")
            print("2. Tambah Resep")
            print("3. Ubah Resep")
            print("4. Hapus Resep")
            print("5. Keluar")

            pilihan = input("Pilih Menu: ")

            if pilihan == "1":
                lihat_resep()

            elif pilihan == "2":
                nama = input("Nama Resep: ")
                kategori = input("Kategori: ")
                bahan = input("Bahan-bahan: ")
                cara = input("Cara Membuat: ")

                if nama == "" or kategori == "" or bahan == "" or cara == "":
                    print("Input tidak boleh kosong!")
                else:
                    resep.append([nama, kategori, bahan, cara])
                    print("Resep berhasil ditambahkan!")

            elif pilihan == "3":
                print("\n======== DAFTAR RESEP ========")

                for i in range(len(resep)):
                    print(i + 1, ".", resep[i][0])

                try:
                    nomor = int(input("Pilih nomor resep yang ingin diubah: "))

                    if nomor >= 1 and nomor <= len(resep):
                        nama = input("Nama resep baru: ")
                        kategori = input("Kategori baru: ")
                        bahan = input("Bahan-bahan baru: ")
                        cara = input("Cara membuat baru: ")

                        if nama == "" or kategori == "" or bahan == "" or cara == "":
                            print("Input tidak boleh kosong!")
                        else:
                            resep[nomor - 1] = [nama, kategori, bahan, cara]
                            print("Resep berhasil diubah!")
                    else:
                        print("Nomor resep tidak valid!")

                except ValueError:
                    print("Input tidak valid! Masukkan angka.")

            elif pilihan == "4":
                print("\n======== DAFTAR RESEP ========")

                for i in range(len(resep)):
                    print(i + 1, ".", resep[i][0])

                try:
                    nomor = int(input("Pilih nomor resep yang ingin dihapus: "))

                    if nomor >= 1 and nomor <= len(resep):
                        resep.pop(nomor - 1)
                        print("Resep berhasil dihapus!")
                    else:
                        print("Nomor resep tidak valid!")

                except ValueError:
                    print("Input tidak valid! Masukkan angka.")

            elif pilihan == "5":
                print("Logout berhasil. Kembali ke menu login.")
                break

            else:
                print("Pilihan tidak valid!")

    elif username == "user":

        while True:
            print("\n======== SISTEM PENGELOLAAN RESEP BAKING ========")
            print("1. Lihat Semua Resep")
            print("2. Keluar")

            pilihan = input("Pilih Menu: ")

            if pilihan == "1":
                lihat_resep()

            elif pilihan == "2":
                print("Logout berhasil. Kembali ke menu login.")
                break

            else:
                print("Pilihan tidak valid!")