"""
IS UYGULAMASI

"""

# Problem:
# Belirli uğraşlar sonucunda alinan bir eğitimin katma değer sağlayip sağlamadiği ölçülmek isteniyor.

# Detaylar:
# Bir departman bir konuda eğitim talep ediyor
# Gerekli/gereksiz değerlendirmeleri neticesinde eğitim aliniyor ■ Eğitimden önce ve sonra olacak şekilde gerekli ölçümler yapiliyor
# Eğitim sonrasinda eğitimin sağladiği katma değer test edilmek isteniyor


# Bagimli iki Orneklem T Testi
# Bagimli iki grup ortalamasi arasinda karsilastirma yapilmak istenildiginde kullanilir.

# Egitimden once ve sonra Sirket personellerinin performans olculerine iliskin degerler: 

import pandas as pd
import numpy as np

before = pd.DataFrame([123,119,119,116,123,123,121,120,117,118,121,121,123,119,
            121,118,124,121,125,115,115,119,118,121,117,117,120,120,
            121,117,118,117,123,118,124,121,115,118,125,115])

after = pd.DataFrame([118,127,122,132,129,123,129,132,128,130,128,138,140,130,
             134,134,124,140,134,129,129,138,134,124,122,126,133,127,
             130,130,130,132,117,130,125,129,133,120,127,123])

mix = pd.concat([before, after], axis = 1)
mix.columns = ["Before", "After"]
#print(mix)



# 1.Veri seti
mix = pd.concat([before, after], axis = 1)
mix.columns = ["BEFORE","AFTER"]
#print("'mix' Veri Seti: \n\n ", mix.head(), "\n\n")


# 2.Veri seti
# Before Flag/Tag'ini olusturma
group_before = np.arange(len(before))
group_before = pd.DataFrame(group_before)
group_before = group_before.astype(str)
group_before[:] = "Before"

# Flag ve Oncesi degerlerini bir araya getirme
A = pd.concat([before, group_before], axis = 1)

# After Flag/Tag'ini olusturma
group_after = np.arange(len(after))
group_after = pd.DataFrame(group_after)
group_after = group_after.astype(str)
group_after[:] = "After"

# Flag ve Sonrasi degerlerini bir araya getirme
B = pd.concat([after, group_after], axis = 1)

# Tum veriyi bir araya getirme
together = pd.concat([A,B])


# isimlendirme
together.columns = ["Performans","Before-After"]
#print("'Birlikte' Veri Seti: \n\n", together.head(), "\n")

import seaborn as sns
import matplotlib.pyplot as plt
#sns.boxplot(x = "Before-After", y = "Performans", data = together, palette = ["green", "orange"])
#plt.show()

# After Performanslari gercekten de daha yuksek cikti. Ama,
# bu degerlerin tesadufen olusmadigini ispatlamak icin Varsayim Kontrollerini yapacagiz.


# Varsayim Kontrolleri (1)
from scipy.stats import shapiro
#print(shapiro(mix.BEFORE))      # p-value = 0.1072201247342477 (H0 Reddedilemez, Dagilim Normaldir.)
#print(shapiro(mix.AFTER))       # p-value = 0.6159508885102487 (H0 Reddedilemez, Dagilim Normaldir.)


# Varsayim Kontrolleri (2)
import scipy.stats as stats
#print(stats.levene(mix.BEFORE, mix.AFTER))  # p-value = 0.005084451180737039 (H0 Reddedilir, Varyans Homojenligi varsayimi Saglanmamaktadir.)


# Bagimli iki orneklem T Testi
#print(stats.ttest_rel(mix.BEFORE, mix.AFTER))
test_ist, pval = stats.ttest_rel(mix["BEFORE"], mix["AFTER"])
#print("Test istatistigi = %.4f, p-val = %.4f" % (test_ist, pval))   # p-value = 0.0000

# Yani Sirketin yapmis oldugu "calisan egitim serisi" ise yaramistir.



# Nonparametrik Bagimli iki Orneklem Testi
# Normallik varsayimi ve Varyans Homojenligi Saglanmadiginda Kullanilir.

test_ist, pval = stats.wilcoxon(mix.BEFORE, mix.AFTER)
print("Test istatistigi = %.4f, p-val = %.4f" % (test_ist, pval))   # p-value = 0.0000