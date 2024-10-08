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


 # Fiyat Stratejisi Karar Destek
#import numpy as np
#fiyatlar = np.random.randint(10,110, 1000)
#print(fiyatlar.mean())

#import statsmodels.stats.api as sms
#print(sms.DescrStatsW(fiyatlar).tconfint_mean())        #-> Guven Araligimiz (58,4 - 61.95) %95 Guvenilirlik ile 



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



 # Binom Uygulama
#from scipy.stats import binom
#p = 0.01
#n = 100
#rv = binom(n, p)
#print(rv.pmf(1))    #-> Verilen bir Reklami goren 100 kisiden 1 kisinin aksiyon alma ihtimali.
#print(rv.pmf(5))
#print(rv.pmf(10))



 # Poisson Uygulama
#from scipy.stats import poisson
#lambda_ = 0.1       #-> Olaylarin ortalama gerceklesme orani
#rv = poisson(mu = lambda_)
#print(rv.pmf(k = 0))
#print(rv.pmf(k = 3))
#print(rv.pmf(k = 5))



 # Normal Dagilim Uygulama
#from scipy.stats import norm
#print(1-norm.cdf(90, 80, 5))                       #-> .cdf(hesaplanmak istenen deger, ortalama, standar sapma) #(90dan fazla olma olasiligi-> 0.022...)
#print(1-norm.cdf(70, 80, 5))
#print(norm.cdf(73, 80, 5))                         #-> 73'ten az olma olasiligi.
#print(norm.cdf(90, 80, 5) - norm.cdf(85, 80, 5))   #-> 85 ile 90 arasinda olma olasiligi.


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


"""
IS UYGULAMASI

"""
# Sitede Gecirilen Surenin Testi
#import numpy as np

#olcumler = np.array([17, 160, 234, 149, 145, 107, 197, 75, 201, 225, 211, 119,
                    #157, 145, 127, 244, 163, 114, 145,  65, 112, 185, 202, 146,
                    #203, 224, 203, 114, 188, 156, 187, 154, 177, 95, 165, 50, 110,
                    #216, 138, 151, 166, 135, 155, 84, 251, 173, 131, 207, 121, 120])

#print(olcumler[0:10])

#import scipy.stats as stats
#print(stats.describe(olcumler))     # ortalama, varyans vs. gosterir.



# varsayimlar
#import pandas as pd
#import matplotlib.pyplot as plt

#pd.DataFrame(olcumler).plot.hist()
#plt.show()         # Histogram Grafigi

#import pylab
#stats.probplot(olcumler, dist="norm", plot=pylab)
#pylab.show()        # qqplot Grafigi



# Shapiro-Wilks Testi
# H0: Ornek Dagilimi ile teorik normal dagilim arasinda istatistiksel olarak anlamli bir farklilik yoktur.
# H1: Ornek Dagilimi ile teorik normal dagilim arasinda istatistiksel olarak anlamli bir farklilik vardir.

#from scipy.stats import shapiro
#print(shapiro(olcumler))     # (0.979631198133062), (0.7329899004671605)
                              #   test istatistigi      p value degeri

# p-value < 0.05 ise H0 Reddedilir!
# Dolayisiyla H0'i kabul edecegiz.

# Varsayim Saglandigi icin Hipotez Testine Gecebiliriz:


# Hipotez Testinin Uygulanmasi
#print(stats.ttest_1samp(olcumler, popmean = 170))   # statistic=(-2.1753117985877966), pvalue=(0.034460415195071446)
# p-value < 0.05, H0 Reddedilir!    (az once varsayim sonucu kabul ettik.) (Varsayimda 0.05'ten kucuk ciksaydi hic hipotez testi yapmayacaktik.)

# Web sitemizde Gecirilen ortalama sure 170 Degildir!  (170'ten Kucuktur.)



# Nonparametrik Test (varsayimlar saglanmadiginda tercih edilir)
# varsayim saglanmiyor ise:
#import numpy as np
#from statsmodels.stats.descriptivestats import sign_test

#olcumler = np.array([17, 160, 234, 149, 145, 107, 197, 75, 201, 225, 211, 119,
                    #157, 145, 127, 244, 163, 114, 145,  65, 112, 185, 202, 146,
                    #203, 224, 203, 114, 188, 156, 187, 154, 177, 95, 165, 50, 110,
                    #216, 138, 151, 166, 135, 155, 84, 251, 173, 131, 207, 121, 120])

#print(sign_test(olcumler, 170))     # (-7.0),       (0.06490864707227217)
                                    # test ist.,        p-value


# Tek Orneklem Oran Testi: Oransal bir ifade test edilmek istenildiginde kullanilir.
# Toplamis olunan orneklem > 30 ise bu testi gerceklestirebiliriz.



