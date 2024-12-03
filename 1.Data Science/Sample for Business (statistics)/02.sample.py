"""

IS UYGULAMASI

"""

# Problem:
# Çeşitli mecralara reklam veriliyor, reklamlarin tiklanma ve geri dönüşüm
# oranlari optimize edilmeye çalişiliyor. Buna yönelik olarak belirli bir
# mecrada çeşitli senaryolara göre reklama tiklama olasiliklari
# hesaplanmak isteniliyor.
 
# Detaylar:
# Bir mecrada reklam verilecek
# Dağilim ve reklama tiklama olasiliği biliniyor (0.01)
# Soru: Reklami 100 kişi gördüğünde 1,5,10 tiklanmasi olasiliği nedir?


from scipy.stats import binom

p = 0.01
n = 100
rv = binom(n, p)

print(rv.pmf(1))    #-> Verilen bir Reklami goren 100 kisiden 1 kisinin aksiyon alma ihtimali.
print(rv.pmf(5))
print(rv.pmf(10))