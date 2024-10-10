"""

IS UYGULAMASI

"""

# Problem:
# Bir yazilim ile bir mecrada reklam verilmiş ve bu reklama ilişkin yazilim tarafindan 0.125 dönüşüm orani elde edildiği ifade edilmiş.
# Fakat bu durum kontrol edilmek isteniyor. Çünkü bu yüksek bir oran ve gelirler incelendiğinde örtüşmüyor.

# Detaylar:
# 500 kişi dis mecrada reklamlara tiklamiş, 40 tanesi sitemize gelip alişveriş yapmiş.
# Örnek üzerinden elde edilen dönüşüm orani: 40/500 = 0,08


# H₀: P = 0.125
# H₁: P ≠ 0.125


from statsmodels.stats.proportion import proportions_ztest
count = 40      # tiklanma sayisi
nobs = 500      # gozlem sayisi
value = 0.125   # karsilastirilmak istenen oran

print(proportions_ztest(count,nobs,value))  #-> -3.7090151628513017, 0.0002080669689845979)
                                                    # test ist.            p-value
                                                    
# P-value < 0.05 oldugundan dolayi H₀ Reddediir.