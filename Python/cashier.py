import pandas as pd

class Transaction:

  def __init__(self):
    self.order = pd.DataFrame(columns=["Nama", "Jumlah", "Harga Satuan", "Harga Total"])

  def add_item(self, *pesanan):
    if len(pesanan) == 0 or len(pesanan) %3 != 0:
      print("Input pesanan tidak sesuai. Silakan mengikuti format add_item(<nama item>, <jumlah item>, <harga item>) tanpa penggunaan tanda <>.")
    else:
      for i, j, k in zip(range(0, len(pesanan), 3), range(1, len(pesanan), 3), range(2, len(pesanan), 3)):
        if pesanan[i].lower() in [nama.lower() for nama in self.order["Nama"].unique()]:
          print(f"{pesanan[i]} sudah ada dalam daftar pesanan. Mohon gunakan nama atau fitur lain.")
        elif type(pesanan[j]) != int:
          print(f"Input {pesanan[i]}, {pesanan[j]}, {pesanan[k]} tidak sesuai. Jumlah {pesanan[j]} harus dalam format numerik. Program hanya menampilkan pesanan dengan format yang sesuai.")
        elif type(pesanan[k]) != int:
          print(f"Input {pesanan[i]}, {pesanan[j]}, {pesanan[k]} tidak sesuai. Harga {pesanan[k]} harus dalam format numerik. Program hanya menampilkan pesanan dengan format yang sesuai.")
        else:
          self.order = pd.concat([self.order, pd.DataFrame.from_records([{"Nama": pesanan[i], "Jumlah": pesanan[j], "Harga Satuan": pesanan[k], "Harga Total": pesanan[j]*pesanan[k]}])], ignore_index=True)
      return self.order

  def update_item_name(self, *pesanan):
    if len(pesanan) == 0 or len(pesanan) %2 != 0:
      print("Input pesanan tidak sesuai. Silakan mengikuti format update_item_name(<nama lama item>, <nama baru item>) tanpa penggunaan tanda <>.")
    else:
      for i, j in zip(range(0, len(pesanan), 2), range(1, len(pesanan), 2)):
        if pesanan[j] in [nama.lower() for nama in self.order["Nama"].unique()]:
          print(f"{pesanan[j]} sudah ada dalam daftar pesanan. Mohon gunakan nama atau fitur lain.")
        else:
          if pesanan[i] not in [nama.lower() for nama in self.order["Nama"].unique()]:
            print(f"{pesanan[i]} belum ada dalam daftar pesanan. Mohon gunakan nama atau fitur lain.")
          else:
            self.order["Nama"] = self.order["Nama"].replace(pesanan[i], pesanan[j])
      return self.order

  def update_item_qty(self, *pesanan):
    if len(pesanan) == 0 or len(pesanan) %2 != 0:
      print("Input pesanan tidak sesuai. Silakan mengikuti format update_item_qty(<nama item>, <jumlah baru item>) tanpa penggunaan tanda <>.")
    else:
      for i, j in zip(range(0, len(pesanan), 2), range(1, len(pesanan), 2)):
        if type(pesanan[j]) != int:
          print(f"Jumlah item {pesanan[j]} harus dalam format numerik. Program hanya menampilkan pesanan dengan format yang sesuai.")
        else:
          if pesanan[i] not in [nama.lower() for nama in self.order["Nama"].unique()]:
            print(f"{pesanan[i]} belum ada dalam daftar pesanan. Mohon gunakan nama atau fitur lain.")
          else:
            self.order.loc[self.order["Nama"] == pesanan[i], "Jumlah"] = pesanan[j]
            self.order["Harga Total"] = self.order.apply(lambda row: row["Jumlah"] * row["Harga Satuan"], axis=1)
      return self.order

  def update_item_price(self, *pesanan):
    if len(pesanan) == 0 or len(pesanan) %2 != 0:
      print("Input pesanan tidak sesuai. Silakan mengikuti format update_item_qty(<nama item>, <harga baru item>) tanpa penggunaan tanda <>.")
    else:
      for i, j in zip(range(0, len(pesanan), 2), range(1, len(pesanan), 2)):
        if type(pesanan[j]) != int:
          print(f"Harga item {pesanan[j]} harus dalam format numerik. Program hanya menampilkan pesanan dengan format yang sesuai.")
        else:
          if pesanan[i] not in [nama.lower() for nama in self.order["Nama"].unique()]:
            print(f"{pesanan[i]} belum ada dalam daftar pesanan. Mohon gunakan nama atau fitur lain.")
          else:
            self.order.loc[self.order["Nama"] == pesanan[i], "Harga Satuan"] = pesanan[j]
            self.order["Harga Total"] = self.order.apply(lambda row: row["Jumlah"] * row["Harga Satuan"], axis=1)
      return self.order

  def update_item_qty_price(self, *pesanan):
    if len(pesanan) == 0 or len(pesanan) %3 != 0:
      print("Input pesanan tidak sesuai. Silakan mengikuti format update_item_qty(<nama item>, <jumlah item>, <harga item>) tanpa penggunaan tanda <>.")
    else:
      for i, j, k in zip(range(0, len(pesanan), 3), range(1, len(pesanan), 3), range(2, len(pesanan), 3)):
        if pesanan[i] not in [nama.lower() for nama in self.order["Nama"].unique()]:
          print(f"{pesanan[i]} belum ada dalam daftar pesanan. Mohon gunakan nama atau fitur lain.")
        elif type(pesanan[j]) != int:
          print(f"Input {pesanan[i]}, {pesanan[j]}, {pesanan[k]} tidak sesuai. Jumlah {pesanan[j]} harus dalam format numerik. Program hanya menampilkan pesanan dengan format yang sesuai.")
        elif type(pesanan[k]) != int:
          print(f"Input {pesanan[i]}, {pesanan[j]}, {pesanan[k]} tidak sesuai. Harga {pesanan[k]} harus dalam format numerik. Program hanya menampilkan pesanan dengan format yang sesuai.")
        else:
          self.order.loc[self.order["Nama"] == pesanan[i], ["Jumlah", "Harga Satuan"]] = pesanan[j], pesanan[k]
          self.order["Harga Total"] = self.order.apply(lambda row: row["Jumlah"] * row["Harga Satuan"], axis=1)
      return self.order

  def delete_item(self, *pesanan):
    if len(pesanan) == 0:
      print("Input pesanan tidak sesuai. Silakan mengikuti format delete_item(<nama item>) tanpa penggunaan tanda <>.")
    else:
      for i in range(len(pesanan)):
        if pesanan[i] not in [nama.lower() for nama in self.order["Nama"].unique()]:
          print(f"{pesanan[i]} belum ada dalam daftar pesanan. Mohon gunakan nama atau fitur lain.")
        else:
          self.order.drop(self.order[self.order["Nama"] == pesanan[i]].index, inplace = True)
          self.order.reset_index(inplace = True, drop = True)
      return self.order

  def reset_transaction(self):
     self.order = pd.DataFrame(columns=["Nama", "Jumlah", "Harga Satuan", "Harga Total"])
     print("Semua pesanan berhasil dihapus.")

  def check_order(self):
    return self.order

  def total_price(self):
    totalprice = self.order["Harga Total"].sum()
    if totalprice > 500000:
      totalprice_new = totalprice * 0.9
      print(f"Total pembelian sebesar {totalprice}. Berdasarkan aturan yang berlaku, total pembelian yang melebihi Rp 500.000 akan mendapatkan diskon sebesar 10% sehingga jumlah yang perlu dibayar adalah sebesar {totalprice_new}")
    elif totalprice > 300000:
      totalprice_new = totalprice * 0.92
      print(f"Total pembelian sebesar {totalprice}. Berdasarkan aturan yang berlaku, total pembelian yang melebihi Rp 300.000 akan mendapatkan diskon sebesar 8% sehingga jumlah yang perlu dibayar adalah sebesar {totalprice_new}")
    elif totalprice > 200000:
      totalprice_new = totalprice * 0.95
      print(f"Total pembelian sebesar {totalprice}. Berdasarkan aturan yang berlaku, total pembelian yang melebihi Rp 200.000 akan mendapatkan diskon sebesar 2% sehingga jumlah yang perlu dibayar adalah sebesar {totalprice_new}")
    else:
      print(f"Total pembelian sebesar {totalprice}.")

