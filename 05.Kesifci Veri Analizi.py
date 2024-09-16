# VSCode Goruntu Ayarlari
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)

"""
        EXPLORATORY DATA ANALYSIS
"""

  # Veriye ilk Bakis

#import seaborn as sns
#planets = sns.load_dataset("planets")

#df = planets.copy()     #-> Ana veri setinin yapisini yedekledik.

#print(df.info())
#print(df.dtypes)

#df.method = pd.Categorical(df.method)   #-> Method'u object'ten, category'ye donustur.
#print(df.head())

#print(df.shape)                         #>> (1035, 6)
#print(df.columns)

#print(df.describe().T)                  #-> Kategorik degiskenleri disarida birakir. Sayisallari ele alir.
#>>
#                 count         mean           std          min         25%        50%       75%       max
#number          1035.0     1.785507      1.240976     1.000000     1.00000     1.0000     2.000       7.0   -> min gezegen sayisi 1, max gezegen sayisi 7
#orbital_period   992.0  2002.917596  26014.728304     0.090706     5.44254    39.9795   526.005  730000.0   -> Yorunge donemini ifade eden degerler.
#mass             513.0     2.638161      3.818617     0.003600     0.22900     1.2600     3.040      25.0   -> Kutle Degerlerini ifade eder.
#distance         808.0   264.069282    733.116493     1.350000    32.56000    55.2500   178.500    8500.0   -> Mesafe Degerlerini ifade eder.
#year            1035.0  2009.070531      3.972567  1989.000000  2007.00000  2010.0000  2012.000    2014.0   -> Yillari ifade eder.



  # Eksik Degerlerin incelenmesi
#import seaborn as sns
#planets = sns.load_dataset("planets")
#df = planets.copy()
#print(df.head())

#print(df.isnull().values.any())                                        #-> Eksik deger var mi?  >> True
#print(df.isnull().sum())                                               #-> Hangi degiskende kac tane eksik var?
#df['orbital_period'] = df['orbital_period'].fillna(0)                  #-> NaN degerleri 0 olarak degistirir.
#df["mass"] = df["mass"].fillna(df.mass.mean())                         #-> NaN degerleri 0 olarak degistirmek yerine Ortalamalarini yazdik.

#numeric_cols = df.select_dtypes(include='number')                      #-> Yalnizca sayisal sutunlari secin.
#df[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.mean())    #-> Tum veri setindeki Eksik degerleri sutunlarin ortalamasiyla doldurun
#print(df.isnull().sum())


#df2 = planets.copy()
#print(df2.isnull().sum())              #-> .copy() metotu kullandigimiz icin ayni veri setiyle baska islemler de yapabiliriz.



  # Kategorik Degisken Ozetleri
#import seaborn as sns
#planets = sns.load_dataset("planets")
#df = planets.copy()

#kat_df = df.select_dtypes(include = ["object"])
#print(kat_df.head())

#print(kat_df.method.unique())                   #-> method isimli kategorik degiskenin siniflarina erisim saglar.
#print(kat_df["method"].value_counts().count())  #-> method isimli kategorik degiskenin kac sinifi oldugunu gosterir.
#print(kat_df["method"].value_counts())          #-> method isimli kategorik degiskenin sinif frekanslarine erisim.


#import matplotlib.pyplot as plt
#ax = df["method"].value_counts().plot.barh()    #-> plot.barh() metotu veri setini Grafik seklinde gorsellestirerek verir.
#ax.set_title('Method Count')
#plt.show()



  # Surekli Degisken Ozetleri
#import seaborn as sns
#planets = sns.load_dataset("planets")
#df = planets.copy()
#print(df.head())

#df_num = df.select_dtypes(include = ["float64", "int64"])       #-> Surekli degisken secme islemi.
#print(df_num.head())
#print(df_num.describe().T)
#print(df_num["distance"].describe())


"""
import seaborn as sns
planets = sns.load_dataset("planets")
df = planets.copy()
df_num = df.select_dtypes(include = ["float64", "int64"])       #-> Surekli degisken secme islemi.

print("Ortalama: " + str(df_num["distance"].mean()))
print("Dolu Gozlem Sayisi: " + str(df_num["distance"].count()))
print("Maksimum Deger: " + str(df_num["distance"].max()))
print("Minimum Deger: " + str(df_num["distance"].min()))
print("Medyan: " + str(df_num["distance"].median()))
print("Standart Sapma: " + str(df_num["distance"].std()))
"""


  # Barplot
#import seaborn as sns
#diamonds = sns.load_dataset("diamonds")
#df = diamonds.copy()
#print(df.head())
#print(df.describe().T)

#print(df["price"].mean())
#print(df["color"].value_counts())
#print(df["cut"].head())


