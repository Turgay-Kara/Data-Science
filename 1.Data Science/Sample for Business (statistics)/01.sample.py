"""

IS UYGULAMASI

"""

# Problem:
# CEO fiyat belirleme konusunda bilimsel bir dayanak ve esneklik isteniyor

# Detaylar:
# Satici, alici ve bir ürün var.
# Alicilara ürüne ne kadar ücret öderdiniz diye soruluyor
# Optimum fiyat bilimsel ve esnek olarak bulunmak isteniyor.


 # Fiyat Stratejisi Karar Destek
import numpy as np
fiyatlar = np.random.randint(10,110, 1000)
print(fiyatlar.mean())

import statsmodels.stats.api as sms
print(sms.DescrStatsW(fiyatlar).tconfint_mean())        #-> Guven Araligimiz (58,4 - 61.95) %95 Guvenilirlik ile 