x = 4
#print(x)
#print("arta")

a = 5 #Integer
b = "1234" #String
c = 1.5 #Float
d = True #Boolean

#penamaan variable tidak boleh menggunakan karakter khusus didepan variable
angkaX = 5

#LIST
#Index dimulai dari 0
tipe_list = ["arta", "septi","vira","zahra"]
#multiple comment
"""
append menambahkan elemen di akhir list
tipe_list.append("Adit")
merubahd elemen berdasarkan index
tipe_list[1] = 5
"""
#tipe_list.pop(0) / menghapus data berdasaran index
#tipe_list.remove("arta") / menghapus data berdasarkan elemen
#print(tipe_list)


#LIST = Mutable / Elemen dapat diubah
#TUPLE = Imutable / Elemen tidak dapat diubah
#tipe_list = [1, 2, 3, 4, 5]
tipe_tuple = (1,2,3,4,5)
#print(tipe_tuple[1])

#SET
tipe_set = {1, 2, 3}
tipe_set.add(1)
tipe_set.remove(3)
#print(tipe_set)

#DICTIONARY
tipe_dictionary = {
    "name": "otong",
    "age": 21,
    "phone": "08532xxxx"
}
tipe_dictionary["prodi"] = "Teknik Informatika"
#tipe_dictionary.pop("name")
#print(tipe_dictionary)



#OPERATOR ARITMATIKA
angka_1 = 5
angka_2 = 2

penjumlahan = angka_1 + angka_2
pengurangan = angka_1 - angka_2
perkalian = angka_1 * angka_2
pembagian = angka_1 / angka_2
pembagian_bulat = angka_1 // angka_2
modulus = angka_1 % angka_2
pangkat = angka_1 ** angka_2
"""
print("penjumlahan : ", penjumlahan)
print("pengurangan : ", pengurangan)
print("perkalian : ", perkalian)
print("pembagian : ", pembagian)
print("pembagian_bulat : ", pembagian_bulat)
print("modulus : ", modulus)
print("pangkat : ", pangkat)
"""
#Menyambung string / variable = CONCATINATION /CONCAT
#print("hasilnya adalah :", hasil)
#print("septi " + " arta")
#print(f"{angka_1} dan {angka_2}")

#OPERATOR LOGIKA
# > < >= <= == !=
x = 4
y = 2
z = 5
#print(x >= y)

#AND OR NOT
if x != y:
    print("benar")
else:
    print("salah")