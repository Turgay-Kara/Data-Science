"""

IS UYGULAMASI

"""

# Problem:
# "Hemen Al" butonu Kirmizi mi, Yesil mi olsa daha fazla Click Rate alir?

# Detaylar:
# Yesil Buton: 1000 Goruntulenme, 300 Tiklama
# Kirmizi Buton: 1100 Goruntulenme, 250 Tiklama

# iki Orneklem Oran Testi: 2 oran arasinda karsilastirma yapmak icin Kullanilir. (AB Testi)

import numpy as np
from statsmodels.stats.proportion import proportions_ztest

basari_sayisi = np.array([300,250])
gozlem_sayisi = np.array([1000,1100])

print(proportions_ztest(count=basari_sayisi, nobs=gozlem_sayisi))   # p-value = 0.0001532 (H0 Red) (Kirmizi ve Yesil buton arasinda Oransal fark vardir.)

# Tiklama/Goruntuleme = Tıklama Oranini verecektir. -> Yesil(%30), Kirmizi(%22,7)