#ordinal tanimlama
#import pandas as pd
#from pandas.api.types import CategoricalDtype
#df.cut = df.cut.astype(CategoricalDtype(ordered = True))    #-> cut'in type'ini Kategorik Degiskene donustur.
#print(df.cut.dtypes)                                        #-> cut = category
#print(df.cut.head(1))                                       #-> ['Ideal' < 'Premium' < 'Very Good' < 'Good' < 'Fair'] >> Siralama islemimiz bozuldu. >> (1)


#cut_categories = ["Fair","Good","Very Good","Premium","Ideal"]  # >> (2)
#df.cut = df.cut.astype(CategoricalDtype(categories = cut_categories, ordered = True)) # (3) >> sorunu cozduk.
#print(df.cut.head(1))


  # Pandas ile Sutun Grafigi olusturma
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas.api.types import CategoricalDtype

diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()
df.cut = df.cut.astype(CategoricalDtype(ordered = True))
cut_categories = ["Fair","Good","Very Good","Premium","Ideal"]
df.cut = df.cut.astype(CategoricalDtype(categories = cut_categories, ordered = True))

(df["cut"]
 .value_counts()
 .plot.barh()
 .set_title("Cut Degiskenlerinin Sinif Frekanslari"));
print(plt.show())
"""



  # Sutun Grafik Ornegi:
"""
import pandas as pd
import matplotlib.pyplot as plt

# 1. Veriyi olustur
data = {
    "deger": ["Fair","Good","Very Good","Premium","Ideal"],
    "ucret(₺)": [500, 900, 1500, 3000, 6000]
}

# 2. DataFrame'e donustur
df = pd.DataFrame(data)

# 3. Sutun grafigi olustur
df.plot(kind='bar', x='deger', y='ucret(₺)', color='skyblue')

# Grafigi guzellestirme
plt.title("Diamond Prices")
plt.xlabel("Zaman")
plt.ylabel("Fiyat")
plt.xticks(rotation=0)  # X eksenindeki seanslarinn dikey yazilmasini engeller
plt.tight_layout()  # Grafigi duzgun yerlestirir

# 4. Grafigi goster
plt.show()
"""



  # Seaborn ile Sutun Grafigi olusturma
""" 
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import CategoricalDtype

diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()
df.cut = df.cut.astype(CategoricalDtype(ordered = True))
cut_categories = ["Fair","Good","Very Good","Premium","Ideal"]
df['cut'] = df['cut'].astype(CategoricalDtype(categories=cut_categories, ordered=True))

sns.countplot(x="cut", data=df, palette="muted")
plt.title("Cut Categories Count")
plt.show()
"""



  # Caprazlama
"""
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import CategoricalDtype

diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()
df.cut = df.cut.astype(CategoricalDtype(ordered = True))
cut_categories = ["Fair","Good","Very Good","Premium","Ideal"]
df['cut'] = df['cut'].astype(CategoricalDtype(categories=cut_categories, ordered=True))

sns.catplot(x= "cut", y= "price", data = df, kind="strip", palette="viridis")
plt.title("Cut Types vs Price")
plt.show()
"""



  # Daha Derinlere in:
"""
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import CategoricalDtype

diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()
df.cut = df.cut.astype(CategoricalDtype(ordered = True))
cut_categories = ["Fair","Good","Very Good","Premium","Ideal"]
df['cut'] = df['cut'].astype(CategoricalDtype(categories=cut_categories, ordered=True))
sns.barplot(x="cut", y="price", hue="color", data=df, palette="Set2") 
plt.show()

print(df.groupby(["cut", "color"], observed= False)["price"].mean())  #-> Gruplayarak Grafiksiz bir sekilde gosterecektir.
"""



# Histogram ve Yogunluk Grafigi
#import matplotlib.pyplot as plt
#import seaborn as sns
#diamodns = sns.load_dataset("diamonds")
#df = diamodns.copy()
#print(df.head())

#sns.displot(df.price, bins = 25, kde = False)   #-> Bins degeri arttiginda daha cok sutun olur yani daha detayli bir sunum verir.
#plt.show()

#sns.displot(df.price, kde = True)               #-> kde = True komutu ile ayni zamanda yogunluk grafigini de gosterebiliyoruz.
#plt.show()

#sns.histplot(df.price)                          #-> Sadece histogrami gosterir
#plt.show()       

#sns.kdeplot(df.price, fill=True)               #-> Sadece yogunluk grafigini gosterir.
#plt.show()



  # Histogram ve Yogunluk Caprazlamalari
"""  
import matplotlib.pyplot as plt
import seaborn as sns
diamodns = sns.load_dataset("diamonds")
df = diamodns.copy()

print(df.head())

(sns.FacetGrid(df,
               hue = "cut",
               height = 5,
               xlim = (0,10000))
.map(sns.kdeplot, "price", fill = True)
.add_legend()
)
plt.show()
"""



"""
import matplotlib.pyplot as plt
import seaborn as sns
diamodns = sns.load_dataset("diamonds")
df = diamodns.copy()
sns.catplot(x = "cut", y = "price", hue = "color", kind = "point", data = df)
plt.show()
"""