"""
   DATA PREPROCESSING
   
"""

import pandas as pd
# Tüm sütunların görüntülenmesini sağla
pd.set_option('display.max_columns', None)

# Tüm satırların görüntülenmesini sağla
pd.set_option('display.max_rows', None)

# Geniş DataFrame'lerde satırların kırılmasını engelle
pd.set_option('display.expand_frame_repr', False)


# Veri Temizleme:
# Gürültülü veri (Noisy Data): Birbirleriyle çelişkili durumlar.
# Eksik Veri Analizi (Missing Data Analysis): Verideki Eksiklikler.
# Aykiri Gözlem Analizi (Outliner Analysis): Verideki Aykiriliklar.

# Veri Standardizasyonu:
# 0-1 Dönüşümü
# Z-Skoruna Dönüştürme
# Logaritmik Dönüşüm

# Veri İndirgeme:
# Gözlem sayisinin azaltilmasi
# Değişken sayisinin azaltilmasi

# Değişken Dönüşümleri:
# Sürekli değikenlerde dönüşümler
# Kategorik değişkenlerde dönüşümler


# Veride genel eğilimin oldukça dişina çikan gözlemlere Aykiri Gözlem denir.

# Eğer kurulacak olan Modellerin bir genellenebilirlik kaygisi varsa(olmali) veri setinde seyrek olan senaryolari çalişmanin dişinda birakmalisin.

# Eşik Değer = Ortalama + 1xStandart Sapma
# Eşik Değer = Ortalama + 2xStandart Sapma ...



  # Aykiri Gözlem Analizi
# Aykiri degerleri yakalamak:
import seaborn as sns
import matplotlib.pyplot as plt

#df = sns.load_dataset("diamonds")
#df = df.select_dtypes(include=["Float64", "Float32"])
#df = df.dropna()  # Eksik gözlemler silindi
#print(df.head())

#df_table = df["table"]
#print(df_table.head())
#sns.boxplot(x = df_table)
#plt.show()


# Eşik Değer Belirleme
#Q1 = df_table.quantile(0.25)  # %25
#Q3 = df_table.quantile(0.75)  # %75
#IQR = Q3-Q1                   # Eşik Değer
#print(Q1, Q3, IQR)

#alt_sinir = Q1 - 1.5*IQR      # 1.Çeyrek Değeri - 1.5*IQR   (alt sinir belirleme)
#ust_sinir = Q3 + 1.5*IQR      # 3.Çeyrek Değeri + 1.5*IQR   (üst sinir belirleme)
#print(alt_sinir, ust_sinir)


# Aykiri Değer Sorgulamasi
#aykirilik = (df_table < alt_sinir) | (df_table > ust_sinir)    # Alt sinirdan küçük, üst sinirdan büyük olan değerleri sorguladik.
#aykiri_tf_alt = (df_table < alt_sinir)
#aykiri_tf_ust = (df_table > ust_sinir)

#print(df_table[aykiri_tf])          # alt sinirin eksik gözlemleri
#print(df_table[aykiri_tf].index)    # aykiri gözlemlerin olduğu indexlere eriştik


# Aykiri Gözlemlerin Silinmesi
#import pandas as pd 
#df_table = pd.DataFrame(df_table)
#print(df_table.shape)                  # 53940 adet Gözlem

#clean_tf = df_table[~((df_table < alt_sinir) | (df_table > ust_sinir)).any(axis = 1)]     # ~ = Koşulu Sağlamayanlari(aykiri olmayanlari) almak için
#print(clean_tf.shape)   # 605 adet aykiri gözlem olduğunu gözlemledik


# Ortalama ile Doldurma
#df_table[aykiri_tf_alt] = df_table.mean()     # Aykiri Gözlemleri veri setinden silmek yerine  Ortalama Değerler ile değiştirdik.
#print(df_table[aykiri_tf_alt])


# Baskilama Yöntemi
# Aykiri Gözlemler; alt sinirda ise alt sinir degerine eşitlenir, üst sinirda ise üst sinir değerine eşitlenir.
#df_table[aykiri_tf_alt] = alt_sinir
#df_table[aykiri_tf_ust] = ust_sinir
#print(df_table[aykiri_tf_alt])
#print(df_table[aykiri_tf_ust])



# Çok Değişkenli Aykiri Gözlem Analizi
#import seaborn as sns
#diamonds = sns.load_dataset("diamonds")
#diamonds = diamonds.select_dtypes(include= ["float64", "int64"])
#df = diamonds.copy()
#df =  df.dropna()
#print(df.head())

#import numpy as np
#from sklearn.neighbors import LocalOutlierFactor
#import matplotlib.pyplot as plt

#clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)    # Komsuluk=20, Yogunluk=0.1
#print(clf.fit_predict(df))

#df_scores = clf.negative_outlier_factor_
#print(df_scores[0:10])

