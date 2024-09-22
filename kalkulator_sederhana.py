sambutan = "SELAMAT DATANG"
print(sambutan)

angkapertama = int(input("Masukan angka pertama : "))
angkakedua = int(input("Masukan angka kedua : "))

hasil_tambah = angkapertama+angkakedua
hasil_kali = angkakedua*angkapertama
hasil_bagi = angkapertama/angkakedua


print(f"ini adalah hasil dari {angkapertama} + {angkakedua} = {hasil_tambah} ")
print(f"ini adalah hasil dari {angkakedua} x {angkapertama} = {hasil_kali}")
print(f"ini adalah hasil dari {angkakedua} : {angkapertama} = {hasil_bagi}")
# print("hasil", angkapertama, "+", angkakedua, "=")
print(hasil_tambah, "\n")
print(hasil_kali)
print(hasil_bagi)
