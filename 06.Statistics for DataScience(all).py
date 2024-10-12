"""
        STATISTICS for DATA SCIENCE

"""

# Orneklem: 
# Bir toplulugun (evrenin) tamamini temsil eden, ondan secilen daha kucuk bir gruptur.

# Merkezi Limit Teoremi: 
# yeterince buyuk bir orneklem alindiginda, orneklem ortalamalarinin dagiliminin, 
# orneklem alinan dagilimin sekli ne olursa olsun, yaklasik olarak normal dagilima yaklasacagini ifade eder. 



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
# Bir veri setindeki degerlerin ortalamaya gore ne kadar dagildigini olcer.
# Dagilim ne kadar buyukse varyans da o kadar buyuk olur.


# Kovaryans:
# iki degiskenin birlikte nasil hareket ettigini gosterir.
# Eger iki degisken ayni yonde hareket ediyorsa pozitif kovaryans, ters yonde hareket ediyorsa negatif kovaryans vardir.


# Korelasyon, iki degisken arasindaki iliskinin yonunu ve gucunu gosteren bir olcudur. Iki degiskenin birlikte nasil degistigini anlamak icin kullanilir.

# Pozitif korelasyon: Bir degisken artarken digeri de artar.
# Negatif korelasyon: Bir degisken artarken digeri azalir.
# 0'a yakin korelasyon: İki degisken arasinda belirgin bir iliski yoktur.

# Korelasyon katsayisi, genellikle -1 ile +1 arasinda bir deger alir:
# +1: Tam pozitif iliski,
# -1: Tam negatif iliski,
# 0: Hicbir iliski yok.



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
#print(df[["tip", "total_bill"]].corr())        # 2 degisken arasindaki iliskiyi gosterir.



 # Guven Araligi
# Ana Kutle parametresinin tahmini degerini kapsayacak 2 sayidan olusan bir aralik.
# Yapilan tahminler ne kadar Guvenilir?


 # Guven Araligi Hesaplama: (guven.aralik.hesaplama.jpg)



 # Olasilik
# Kesikli Olasilik Dagilimlari: (0 veya 1)
# Bernoulli:    Basarili-Basarisiz seklinde 2 sonuclu olaylarda kullanilan Kesikli Olasilik Dagilimidir. (0 veya 1)
# Binom:        Bagimsiz n deneme sonucu k basarili olma olasiligi ile ilgili Kullanilan Dagilimdir.
# Poisson:      Belirli bir zaman araliginda belirli bir alanda nadiren rastlanan olaylarin olasiliklarini hesaplamak icin Kullanilir. (rotara dusen ucak sefer sayisi gibi...)


# Surekli Olasilik Dagilimlari: (0.1, 0.2, ...)
# Normal Dagilim:       Normal dagildigi bilinen surekli Rassal Degiskenlerin olasilik hesaplamasini yapmak icin Kullanilir.
# Uniform Dagilim:      
# Ustel Dagilim:        



# Bernoulli Uygulama
#from scipy.stats import bernoulli
#p = 0.6         # tura gelme olasiligi 0.6 dedik.
#rv = bernoulli(p)
#print(rv.pmf(k = 1))    # 0.6, k=0 iken yazi gelme olasiligi: 0.4



 # Buyuk Sayilar Yasasi

"""
import numpy as np
rng = np.random.RandomState(123)
for i in np.arange(1,21):
    deney_sayisi = 2**i
    yazi_turalar = rng.randint(0,2, size = deney_sayisi)
    yazi_olasiliklari = yazi_turalar.mean()
    print("Atis Sayisi:", deney_sayisi, "--", "Yazi Olasiligi:","%","%.2f" % (yazi_olasiliklari*100))
"""

 # Hipotez Testi: Bir tahmini test etmek icin kullanilan istatiksel bir tekniktir.

# p-Value
# p < 0.05  ise  h0 hipotezi Reddedildi.


"""
İstatistikte iki temel hipotez vardir:

Sifir Hipotezi (H₀): Arastirmada iddia edilen durumun olmadigini savunan varsayimdir. 
Genellikle, "degisiklik yok", "etki yok" veya "fark yok" anlamina gelir.
ornegin, bir ilac calismasinda sifir hipotezi, ilacin etkisiz oldugunu savunabilir.


Alternatif Hipotez (H₁): Sifir hipotezine karsi ileri surulen varsayimdir.
Bu, "degisiklik var", "etki var" veya "fark var" gibi sonuclari savunur.
Yani, arastirmanin asil iddiasini test etmek icin bu hipotez kullanilir.


Bir hipotezin dogrulugu test edilirken, sifir hipotezi baslangicta dogru kabul edilir ve analizler bu varsayimi sinamak icin yapilir.
Verilere dayali sonuclara gore sifir hipotezi reddedilebilir veya kabul edilebilir.
"""


 # Hipoez Testi Adimlari
# Adim 1: Hipotezlerin kurulmasi ve yonlerinin belirlenmesi.
# Adim 2: Anlamlilik duzeyinin ve tablo degerinin belirlenmesi.
# Adim 3: Test istatistiginin belirlenmesi ve hesaplanmasi.
# Adim 4: Hesaplanan Test istatistigi ile Alfa'ya karsilik gelen tablo degerinin karsilastirilmasi.
# Adim 5: Yorum

# Test istatistigi (Zh) > Tablo Degeri (Zt) ise H0 Red



# pvalue >= 0.05
# H0 Kabul (etki yok)

# pvalue < 0.05
# H1 Red (etki var)