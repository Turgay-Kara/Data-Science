import pandas as pd
from scipy.stats import shapiro, levene, ttest_rel, wilcoxon
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
test_ist, pvalue_before = shapiro(mix.BEFORE)
test_ist2, pvalue_after = shapiro(mix.AFTER)

# Normal dağilim kontrolü
print("Shapiro-Wilks Testi uygulaniyor...")
if pvalue_before >= 0.05:
    print("BEFORE grubu Normal Dagilmaktadir. (p-value: {:.3f})".format(pvalue_before))
else:
    print("BEFORE grubu Normal Dagilmamaktadir. (p-value: {:.3f})".format(pvalue_before))

if pvalue_after >= 0.05:
    print("AFTER grubu Normal Dagilmaktadir. (p-value: {:.3f})".format(pvalue_after))
else:
    print("AFTER grubu Normal Dagilmamaktadir. (p-value: {:.3f})".format(pvalue_after))

# Parametrik veya nonparametrik testin seçimi
if pvalue_before >= 0.05 and pvalue_after >= 0.05:
    # Normal dağılım varsayımı sağlanıyorsa Levene testi
    print("\nLevene Testi uygulanmasi...")
    levene_stat, levene_pvalue = levene(mix.BEFORE, mix.AFTER)
    
    if levene_pvalue >= 0.05:
        # Varyanslar eşitse bağımlı T-Testi
        print("Varyanslar eşit. T-Testi uygulaniyor...")
        ttest_stat, ttest_pvalue = ttest_rel(mix.BEFORE, mix.AFTER)
        
        if ttest_pvalue >= 0.05:
            print("T-Testine göre anlamli bir fark Yoktur. (p-value: {:.3f})".format(ttest_pvalue))
        else:
            print("T-Testine göre anlamli bir fark Vardir. (p-value: {:.3f})".format(ttest_pvalue))
    else:
        print("Varyanslar eşit değil, Nonparametrik test uygulaniyor...")
        nont_test, nonp_value = wilcoxon(mix.BEFORE, mix.AFTER)
        
        if nonp_value >= 0.05:
            print("Wilcoxon testine göre anlamli bir fark Yoktur. (p-value: {:.3f})".format(nonp_value))
        else:
            print("Wilcoxon testine göre anlamli bir fark Vardir. (p-value: {:.3f})".format(nonp_value))
else:
    # Normal dağılım sağlanmadığında Wilcoxon testi
    print("Normal dağilim sağlanmadiği için Wilcoxon testi uygulaniyor...")
    nont_test, nonp_value = wilcoxon(mix.BEFORE, mix.AFTER)
    
    if nonp_value >= 0.05:
        print("Wilcoxon testine göre anlamli bir fark Yoktur. (p-value: {:.3f})".format(nonp_value))
    else:
        print("Wilcoxon testine göre anlamli bir fark Vardir. (p-value: {:.3f})".format(nonp_value))

nont_test, nonp_value = wilcoxon(mix.BEFORE, mix.AFTER)

# Eğitim programının etkinliği
print("\n--- Eğitim Programinin Etkisi ---")
if nonp_value < 0.05:
    print("Eğitim programi, çalişanlarin performansinda anlamli bir iyileşme sağlamiştir.")
else:
    print("Eğitim programi, çalişanlarin performansinda anlamli bir iyileşme sağlamamiştir.")