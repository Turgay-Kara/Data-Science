"""

IS UYGULAMASI

"""


# Problem:
# Anasayfa'da geçirilen süre artirilmak isteniyor.

# Detaylar:
# Bir web sitesi için başari kriterleri: ortalama ziyaret süresi, hemen çikiş orani vb
# Uzun zaman geçiren kullanicilarn reklamlara daha fazla tikladiği ve markaya olan bağliliklarinin arttiği biliniyor.
# Buna yönelik olarak benzer haberler farkli resimler ya da farkli formatlarda hazirlanarak oluşturulan test gruplarina gösteriliyor.
# A: Doğal Şekilde, B: Yönlendirici, C: İlgi Çekici


# Varyans Analizi: 2 veya dahya fazla grup ortalmasi arasinda istatiksel
# olarak anlamli farklilik olup olmadigi ogrenilmek istenildiginde kullanilir.

# H0 = Hipotezler birbirine Esittir.
# H1 = En az 1 hipotez Farklidir.

import pandas as pd

# Gecirilen Saniyeler:
A = pd.DataFrame([28,33,30,29,28,29,27,31,30,32,28,33,25,29,27,31,31,30,31,34,30,32,31,34,28,32,31,28,33,29])
B = pd.DataFrame([31,32,30,30,33,32,34,27,36,30,31,30,38,29,30,34,34,31,35,35,33,30,28,29,26,37,31,28,34,33])
C = pd.DataFrame([40,33,38,41,42,43,38,35,39,39,36,34,35,40,38,36,39,36,33,35,38,35,40,40,39,38,38,43,40,42])

dfs = [A, B, C]

ABC = pd.concat(dfs, axis = 1)
ABC.columns = ["GRUP_A","GRUP_B","GRUP_C"]
print(ABC.head())


# Normallik Varsayimi
from scipy.stats import shapiro
print(shapiro(ABC["GRUP_A"]))       # p-value = 0.5321
print(shapiro(ABC["GRUP_B"]))       # p-value = 0.7979
print(shapiro(ABC["GRUP_C"]))       # p-value = 0.2738
# H0 Reddedilemez. Normallik varsayimi saglaniyor.


# Homojenlik Varsayimi
import scipy.stats as stats
print(stats.levene(ABC["GRUP_A"], ABC["GRUP_B"], ABC["GRUP_C"]))
# H0 Reddedilemez. Homojenlik varsayimi saglaniyor.



# Hipotez Testi
from scipy.stats import f_oneway
print(f_oneway(ABC["GRUP_A"], ABC["GRUP_B"], ABC["GRUP_C"]))
print("{:.4f}".format(f_oneway(ABC["GRUP_A"], ABC["GRUP_B"], ABC["GRUP_C"])[1]))    # p-value = 0.0000
# H0 Reddedilir. Gruplar arasinda anlamli bir farklilik var.

print(ABC.describe().T)
# boxplot ciz



# Normallik ve Homojenlik Saglanmaz ise Kullanacagimiz Yontem:
from scipy.stats import kruskal
print(kruskal(ABC["GRUP_A"], ABC["GRUP_B"], ABC["GRUP_C"]))
print("{:.4f}".format(kruskal(ABC["GRUP_A"], ABC["GRUP_B"], ABC["GRUP_C"])[1]))    # p-value = 0.0000
# H0 Reddedilir. Gruplar arasinda anlamli bir farklilik var.
# En az 1 Grup diger gruplardan Farklidir.