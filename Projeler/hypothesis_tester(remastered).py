import pandas as pd
from scipy.stats import shapiro
import scipy.stats as stats

# Eğitim öncesi ve sonrasi performans verileri (örnek)

before = pd.DataFrame([123, 119, 119, 116, 123, 123, 121, 120, 117, 118, 121, 121, 123, 119,
                       121, 118, 124, 121, 125, 115, 115, 119, 118, 121, 117, 117, 120, 120,
                       121, 117, 118, 117, 123, 118, 124, 121, 115, 118, 125, 115], columns=['BEFORE'])

after = pd.DataFrame([118, 127, 122, 132, 129, 123, 129, 132, 128, 130, 128, 138, 140, 130,
                      134, 134, 124, 140, 134, 129, 129, 138, 134, 124, 122, 126, 133, 127,
                      130, 130, 130, 132, 117, 130, 125, 129, 133, 120, 127, 123], columns=['AFTER'])

# Verileri birleştirme
mix = pd.concat([before, after], axis=1)

# Shapiro-Wilk testinin uygulanmasi
test_ist, pvalue = shapiro(mix.BEFORE)
test_ist2, pvalue2 = shapiro(mix.AFTER)

# Normal dağilim kontrolü
if pvalue >= 0.05:
    print("BEFORE grubunun normal dağilim varsayimi kabul edilmektedir (p-value: {:.3f}).".format(pvalue))
else:
    print("BEFORE grubunun normal dağilim varsayimi reddedilmiştir (p-value: {:.3f}).".format(pvalue))

if pvalue2 >= 0.05:
    print("AFTER grubunun normal dağilim varsayimi kabul edilmektedir (p-value: {:.3f}).\n".format(pvalue2))
else:
    print("AFTER grubunun normal dağilim varsayimi reddedilmiştir (p-value: {:.3f}).\n".format(pvalue2))

# Devam eden test kodlari...


# Levene Testi uygulanmasi
if pvalue >= 0.05:
    print("Normal dağilim varsayimi sağlandiği için Levene Testi uygulanacaktir...")
    ttest_ist, ttest_pvalue = stats.levene(mix.BEFORE, mix.AFTER)
    
    if ttest_pvalue >= 0.05:
        print("Levene Testi sonuçlarina göre varyanslar arasinda anlamli bir fark yoktur (p-value: {:.3f}).".format(ttest_pvalue))
        print("Her iki grubun da normal dağilim varsayimini sağladiği için Shapiro-Wilk testi uygulanacaktir...\n")
        
        test_ist3, pvalue3 = shapiro(mix.BEFORE)    
        test_ist4, pvalue4 = shapiro(mix.AFTER)
        
        if pvalue3 >= 0.05:
            print("BEFORE grubunun normal dağilim varsayimi kabul edilmektedir (p-value: {:.3f}).".format(pvalue3))
            print("Anlamli bir fark yoktur.")
        else:
            print("BEFORE grubunun normal dağilim varsayimi reddedilmiştir (p-value: {:.3f}).".format(pvalue3))
            print("Anlamli fark vardir!")

        if pvalue4 >= 0.05:
            print("AFTER grubunun normal dağilim varsayimi kabul edilmektedir (p-value: {:.3f}).".format(pvalue4))
        else:
            print("AFTER grubunun normal dağilim varsayimi reddedilmiştir (p-value: {:.3f}).".format(pvalue4))

    else:
        print("Levene Testi sonuçlarina göre varyanslar arasinda anlamli bir fark vardir (p-value: {:.3f}).".format(ttest_pvalue))
        print("Bu durumda T-Testi uygulanacaktir.\n")
        
else:
    print("Anlamli bir fark olduğu tespit edilmiştir. T-Testi uygulanacaktir...")
    ttest_ist, ttest_pvalue = stats.ttest_rel(mix.BEFORE, mix.AFTER)
    
    if ttest_pvalue >= 0.05:
        print("T-Testi sonuçlarina göre anlamli bir fark yoktur (p-value: {:.3f}).".format(ttest_pvalue))
    else:
        print("T-Testi sonuçlarina göre anlamli bir fark vardir (p-value: {:.3f}).".format(ttest_pvalue))    

# Nonparametrik testin uygulanmasi
if ttest_pvalue < 0.05 and pvalue2 < 0.05:
    print("Normal dağilim varsayimlari sağlanmadiği için Nonparametrik T-Testi (Wilcoxon testi) uygulanacaktir...")
    nont_test, nonp_value = stats.wilcoxon(mix.BEFORE, mix.AFTER)
    
    if nonp_value >= 0.05:
        print("Wilcoxon testi sonuçlarina göre anlamli bir fark yoktur (p-value: {:.3f}).".format(nonp_value))
    else:
        print("Wilcoxon testi sonuçlarina göre anlamli bir fark vardir (p-value: {:.3f}).".format(nonp_value))
else:
    print("Nonparametrik T-Testi (Wilcoxon testi) uygulanamamaktadir çünkü normal dağilim varsayimlari sağlanmamaktadir.")

print()  # Boş satir eklemek için

# Eğitim programinin etkinliği
print("--- Eğitim Programinin Etkisi ---")
if ttest_pvalue < 0.05:
    print("Eğitim programi, çalişanlarin performansinda anlamli bir iyileşme sağlamiştir.")
else:
    print("Eğitim programi, çalişanlarin performansinda anlamli bir iyileşme sağlamamiştir.")