# Donusum Orani Testi (detayli anlatim)
# > Ornegin bir reklami goren 100 kisiden 1'i donus yapiyorsa Donusum Orani: 0.01'dir. <

"""
 Problem: Verilen bir reklamda Donusum orani "yazilim" ile 0.125 donusum orani elde edilmistir.
 Fakat bu oran gelirlerle ortusmuyor.

 Detaylar: 500 kisi reklamlara tiklamis, 40 atnesi sitemize gelip alisveris yapmis.
 Ornek uzerinden elde edilen donusum orani: 0.08
"""

# H₀: P = 0.125
# H₁: P ≠ 0.125

#from statsmodels.stats.proportion import proportions_ztest
#count = 40      # tiklanma sayisi
#nobs = 500      # gozlem sayisi
#value = 0.125   # karsilastirilmak istenen oran

#print(proportions_ztest(count,nobs,value))  #-> -3.7090151628513017, 0.0002080669689845979)
                                                    # test ist.            p-value
# P-value < 0.05 oldugundan dolayi H₀ Reddediir.



# Bagimsiz iki Orneklem T Testi (AB Testi) (detayli anlatim)
# > iki grup ortalamasi arasinda karsilastirma yapmak amaciyla kullanilir. <

"""
 Problem: ML Modelinin Basari Testi:
 Bir ML Projesinin Urettigi tahminler neticesinde olusan gelir ile eski sistemin urettigi
 gelirler karsilastirilip anlamli bir farklilik olup olmadigi test edilmek isteniyor.

 Detaylar:
 Model Gelistirilmis ve Web sitesine entegre edilmis.
 Site Kullanicilari belirli bir kurala gore 2ye bolunmus olsun
 A grubu eski, B grubu yeni sisteme gore analiz edilecek.
 Gelir anlaminda anlamli bir is yapilip yapilmadigi test edilmek isteniyor.
"""

# veri setinin duzenlenmesi (en zor sekli ile)
#import numpy as np
#import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt

#A = pd.DataFrame([30,27,21,27,29,30,20,20,27,32,35,22,24,
                  #23,27,23,27,23,25,21,18,24,26,27,28,19,25])

#B = pd.DataFrame([37,39,31,31,34,38,30,36,29,28,38,28,37,
                  #37,30,32,31,31,27,32,33,33,33,31,32,33,26])

"""
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
"""

# Verilerin rastgele mi yoksa doğru olduğu için mi elde edildiğini anlamak için varsayım kontrolü yapacağız.


 # Varsayim Kontrolu
# normallik varsayimi:
#from scipy.stats import shapiro
#A_B = pd.concat([A,B], axis = 1)
#A_B.columns = ["A", "B"]
#print(shapiro(A_B.A))       # p-value = 0.7849036492977337 (H₀ Kabul edilir!)
#print(shapiro(A_B.B))       # p-value = 0.2762148565263921 (H₀ Kabul edilir!)


# varyans homojenligi varsayimi
# H₀: Varyanslar Homojendir.
# H₁: Varyanslar Homojen Degildir.

#import scipy.stats as stats
#print(stats.levene(A_B.A, A_B.B))   # p-value = 0.4089042823104799 -> (H₀ Kabul edilir!) (Varyanslar Homojendir.)



 # T Test Uygulamasi
#test_istatistigi, pvalue = stats.ttest_ind(A_B["A"], A_B["B"], equal_var = True)   #-> equal_var = True (varyans homojenligi saglaniyor)
#print(pvalue)   # p-value = 5.3036326801800985e-09 > 0.05 oldugu icin H₀ Hipotezi Reddediir.
#print("Test istatistigi = %.4f, p-value = %.4f" % (test_istatistigi, pvalue))


# Nonparametrik Bagimsiz iki Orneklem Testi
#import scipy.stats as stats
#print(stats.mannwhitneyu(A_B["A"], A_B["B"]))       # Hem Normallik varyansı hem de varyans homojenligi varsayimi Saglanmiyorsa Kullanilir.


"""
IS UYGULAMASI
"""
# Bagimli iki Orneklem T Testi
# Bagimli iki grup ortalamasi arasinda karsilastirma yapilmak istenildiginde kullanilir.

# Egitimden once ve sonra Sirket personellerinin performans olculerine iliskin degerler: 

import pandas as pd
import numpy as np

np1 = np.random.randint(100,141, size=40)
np2 = np.random.randint(120,161, size=40)

before = pd.DataFrame(np1)
after = pd.DataFrame(np2)

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
print("'Birlikte' Veri Seti: \n\n", together.head(), "\n")

import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(x = "Before-After", y = "Performans", data = together, palette = ["green", "orange"])
plt.show()

# After Performanslari gercekten de daha yuksek cikti. Ama,
# bu degerlerin tesadufen olusmadigini ispatlamak icin Varsayim Kontrollerini yapacagiz.