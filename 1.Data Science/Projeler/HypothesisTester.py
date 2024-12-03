#_HypothesisTester_

#Sifir Hipotezi (H₀): Arastirmada iddia edilen durumun olmadigini savunan varsayimdir. 
#Alternatif Hipotez (H₁): Sifir hipotezine karsi ileri surulen varsayimdir.

#import islemleri
import numpy as np
from scipy.stats import shapiro
import scipy.stats as stats
import matplotlib.pyplot as plt

# Data Array'inin icine Verilerinizi Giriniz!
data = np.array([17, 160, 234, 149, 145, 107, 197, 75, 201, 225, 211, 119,
                157, 145, 127, 244, 163, 114, 145,  65, 112, 185, 202, 146,
                203, 224, 203, 114, 188, 156, 187, 154, 177, 95, 165, 50, 110,
                216, 138, 151, 166, 135, 155, 84, 251, 173, 131, 207, 121, 120])

print("\nUygulanabilir Testler:\nNormality (1)\tT-Test (2)")
while True:
    try:
        tercih = int(input("\nHangi Testi Uygulamak istiyorsunuz: (1/2): "))
        if tercih in [1, 2]:
            break
        else:
            print("Lutfen 1 veya 2 degerini Giriniz.")
    except ValueError:
        print("Lutfen Gecerli bir Sayi Giriniz.")

while True:
    if tercih == 1:
        print("Shapiro-Wilk Testi Gerceklestiriliyor...")
        result = shapiro(data)
        p_value = result.pvalue
        print(f"\nShapiro-Wilk Test Sonucu: {result}")
        print(f"p-value: {p_value}\n")

        if p_value < 0.05:
            print("p-value degeri < 0.05 oldugu icin, H₀ Hipotezi Reddedilir!")

        if p_value >= 0.05:
            print("p-value degeri >= 0.05 oldugu icin, H₀ Hipotezi Kabul Edilir!\nDagiliminiz Normal oldugu icin T-Test yapabilirsiniz.")
            tercih2 = input("\nT-Testine Gecmek istiyor musunuz? (y/n): ").upper()
            
            if tercih2 == "N":
                print("Test Gecisini Reddettiniz!\nProgram Sonlaniyor...")
                break

            if tercih2 == "Y":
                print("Test Gecisini Kabul Ettiniz!")
                tercih = 2
                continue

    if tercih == 2:
        print("\nT Testine Gecis Yaptiniz.")
        print(f"Veri Setinizin Ortalamasi: {data.mean()}")

        pop_mean = float(input("\nKarsilastirmak istediginiz Populasyon Ortalamasini Giriniz: "))
        t_statistic, pvalue = stats.ttest_1samp(data, popmean = pop_mean)

        print(f"\nVeri Setinizin T Test istatistigi: {t_statistic}")
        print(f"Veri Setinizin p-value Degeri: {pvalue}")

        if pvalue < 0.05:
            print("\nH₀ Hipotezi Reddedilir!\nVeri Setiniz Normal Dagilima Uygun Degil!\n")
            break
        if pvalue >= 0.05:
            print("\nH₀ Hipotezi Kabul Edilir!\nVeri Setiniz tamamen Normal Dagiliyor!\n")
            break

tercih3 = input("Veri Setinizin grafigini goruntulemek ister misiniz? (y/n): ").upper()
if tercih3 == "N":
    print("Program Sonlaniyor...")

if tercih3 == "Y":
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1)  # 1 satır, 3 sütun, 1. grafik
    plt.hist(data, bins=10, color='blue', alpha=0.7)

    plt.title('Histogram')
    plt.xlabel('Değerler')
    plt.ylabel('Frekans')

    plt.tight_layout()
    plt.show()