#print(np.sort(df_scores)[0:20])   # sort = siralama islemi

#print(np.sort(df_scores)[13])     # bu değeri eşik değer kabul edelim.

#esik_deger = np.sort(df_scores)[13]
#aykiri_tf = df_scores < esik_deger    # aykiri gözlemler


# Silme Yöntemi
#new_df = df[df_scores > esik_deger]   # aykiri olmayan değerlerle yeni df oluşturduk
#print(new_df)


# Baskilama Yöntemi
#baski_deger = df[df_scores == esik_deger]
#aykirilar = df[~aykiri_tf]

#res = aykirilar.to_records(index = False)
#res[:] = baski_deger.to_records(index = False)
#print(res)  # aykiri gözlemleri ortalama değerlerle doldurduk ama kalici olmadi.

# Kalici olmasi icin:
#import pandas as pd
#df[~aykiri_tf] = pd.DataFrame(res, index = df[~aykiri_tf].index)
#print(df[~aykiri_tf])


# Eksik Gözlem Analizi:
# Veri setindeki eksikliğin yapisal bir eksiklik olup olmadiğinin bilinmesi gerekir!
# NA her zaman esksiklik anlamina gelmez.

# Bilgi Kayiplari:
# Tümüyle Rastlantisal Kayip:
# Diğer değişkenlerden ya da yapisal bir problemden kayanaklanmayan tamamen rastgele oluşan gözlemler.

# Rastlantisal Kayip:
# Diğer değişkenlerde bağli olarak oluşabilen eksiklik türü

# Rastlantisal Olmayan Kayip:
# Göz ardi edilemeyecek olan ve yapisal problemler ile ortaya çikan eksiklik türü

# Rastsallik Nasil incelenir?
# Görsel Teknikler*, Bağimsiz iki örneklem T Testi, Korelasyon Testi, Little'nin MCAR Testi*



# Eksik Veri (hizli çözüm)
import numpy as  np
import pandas as pd

#V1 = np.array([1,3,6,np.nan, 7,1,np.nan,9,15])
#V2 = np.array([7,np.nan,5,8,12,np.nan,np.nan,2,3]) 
#V3 = np.array([np.nan,12,5,6,14,7,np.nan,2,31])
#df = pd.DataFrame({
#    "V1":V1,
#    "V2":V2,
#    "V3":V3})

#print(df)

#print(df.isnull().sum())        # Eksik Değer sayisi
#print(df.notnull().sum())       # Eksik olmayan Değer sayisi
#print(df.isnull().sum().sum())  # Toplam Eksik Değer

#print(df.isnull())              # True = nan degerler

#print(df[df.isnull().any(axis = 1)])    # En az 1 tane eksik gözlem varsa Tüm satiri getirecek / axis=1 (sütun bazinda)
#print(df[df.notnull().all(axis = 1)])   # Eksik değeri olmayan Satirlar

#print(df.dropna())                # Tüm Eksik Değerleri Siler (geçici olarak)
#print(df.dropna(inplace = True))  # Tüm Eksik Değerleri Siler (kalici olarak)

#df["V1"] = df["V1"].fillna(df["V1"].mean())   # Eksik Değerleri Ortalama ile Değiştir
#df["V2"] = df["V2"].fillna(0)                 # Eksik Değerleri 0 ile Değiştir.
#print(df)

#df = df.apply(lambda x: x.fillna(x.mean()), axis = 0)  # Veri setinin Tamamini değiştirir
#print(df)



# Eksik Veri Yapisinin Görselleştirilmesi
import missingno as msno
import matplotlib.pyplot as plt

#msno.bar(df)
#plt.show()       # Sol bar:yüzde, Sağ bar: tam gözlem sayisi

#msno.matrix(df)
#plt.show()       # Eksik ve Dolu verileri Görselleştirerek verir.


#import seaborn as sns
#df_pl = sns.load_dataset("planets")
#print(df.head())

#print(df.isnull().sum())
#msno.matrix(df_pl)
#plt.show()

#msno.heatmap(df_pl)
#plt.show()        # Heatmap ile Değişkenlerin arasindaki Korelasyonu rahatlikla belirledik.
# Planets veri setinde rassal bir eksikliğe sahip değildir. Dolayisiyla,
# Eksik değerlerin Silinmesi veya Doldurma işlemleri sakincali olabilir.



# Silme İşlemleri
#df = df.dropna(how = "all")            # 6.Satirin Tüm değerleri Eksik olduğu için tüm Satiri sildik.
#df = df.dropna(axis = 1)               # En az 1 tane eksik değere sahip olan Satiri sil.
#df["sil_beni"] = np.nan                # Tüm satirlari nan olan bir Sütun
#df = df.dropna(axis = 1, how ="all")   # Tüm satirlari nan olan bir Sütunu sildik.
#print(df)



