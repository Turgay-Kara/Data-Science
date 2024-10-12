"""

IS UYGULAMASI

"""

# Korelasyon Analizi: Degiskenler arasinda iliski, bu iliskinin yonu ve siddeti ile ilgi bilgiler saglar.

# Reklam Harcamalari arttikca, Urun satislari artar.  (Pozitif Korelasyon)
# Arac  Kilometresi  arttikca, Arac Fiyatlari azalir. (Negatif Korelasyon) 

# Varsayim Saglaniyorsa:  Pearson  Korelasyon Katsayisi
# Varsayim Saglanmiyorsa: Spearman Korelasyon Katsayisi


# Bahsis ile Odenen Hesap arasindaki iliski
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
df = tips.copy()

df["total_bill"] = df["total_bill"] - df["tip"]     # Toplam Tutara bahsis dahil oldugu icin bahsisi cikarttik.
print(df.head())

print(df.plot.scatter("tip", "total_bill"))
#plt.show()  # Hesap Tutari arttikca Bahsisin de arttigini Gozlemliyoruz.


# Varsayimlar
# Normallik varsayimi
from scipy.stats import shapiro

test_ist, pvalue = shapiro([df["tip"]])
print("Test istatistigi: %.4f, P-value: %.4f" % (test_ist, pvalue))     # p-value: 0.0000

test_ist2, pvalue2 = shapiro(df["total_bill"])
print("Test istatistigi: %.4f, P-value: %.4f" % (test_ist2, pvalue2))   # p-value: 0.0000

# p-value < 0.05 --> H0 Reddedilir. Anlamli bir farklilik Vardir.



# H0 Reddedilemez gibi islem yaparak Devam edecegiz.

# Korelasyon Katsayisi
print(df["tip"].corr(df["total_bill"]))
# 0.5766 (Pozitif yonlu, Orta siddetli bir Korelasyon)

print(df["tip"].corr(df["total_bill"], method = "spearman"))
# 0.5936 (Pozitif yonlu, Orta siddetli bir Korelasyon)


# Anlamlilik Kontrolu
from scipy.stats import pearsonr


kor_kats, pvalue = pearsonr(df["tip"], df["total_bill"])
print("Korelasyon Katsayisi: %.4f, P-value: %.4f" % (kor_kats, pvalue))     # kor_kats =  0.5937(orta siddetli), p-value = 0.0000
# Degiskenler arasinda anlamli bir Korelasyon Vardir.


# Nonparametrik Korelasyon Testi
from scipy.stats import spearmanr
kor_kats2, pvalue3 = spearmanr(df["tip"], df["total_bill"])
print("Korelasyon Katsayisi: %.4f, P-value: %.4f" % (kor_kats2, pvalue3))   # kor_kats2 = 0.5937(orta siddetli), p-value = 0.0000