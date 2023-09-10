# Python Project Pacmann - Super Cashier

## Tujuan Pengerjaan Project
Tujuan dari pengerjaan project ini adalah untuk membangun suatu program aplikasi kasir secara sederhana menggunakan bahasa pemrograman Python.

## Alur Program
1. Program cashier.py dijalankan menggunakan perintah python cashier.py di terminal.
2. Terdapat 9 fitur dalam program, yaitu:
    - Tambah Item
    - Update nama item
    - Update jumlah item
    - Update harga item
    - Update jumlah dan harga item
    - Hapus item
    - Reset Transaksi
    - Cek pesanan
    - Total Harga
3. Program dibangun secara sederhana sehingga pengguna hanya perlu mengikuti perintah yang tertulis di dalam program.

## Penjelasan Code
1. Library

![Library Pandas](images\library.png)

Library yang digunakan hanyalah library pandas

2. Class

![Class Transaction](images\class.png)

Class yang dibangun adalah Class Transaction yang menginisiasi pembentukan DataFrame yang berisi kolom nama, jumlah, harga satuan, dan total harga. Terdapat beberapa fungsi di dalam Class ini yang menjadi fitur utama dalam program ini.

3. While loop

![While loop](images\while_loop.png)

While loop dipakai untuk membantu pengguna memilih fitur-fitur yang ada pada program dan menjaga program tetap terus berjalan sampai pengguna sendiri yang mengakhirinya.

## Hasil Test Case
1. Add Item/Tambah Item

![Add Item/Tambah Item](images\add_item.png)

2. Delete Item/Hapus Item

![Delete Item/Hapus Item](images\delete_item.png)

3. Reset Transaction/Reset Transaksi

![Reset Transaction/Reset Transaksi](images\reset_transaction.png)

4. Total Price/Total Harga

![Total Price/Total Harga](images\total_price.png)

## Konklusi
Program cashier.py adalah program aplikasi kasir secara sederhana menggunakan bahasa pemrograman Python. Secara umum, program ini dapat mengerjakan hal-hal dasar selayaknya mesin kasir seperti menambah item, mengganti jumlah, mengganti harga, dll. Ke depannya, program ini dapat dikembangkan agar dapat memindai QR code ataupun barcode agar memudahkan pengguna untuk memasukkan nama item ataupun harga satuannya.