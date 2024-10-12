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



  # Boxplot
# total_bill = yemegin toplam fiyati (bahsis ve vergi dahil)
# tip = bahsis
# sex = ucreti odeyen kisinin cinsiyeti (0:male, 1:female)
# smoker = grupta sigara icen var mi? (0:No, 1:Yes)
# day = gun (3:Thur, 4:Fri, 5:Sat)
# time = ne zaman? (0:Day, 1:Night)
# size = Grupta kac kisi var? 



"""
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
df = tips.copy()
#print(df.head())
#print(df.describe().T)

print(df["sex"].value_counts())
print(df["smoker"].value_counts())
print(df["day"].value_counts())
print(df["time"].value_counts())

sns.boxplot(x=df["total_bill"])   # Sutun Grafigi
plt.show()
"""


  # Caprazlamalar
#sns.boxplot(x = "day", y = "total_bill", data = df)   #-> x ekseninde gunleri, y ekseninde geliri goster.
#plt.show()                                            #-> En cok Gelir Pazar Gunu

#sns.boxplot(x = "time", y = "total_bill", data = df)  #-> Aksam Yemeginde Daha fazla gelir elde ediyor.
#plt.show()

#sns.boxplot(x = "size", y = "total_bill", data = df)
#plt.show()

#sns.boxplot(x = "day", y = "total_bill", hue = "sex", data = df)
#plt.show()


  # Violin Grafik -> Kutu & Yoğunluk Grafigi
#import seaborn as sns
#import matplotlib.pyplot as plt

#tips = sns.load_dataset("tips")
#df = tips.copy()
#print(df.head())

#sns.catplot(y = "total_bill", kind = "violin", data = df)
#plt.show()

  # Caprazlamalar
#sns.catplot(x = "day", y = "total_bill", hue = "sex", kind = "violin", palette = "Set2", data = df)
#plt.show()

  # Korelasyon Caprazlamalari
# Scatterplot

#sns.scatterplot(x = "total_bill", y = "tip", data = df)   # Harcanilan para arttikca Bagis artiyor.
#plt.show()

#sns.scatterplot(x = "total_bill", y = "tip", style = "day", hue = "day", data = df)   # Veri Grafigindeki sembol degisikligi
#plt.show()

#sns.scatterplot(x = "total_bill", y = "tip", hue = "size", size = "size" , data = df)  # hue ile renklendirdik, size ile boyut ayarladik
#plt.show()


  # Dogrusal iliskinin Gosterilmesi
#sns.lmplot(x = "total_bill", y = "tip", hue = "smoker",  data = df)
#plt.show()

#sns.lmplot(x = "total_bill", y = "tip", hue = "smoker", col = "time",  data = df)
#plt.show()

#sns.lmplot(x = "total_bill", y = "tip", hue = "smoker", col = "time", row = "sex", data = df) # Satirlara gore Cinsiyet, Sutunlara gore Time
#plt.show()


  # Scatterplot Matrisi
#import seaborn as sns
#import matplotlib.pyplot as plt
#iris = sns.load_dataset("iris") # Cicek Turleri
#df = iris.copy()
#print(iris.head())
#print(df.shape)

#sns.pairplot(df, hue = "species", markers= ["o", "s", "D"])
#plt.show()

#sns.pairplot(df, hue = "species", kind = "reg")
#plt.show()



  # Heatmap (isi haritasi)
#import seaborn as sns
#import matplotlib.pyplot as plt
#flight = sns.load_dataset("flights")
#df = flight.copy()
#print(df.head())
#print(df.shape)
#print(df["passengers"].describe())

#df = df.pivot(index="month", columns="year", values="passengers")
#sns.heatmap(df)   # Ucus sayilarini yila ve aylara oranla nasil arttigini gozlemledik.
#plt.show()

# Daha detayli:
#df = df.pivot(index = "month", columns= "year", values = "passengers")
#sns.heatmap(df, annot=True, fmt="d", linewidths= 0.5)     # cbar = False ile yandaki bar'i kaldirabiliriz.
#plt.show()



# Cizgi Grafik
#import seaborn as sns
#import matplotlib.pyplot as plt
#fmri = sns.load_dataset("fmri")
#df = fmri.copy()
#print(df.head())
#print(df.shape)

#print(df["timepoint"].describe())
#print(df["signal"].describe())

#print(df.groupby("timepoint")["signal"].count())
#print(df.groupby("timepoint")["signal"].describe())


  # Cizgi Grafigi ve Caprazlamalar
#sns.lineplot(x = "timepoint", y = "signal", data = df)  # her bir timepointin ortalamasini alarak cizgi grafigi olusturacak.
#plt.show()

#sns.lineplot(x = "timepoint", y = "signal", hue= "event", style= "event", data = df)  # hue argumani 3. bir boyut ekler. style="event" argumani eventin stilini degistirir.
#plt.show()

"""
sns.lineplot(x = "timepoint", 
             y = "signal", 
             hue= "event", 
             style= "event", 
             markers=True,
             dashes=False,
             data = df)
plt.show()
"""

"""
sns.lineplot(x = "timepoint", 
             y = "signal", 
             hue= "region", 
             style= "event",
             data = df)  # hue argumani 3. bir boyut ekler. style="event" argumani eventin stilini degistirir.
plt.show()
"""



  # Basit Zaman Serisi Grafigi
""" 
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("AAPL", start="2019-09-21", end="2024-09-21")    # start end araligindaki apple hisse senetlerinini verilerini cek.
print(df.head())
kapanis = df["Close"]
kapanis.plot()
plt.show()
"""