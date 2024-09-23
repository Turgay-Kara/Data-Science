"""
        STATISTICS for DATA SCIENCE
"""

# Orneklem: 
# Bir topluluğun (evrenin) tamamini temsil eden, ondan seçilen daha kuçuk bir gruptur.

# Merkezi Limit Teoremi: 
# yeterince buyuk bir orneklem alindiğinda, orneklem ortalamalarinin dağiliminin, 
# orneklem alinan dağilimin sekli ne olursa olsun, yaklasik olarak normal dağilima yaklasacağini ifade eder. 



 # Ornek Teorisi
#import numpy as np
#populasyon = np.random.randint(0, 80, 10000)    # 0-80 yas arasi 10k kisi
#print(populasyon[0:10])


 # Orneklem Cekimi
#np.random.seed(10)      # Yapilacak islemlerin her tekrarda ayni sonuclari getirmeyi garanti altina alir.
#orneklem = np.random.choice(a = populasyon, size=100)   # Populasyon icerisinden rastgele 100 tane gozlem cek.

#print(orneklem.mean())
#print(populasyon.mean())



 # Betimsel Istatistikler

# Varyans:
# Bir veri setindeki değerlerin ortalamaya göre ne kadar dağıldığını ölçer.
# Dağılım ne kadar büyükse varyans da o kadar büyük olur.


# Kovaryans:
# iki değişkenin birlikte nasıl hareket ettiğini gösterir.
# Eğer iki değişken aynı yönde hareket ediyorsa pozitif kovaryans, ters yönde hareket ediyorsa negatif kovaryans vardır.


# Korelasyon, iki değişken arasındaki ilişkinin yönünü ve gücünü gösteren bir ölçüdür. Iki değişkenin birlikte nasıl değiştiğini anlamak için kullanılır.

# Pozitif korelasyon: Bir değişken artarken diğeri de artar.
# Negatif korelasyon: Bir değişken artarken diğeri azalır.
# 0'a yakın korelasyon: İki değişken arasında belirgin bir ilişki yoktur.

# Korelasyon katsayısı, genellikle -1 ile +1 arasında bir değer alır:
# +1: Tam pozitif ilişki,
# -1: Tam negatif ilişki,
# 0: Hiçbir ilişki yok.



# Betimsel Istatistikler Uygulama
#import seaborn as sns
#tips = sns.load_dataset("tips")
#df = tips.copy()
#print(df.head())

"""
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
"""

#import researchpy as rp
#print(df.describe().T)                                          # ayni islem
#print(rp.summary_cont(df[["total_bill", "tip", "size"]]))       # farkli metotla

#print(rp.summary_cat(df[["sex", "smoker", "day", "time"]]))     # Ekstra olarak Yuzdelik de verecektir.


# Kovaryans
#print(df[["tip", "total_bill"]].cov())         # 2 Degisken arasindaki degisimi ifade eden bir istatistik.

# Korelasyon
#print(df[["tip", "total_bill"]].corr())        # 2 değişken arasındaki ilişkiyi gösterir.



 # Guven Araligi