# Değer Atama (sayisal değişkenlerde)
#print(df["V1"].fillna(0))                               # Eksik değerlere 0 atadik.
#print(df["V1"].fillna(df["V1"].mean()))                 # Eksik değerleri ortalama ile doldurduk.
#print(df.apply(lambda x: x.fillna(x.mean()), axis = 0)) # Tüm değişkenler için
#print(df.fillna(df.mean()[:]))                          # Ayni işlem
#print(df.fillna(df.mean()["V1":"V2"]))                  # V1 ve V2'yi ortalamalar ile,
#print(df["V3"].fillna(df["V3"].median()))               # V3'ü median ile doldurduk.



# Değer Atama (kategorik değişkenlerde)
"""
V1 = np.array([1,3,6,np.nan,7,1,np.nan,9,15])
V2 = np.array([7,np.nan,5,8,12,np.nan,np.nan,2,3])
V3 = np.array([np.nan,12,5,6,14,7,np.nan,2,31])
V4 = np.array(["IT","IT","IK","IK","IK","IK","IK","IT","IT"])

df = pd.DataFrame(
        {"maas" : V1,
         "V2" : V2,
         "V3" : V3,
        "departman" : V4}        
)
print(df)

print(df.groupby("departman")["maas"].mean())

print(df["maas"].fillna(df.groupby("departman")["maas"].transform("mean")))   # gruplara göre bölünüp hesaplanmiş olan ortalamalari boşluklara atadi.
"""



"""
import numpy as np
import pandas as pd
V1 = np.array([1,3,6,np.nan,7,1,np.nan,9,15])
V4 = np.array(["IT",np.nan,"IK","IK","IK","IK","IK","IT","IT"], dtype=object)

df = pd.DataFrame(
        {"maas" : V1,
        "departman" : V4}        
)
print(df)

print(df["departman"].fillna(df["departman"].mode()[0]))   # Departmandaki NaN değeri veri setinin Mod'u ile doldurduk.
print(df["departman"].ffill())                             # Eksik değeri bir önceki  değer ile doldurduk.
print(df["departman"].bfill())                             # Eksik değeri bir sonraki değer ile doldurduk.
"""



# Tahmine Dayali Değer Atama
# Doldurma işlemleri

#import seaborn as sns
#import missingno as msno
#df = sns.load_dataset('titanic')
#df = df.select_dtypes(include = ['float64', 'int64'])
#print(df.head())
#print(df.isnull().sum())

#import numpy as np
#import pandas as pd
#from ycimpute.imputer import knnimput
#var_names = list(df)
#n_df = np.array(df)
#print(n_df[0:10])

#df = knnimput.KNN(k = 4).complete(n_df)
#df = pd.DataFrame(df, columns = var_names)
#print(df.isnull().sum())



# Random Forest
#import seaborn as sns
#import missingno as msno
#df = sns.load_dataset('titanic')
#df = df.select_dtypes(include = ['float64', 'int64'])
#print(df.isnull().sum())

#var_names = list(df)
#n_df = np.array(df)
#from sklearn.impute import SimpleImputer
#n_dff = SimpleImputer(missing_values=np.nan, strategy="mean").fit(n_df).transform(n_df)
#print(n_dff)

#dff = pd.DataFrame(n_dff, columns= var_names)
#print(dff.isnull().sum())



# EM
#import seaborn as sns
#import missingno as msno
#df = sns.load_dataset('titanic')
#df = df.select_dtypes(include = ['float64', 'int64'])

#from ycimpute.imputer import EM
#var_names = list(df)
#n_df = np.array(df)

#dff = EM().complete(n_df)
#dff = pd.DataFrame(dff, columns = var_names)
#print(dff.isnull().sum())



# Değişken Standardizasyonu (Veri Standardizasyonu)
# Standartlaştirma: Veri setinin taşimiş olduğu bilgiyi aslini bozmadan belirli bir standarta getirir.
# Dönüştürme: Veri setinin taşimiş olduğu bilgiyi bazen bozar, bazen temsil şeklini değiştirir.
"""
import numpy as np
import pandas as pd
V1 = np.array([1,3,6,5,7])
V2 = np.array([7,7,5,8,12])
V3 = np.array([6,12,5,6,14])

df = pd.DataFrame(
    {"V1": V1,
     "V2": V2,
     "V3": V3})

df = df.astype(float)
print(df)


# Standardizasyon
from sklearn import preprocessing
print(preprocessing.scale(df))


# Normalizasyon (0-1 arasinda)
print(preprocessing.normalize(df))


# Min-Max Dönüşümü (verilen aralikta dönüşüm)
scaler = preprocessing.MinMaxScaler(feature_range = (10,20))
print(scaler.fit_transform(df))
"""



# Değişken Dönüşümleri









