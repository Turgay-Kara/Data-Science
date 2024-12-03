# Bir ilaç firmasının yeni geliştirdiği bir ilacın, kan basıncını düşürme etkisi olup olmadığını test etmek istiyoruz.
# ilaç etkili mi, etkisiz mi?

import numpy as np
from scipy import stats

# 30 hasta üzerinde ilacın etkisini test ettik ve elde ettiğimiz kan basıncı verileri şu şekilde:
values   = [118, 121, 119, 122, 117, 120, 123, 125, 116, 119, 
            124, 118, 122, 121, 120, 117, 126, 124, 121, 119, 
            115, 122, 123, 118, 120, 117, 125, 124, 119, 118]

orneklem_mean = np.mean(values)
orneklem_std = np.std(values, ddof=1)

mu_h0 = 120

n = len(values)

values_t, values_p = stats.ttest_1samp(values, mu_h0)
print("T Test Sonucu:", values_t)

if values_t < 0.05:
    print("0 Hipotezi Reddedildi!\nilaç etkisiz.")

if values_t >= 0.05:
    print("0 Hipotezi Kabul edili!\nilaç etkili.")