transaction = Transaction()

while True:
    print("")
    print("Pilih opsi:")
    print("1. Tambah item")
    print("2. Update nama item")
    print("3. Update jumlah item")
    print("4. Update harga item")
    print("5. Update jumlah dan harga item")
    print("6. Hapus item")
    print("7. Reset transaksi")
    print("8. Cek pesanan")
    print("9. Total harga")
    print("0. Keluar")
    print("")
    choice = input("Masukkan nomor opsi: ")

    if choice == "1":
        name = input("Masukkan Nama Item: ")
        try:
          quantity = int(input("Masukkan Jumlah Item: "))
          price = int(input("Masukkan Harga Item: "))
          print("")
          print(transaction.add_item(name, quantity, price))
        except:
          print("Input jumlah/harga item tidak sesuai. Mohon gunakan angka untuk memasukkan jumlah/harga item.")
    elif choice == "2":
        name_old = input("Masukkan Nama Item: ")
        name_new = input("Masukkan Nama Baru Item: ")
        print("")
        print(transaction.update_item_name(name_old, name_new))
    elif choice == "3":
        name = input("Masukkan Nama Item: ")
        try:
            quantity = int(input("Masukkan Jumlah Item: "))
            print("")
            print(transaction.update_item_qty(name, quantity))
        except:
          print("Input jumlah item tidak sesuai. Mohon gunakan angka untuk memasukkan jumlah item.")
    elif choice == "4":
        name = input("Masukkan Nama Item: ")
        try:
            price = int(input("Masukkan Harga Item: "))
            print("")
            print(transaction.update_item_price(name, price))
        except:
          print("Input harga item tidak sesuai. Mohon gunakan angka untuk memasukkan harga item.")
    elif choice == "5":
        name = input("Masukkan Nama Item: ")
        try:
          quantity = int(input("Masukkan Jumlah Item: "))
          price = int(input("Masukkan Harga Item: "))
          print("")
          print(transaction.update_item_qty_price(name, quantity, price))
        except:
          print("Input jumlah/harga item tidak sesuai. Mohon gunakan angka untuk memasukkan jumlah/harga item.")
    elif choice == "6":
        name = input("Masukkan Nama Item: ")
        print("")
        print(transaction.delete_item(name))
    elif choice == "7":
        print("")
        transaction.reset_transaction()
    elif choice == "8":
        print("")
        print(transaction.check_order())
    elif choice == "9":
        print("")
        transaction.total_price()
    elif choice == "0":
        print("Program selesai.")
        break
    else:
        print("Opsi tidak valid. Silakan pilih opsi yang benar.")