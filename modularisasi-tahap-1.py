"""
Program menghitung luas segitiga
luas_segitiga = alas * tinggi / 2
"""
print('Menghitung luas segitiga tanpa fungsi')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luar {luas_segitiga}')

alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luar {luas_segitiga}')

print('\nMempersiapkan fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi /2
    return luas_segitiga

print(f'Menghitung luas segitiga dengan fungsi hasilnya: {hitung_luas_segitiga(10, 6)}')
print(f'Menghitung luas segitiga dengan fungsi hasilnya: {hitung_luas_segitiga(20, 2)}')

