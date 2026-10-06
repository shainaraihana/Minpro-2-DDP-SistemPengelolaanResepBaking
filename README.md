# Minpro-2-DDP-SistemPengelolaanResepBaking

Nama: Shaina Naila Raihana

NIM: 2609116090

Kelas: Kelas C

# PENJELASAN PROGRAM

Program Sistem Pengelolaan Resep Baking dibuat menggunakan Python untuk mengelola data resep baking. Program memiliki fitur login dengan dua jenis pengguna, yaitu admin dan user. Admin memiliki akses untuk melihat, menambah, mengubah, dan menghapus resep, sedangkan user hanya dapat melihat resep.

1. Library

Program menggunakan tiga library, yaitu:

- PrettyTable digunakan untuk menampilkan data resep dalam bentuk tabel agar lebih rapi.
- pwinput digunakan untuk menyembunyikan password saat proses login.
- os digunakan untuk membersihkan tampilan terminal setelah login berhasil.

<img width="265" height="42" alt="Screenshot 2026-10-06 201902" src="https://github.com/user-attachments/assets/3e5bedb7-41f1-4211-ab79-f339a1bd7332" />

2. Data Resep

Data resep disimpan dalam bentuk list yang berisi beberapa data resep. Setiap resep memiliki nama, kategori, bahan-bahan, dan cara membuat.

<img width="1238" height="510" alt="Screenshot (505)" src="https://github.com/user-attachments/assets/a172b06a-df15-428d-bc84-effaa2326de1" />

3. Dictionary Akun

Program menggunakan dictionary akun untuk menyimpan username dan password.

<img width="296" height="43" alt="Screenshot 2026-10-06 202117" src="https://github.com/user-attachments/assets/db81e0f4-aa3d-4f9a-a8fd-2837e27490d7" />

4. Function Login

Function login() digunakan untuk mengatur proses masuk ke program.

<img width="123" height="18" alt="Screenshot 2026-10-06 211137" src="https://github.com/user-attachments/assets/be2232eb-f84b-4ce2-af67-1c65945248b2" />

Saat dijalankan, program menampilkan:

<img width="384" height="145" alt="Screenshot (515)" src="https://github.com/user-attachments/assets/ca13fd21-647e-4f99-88be-5877c0119206" />

Jika memilih Admin, pengguna diminta memasukkan username dan password.

<img width="193" height="106" alt="Screenshot 2026-10-06 211412" src="https://github.com/user-attachments/assets/ea90770f-55b3-4226-a0a1-460f6c2aafda" />

Jika username atau password salah:

<img width="194" height="105" alt="Screenshot 2026-10-06 211550" src="https://github.com/user-attachments/assets/8c57ef86-1b17-4c4b-8224-8f85f7224cb0" />

Program akan kembali ke menu login.

Jika memilih user, tampilan nya akan sama seperti admin.

Jika memilih Keluar:

<img width="302" height="97" alt="Screenshot 2026-10-06 211915" src="https://github.com/user-attachments/assets/660ee2ce-d296-436e-b5f2-8d9d83613aa0" />

Program kemudian berhenti.

5. Function Lihat Resep

Function lihat_resep() digunakan untuk menampilkan seluruh resep.

<img width="160" height="16" alt="Screenshot 2026-10-06 202357" src="https://github.com/user-attachments/assets/10cf8d5c-6c68-4335-af80-30d058399fad" />

Contoh output:

<img width="913" height="226" alt="Screenshot 2026-10-06 212152" src="https://github.com/user-attachments/assets/b4256779-01ea-45d8-972c-ca88f160e511" />

Tampilan tabel dapat menyesuaikan lebar terminal.

6. Menu Admin

Setelah berhasil login sebagai admin, program menampilkan:

<img width="299" height="101" alt="Screenshot 2026-10-06 212339" src="https://github.com/user-attachments/assets/a84ae059-53fe-4421-a2dc-13dddd9c7f29" />

Admin memiliki akses CRUD.

a. Lihat Resep

Jika memilih:

<img width="89" height="17" alt="Screenshot 2026-10-06 212457" src="https://github.com/user-attachments/assets/e229cee8-6a07-4816-bbfe-a1ad60db1461" />

Program akan menampilkan seluruh resep menggunakan PrettyTable.

b. Tambah Resep

Jika memilih:

<img width="1113" height="342" alt="Screenshot (508)" src="https://github.com/user-attachments/assets/d6aa9e1f-8d29-46d0-a30a-18bff5120fc6" />

Output:

<img width="307" height="32" alt="Screenshot (508)" src="https://github.com/user-attachments/assets/5c0f6572-ab70-4983-befa-abac2f03708b" />

Data baru kemudian masuk ke dalam list resep.

c. Ubah Resep

Program menampilkan nomor resep:

<img width="535" height="149" alt="Screenshot 2026-10-06 213106" src="https://github.com/user-attachments/assets/fb78eaee-4405-4749-8e20-86901f9f86d7" />

