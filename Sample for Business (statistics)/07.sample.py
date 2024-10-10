"""

IS UYGULAMASI

"""

# Problem:
# Bir ML projesine yatirim yapilmiş. Ürettiği tahminler neticesinde oluşan gelir ile
# eski sistemin ürettiği gelirler karşilaştirilip anlamli farklilik olup olmadiği test edilmek isteniyor.

# Detaylar:
# Model geliştirilmiş ve web sitesine entegre edilmiş.
# Site kullanicilari belirli bir kurala göre ikiye bölünmüş olsun.
# A grubu eski B grubu yeni sistem.
# Gelir anlaminda anlamli bir iş yapilip yapilmadiği test edilmek isteniyor.


# veri setinin duzenlenmesi (en zor sekli ile)
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import shapiro
import scipy.stats as stats
import matplotlib.pyplot as plt

A = pd.DataFrame([30,27,21,27,29,30,20,20,27,32,35,22,24,
                  23,27,23,27,23,25,21,18,24,26,27,28,19,25])

B = pd.DataFrame([37,39,31,31,34,38,30,36,29,28,38,28,37,
                  37,30,32,31,31,27,32,33,33,33,31,32,33,26])


# Grup A
grup_a = np.arange(len(A)).astype(str)  # A icerisindeki eleman sayisi kadarlik bir grup olustur.
grup_a = pd.DataFrame(grup_a)           # Bunu DataFrame'e donustur.
grup_a[:] = "A"                         # Grup icerisindeki tum elemanlari "A" yap.
A = pd.concat([A, grup_a], axis = 1)    # A'yi ve Grubu Yanyana Getir.

# Grup B
grup_b = np.arange(len(B)).astype(str)
grup_b = pd.DataFrame(grup_b)
grup_b[:] = "B"
B = pd.concat([B, grup_b], axis = 1)

# Tum Veri
AB = pd.concat([A,B])
AB.columns = ["Gelir", "Grup"]

print(AB.head())
print(AB.tail())

# Gorsellestirme
sns.boxplot(x = "Grup", y = "Gelir", data = AB)
plt.show()


# Verilerin rastgele mi yoksa doğru olduğu için mi elde edildiğini anlamak için varsayim kontrolü yapacağiz.


 # Varsayim Kontrolu
# normallik varsayimi:
#A_B = pd.concat([A,B], axis = 1)
#A_B.columns = ["A", "B"]
#print(shapiro(A_B.A))       # p-value = 0.7849036492977337 (H₀ Kabul edilir!)
#print(shapiro(A_B.B))       # p-value = 0.2762148565263921 (H₀ Kabul edilir!)


# varyans homojenligi varsayimi
# H₀: Varyanslar Homojendir.
# H₁: Varyanslar Homojen Degildir.


#print(stats.levene(A_B.A, A_B.B))   # p-value = 0.4089042823104799 -> (H₀ Kabul edilir!) (Varyanslar Homojendir.)


 # T Test Uygulamasi
#test_istatistigi, pvalue = stats.ttest_ind(A_B["A"], A_B["B"], equal_var = True)   #-> equal_var = True (varyans homojenligi saglaniyor)
#print(pvalue)   # p-value = 5.3036326801800985e-09 > 0.05 oldugu icin H₀ Hipotezi Reddediir.
#print("Test istatistigi = %.4f, p-value = %.4f" % (test_istatistigi, pvalue))


# Nonparametrik Bagimsiz iki Orneklem Testi
#print(stats.mannwhitneyu(A_B["A"], A_B["B"]))       # Hem Normallik varyansi hem de varyans homojenligi varsayimi Saglanmiyorsa Kullanilir.