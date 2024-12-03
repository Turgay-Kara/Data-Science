"""

IS UYGULAMASI

"""

# Problem:
# Hatali ilan girişi olasiliklari hesaplanmak isteniyor.

# Detaylar:
# Bir yil süresince ölçümler yapiliyor
# Dağilim biliniyor (Poisson) ve Lambda 0.1 (ortalama hata sayisi)
# Hiç hata olmamasi, 3 hata olmasi ve 5 hata olmasi olasiliklari nedir?

from scipy.stats import poisson

lambda_ = 0.1       #-> Olaylarin ortalama gerceklesme orani
rv = poisson(mu = lambda_)

print(rv.pmf(k = 0))
print(rv.pmf(k = 3))
print(rv.pmf(k = 5))