Kemudian pengguna memasukkan data baru.

<img width="535" height="70" alt="Screenshot 2026-10-06 213106" src="https://github.com/user-attachments/assets/bd9dda02-39eb-4a70-b56c-9e3dc93b760c" />

d. Hapus Resep

Program menampilkan daftar resep dan meminta nomor resep:

<img width="553" height="231" alt="Screenshot (512)" src="https://github.com/user-attachments/assets/3f51a163-ba2b-481a-9627-5cc5d6b36e20" />

Resep yang dipilih akan dihapus menggunakan pop().

e. Keluar

Jika admin memilih:

<img width="650" height="239" alt="Screenshot (514)" src="https://github.com/user-attachments/assets/90c36abd-8893-4373-910d-f0e74ac43a80" />

Program tidak berhenti, tetapi kembali ke menu login

7. Menu User

Jika login sebagai user, menu yang tersedia hanya:

<img width="133" height="13" alt="Screenshot 2026-10-06 213113" src="https://github.com/user-attachments/assets/e04c3fa1-56f7-46f2-843c-1ab2b8144901" />

User hanya dapat melihat resep dan tidak dapat menambah, mengubah, atau menghapus resep.

Jika memilih 1:

<img width="913" height="226" alt="Screenshot 2026-10-06 212152" src="https://github.com/user-attachments/assets/80b1813e-18a9-4466-8ce7-abae6d192486" />

seluruh resep ditampilkan dalam bentuk tabel.

Jika memilih 2:

<img width="282" height="74" alt="Screenshot 2026-10-06 214136" src="https://github.com/user-attachments/assets/c736cc57-018c-4d91-922b-721efb1037af" />

Program kembali ke menu login.

8. Validasi Input

Program menggunakan conditional statement untuk melakukan validasi.

Contohnya saat menambah resep:

<img width="503" height="32" alt="Screenshot 2026-10-06 202832" src="https://github.com/user-attachments/assets/47aaea78-02bb-4d6a-aa2d-a58070010f8a" />

Jika pengguna tidak mengisi salah satu data:

<img width="167" height="65" alt="Screenshot 2026-10-06 214359" src="https://github.com/user-attachments/assets/28fe579f-b3a9-41c4-abbd-4d4ce3948301" />

Data tidak akan ditambahkan.

9. Error Handling

Program menggunakan try-except ketika pengguna memasukkan nomor resep.

<img width="368" height="35" alt="Screenshot 2026-10-06 214657" src="https://github.com/user-attachments/assets/8af95b19-782c-402a-869e-4d8a1075bbc7" />

Jika pengguna memasukkan huruf:

<img width="228" height="23" alt="Screenshot 2026-10-06 214742" src="https://github.com/user-attachments/assets/6de9fe6c-b591-4e38-a6d1-ac2f517b13db" />

Program tidak langsung berhenti/error, tetapi kembali ke menu.

10. Alur Program

Program dimulai dari login. Setelah login berhasil, pengguna akan diarahkan ke menu sesuai akun yang digunakan. Admin dapat melakukan CRUD resep, sedangkan user hanya dapat melihat resep. Setelah memilih Keluar, pengguna kembali ke halaman login. Program benar-benar berhenti ketika memilih Keluar pada halaman login.

# Alur Flowchart Program

1. Start

<img width="1175" height="732" alt="Screenshot (519)" src="https://github.com/user-attachments/assets/99da9784-76d3-4c14-b851-c3c701118554" />

Flowchart program dimulai dari Start, kemudian program menampilkan menu login yang terdiri dari pilihan Admin, User, dan Keluar.

Jika pengguna memilih Admin, program meminta username dan password. Data login akan diperiksa. Jika username atau password salah, program menampilkan pesan kesalahan dan kembali ke menu login. Jika benar, pengguna masuk ke Menu Admin.

2. Menu admin

<img width="1039" height="685" alt="Screenshot (517)" src="https://github.com/user-attachments/assets/5b62dd9f-8f17-4f93-80d0-72712edc3262" />

Pada Menu Admin terdapat lima pilihan. Pilihan pertama digunakan untuk melihat semua resep. Pilihan kedua digunakan untuk menambah resep baru. Pilihan ketiga digunakan untuk mengubah resep berdasarkan nomor resep yang dipilih. Pilihan keempat digunakan untuk menghapus resep. Pilihan kelima digunakan untuk keluar dari akun, kemudian program kembali ke menu login.

3. Menu user

<img width="510" height="697" alt="Screenshot (518)" src="https://github.com/user-attachments/assets/49a4dc9a-ead2-425f-95ec-4fb8985873c3" />

Jika pengguna memilih User, program juga meminta username dan password. Jika login berhasil, pengguna masuk ke Menu User. User hanya memiliki dua pilihan, yaitu melihat semua resep dan keluar. Jika memilih keluar, program kembali ke menu login.

Pada menu login, jika pengguna memilih Keluar, program menampilkan pesan bahwa program selesai dan proses berakhir pada End.
