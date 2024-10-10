"""

IS UYGULAMASI

"""

# Problem:
# Web sitemizde geçirilen ortalama süre gerçekten 170 saniye mi?

# Detaylar:
# Yazilimlardan elde edilen web sitesinde geçirilen ort. süreler var.
# Bu veriler incelendiğinde bir yönetici ya da çalişanimiz
# bu değerlerin böyle olmadiğina yönelik düşünceler taşiyor ve bu durumu test etmek istiyorlar.

import numpy as np
import pandas as pd
from scipy.stats import shapiro
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.stats.descriptivestats import sign_test

#Sitede Gecirilen Surenin Testi
olcumler = np.array([17, 160, 234, 149, 145, 107, 197, 75, 201, 225, 211, 119,
                    157, 145, 127, 244, 163, 114, 145,  65, 112, 185, 202, 146,
                    203, 224, 203, 114, 188, 156, 187, 154, 177, 95, 165, 50, 110,
                    216, 138, 151, 166, 135, 155, 84, 251, 173, 131, 207, 121, 120])

print(olcumler[0:10])

print(stats.describe(olcumler))     # ortalama, varyans vs. gosterir.



# varsayimlar
pd.DataFrame(olcumler).plot.hist()
plt.show()         # Histogram Grafigi

import pylab
stats.probplot(olcumler, dist="norm", plot=pylab)
pylab.show()        # qqplot Grafigi



# Shapiro-Wilks Testi
# H0: Ornek Dagilimi ile teorik normal dagilim arasinda istatistiksel olarak anlamli bir farklilik yoktur.
# H1: Ornek Dagilimi ile teorik normal dagilim arasinda istatistiksel olarak anlamli bir farklilik vardir.


print(shapiro(olcumler))     # (0.979631198133062), (0.7329899004671605)
                              #   test istatistigi      p value degeri

# p-value < 0.05 ise H0 Reddedilir!
# Dolayisiyla H0'i kabul edecegiz.

# Varsayim Saglandigi icin Hipotez Testine Gecebiliriz:

# Hipotez Testinin Uygulanmasi
print(stats.ttest_1samp(olcumler, popmean = 170))   # statistic=(-2.1753117985877966), pvalue=(0.034460415195071446)
# p-value < 0.05, H0 Reddedilir!    (az once varsayim sonucu kabul ettik.) (Varsayimda 0.05'ten kucuk ciksaydi hic hipotez testi yapmayacaktik.)

# Web sitemizde Gecirilen ortalama sure 170 Degildir!  (170'ten Kucuktur.)


# Nonparametrik Test (varsayimlar saglanmadiginda tercih edilir)
# varsayim saglanmiyor ise:

print(sign_test(olcumler, 170))     # (-7.0),       (0.06490864707227217)
                                    # test ist.,        p-value


# Tek Orneklem Oran Testi: Oransal bir ifade test edilmek istenildiginde kullanilir.
# Toplamis olunan orneklem > 30 ise bu testi gerceklestirebiliriz.