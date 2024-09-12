# VSCode Goruntu Ayarlari
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)

"""
        EXPLORATORY DATA ANALYSIS
"""

  # Veriye ilk Bakis

import seaborn as sns
planets = sns.load_dataset("planets")

df = planets.copy()     #-> Ana veri setinin yapisini yedekledik.

#print(df.info())
#print(df.dtypes)

df.method = pd.Categorical(df.method)   #-> Method'u object'ten, category'ye donustur.
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







