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

df = sns.load_dataset("diamonds")
df = df.select_dtypes(include=["Float64", "Float32"])
df = df.dropna()  # Eksik gözlemler silindi
#print(df.head())

df_table = df["table"]
#print(df_table.head())
sns.boxplot(x = df_table)
#plt.show()


# Eşik Değer Belirleme
Q1 = df_table.quantile(0.25)  # %25
Q3 = df_table.quantile(0.75)  # %75
IQR = Q3-Q1                   # Eşik Değer
#print(Q1, Q3, IQR)

alt_sinir = Q1 - 1.5*IQR      # 1.Çeyrek Değeri - 1.5*IQR   (alt sinir belirleme)
ust_sinir = Q3 + 1.5*IQR      # 3.Çeyrek Değeri + 1.5*IQR   (üst sinir belirleme)
#print(alt_sinir, ust_sinir)


# Aykiri Değer Sorgulamasi
aykirilik = (df_table < alt_sinir) | (df_table > ust_sinir)    # Alt sinirdan küçük, üst sinirdan büyük olan değerleri sorguladik.
aykiri_tf_alt = (df_table < alt_sinir)
aykiri_tf_ust = (df_table > ust_sinir)

#print(df_table[aykiri_tf])          # alt sinirin eksik gözlemleri
#print(df_table[aykiri_tf].index)    # aykiri gözlemlerin olduğu indexlere eriştik


# Aykiri Gözlemlerin Silinmesi
import pandas as pd 
df_table = pd.DataFrame(df_table)
#print(df_table.shape)                  # 53940 adet Gözlem

clean_tf = df_table[~((df_table < alt_sinir) | (df_table > ust_sinir)).any(axis = 1)]     # ~ = Koşulu Sağlamayanlari(aykiri olmayanlari) almak için
#print(clean_tf.shape)   # 605 adet aykiri gözlem olduğunu gözlemledik


# Ortalama ile Doldurma
df_table[aykiri_tf_alt] = df_table.mean()     # Aykiri Gözlemleri veri setinden silmek yerine  Ortalama Değerler ile değiştirdik.
#print(df_table[aykiri_tf_alt])


# Baskilama Yöntemi
# Aykiri Gözlemler; alt sinirda ise alt sinir degerine eşitlenir, üst sinirda ise üst sinir değerine eşitlenir.
df_table[aykiri_tf_alt] = alt_sinir
df_table[aykiri_tf_ust] = ust_sinir
print(df_table[aykiri_tf_alt])
print(df_table[aykiri_tf_ust])