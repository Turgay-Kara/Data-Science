# >> randint ile olusturulmus bir Zar ornegi: <<
import numpy as np

atis = 0
yazi = 0
tura = 0
print("\n")
while yazi < 100 and tura < 100:
    para = np.random.randint(0,2)
    if para == 0:
        print("Yazi Geldi!")
        yazi +=1
        atis +=1

    if para == 1:
        print("Tura Geldi!")
        tura +=1
        atis +=1

ortalama_yazi = (yazi / atis) * 100
ortalama_tura = (tura / atis) * 100

print("\nPara Toplam:", atis, "Kere Atildi!\n")
print("Yazi Gelme Ihtimali: %{:.1f} olarak belirlendi.".format(ortalama_yazi))
print("Tura Gelme Ihtimali: %{:.1f} olarak belirlendi.\n".format(ortalama_tura))
