"""

IS UYGULAMASI

"""

# Problem:
# Bir yatirim/toplanti öncesinde gelecek ay ile ilgili satişlarin
# belirli değerlerde gerçekleşmesi olasiliklari belirlenmek isteniyor.

# Detaylar:
# Dağilimin normal olduğu biliniyor
# Aylik ortalama satiş sayisi 80K, standart sapmasi 5K
# 90K'dan fazla satiş yapma olasiliği nedir?

from scipy.stats import norm

print(1-norm.cdf(90, 80, 5))                       #-> .cdf(hesaplanmak istenen deger, ortalama, standar sapma) #(90dan fazla olma olasiligi-> 0.022...)
print(1-norm.cdf(70, 80, 5))
print(norm.cdf(73, 80, 5))                         #-> 73'ten az olma olasiligi.
print(norm.cdf(90, 80, 5) - norm.cdf(85, 80, 5))   #-> 85 ile 90 arasinda olma olasiligi.