# TO-DO LIST

gorevler = []

while True:
    tercih = input("\nGörev Ekleme (A)\nGörev Çikartma (B)\nGörevleri Göster (G)\nÇikiş Yap (Q)\n\nTercih: ").upper()

    if tercih == "A":
        ekleme = input("Eklemek istediğiniz Görevi Giriniz: ").lower()
        if ekleme:
            gorevler.append(ekleme)
            print(f'"{ekleme}" görevi eklendi.')
        else:
            print("Boş bir görev giremezsiniz.")

    elif tercih == "B":
        cikartma = input("Çikartmak istediğiniz Görevi Giriniz: ").lower()
        if cikartma in gorevler:
            gorevler.remove(cikartma)
            print(f'"{cikartma}" görevi çikarildi.')
        else:
            print(f'"{cikartma}" listede yok.')

    elif tercih == "G":
        if gorevler:
            print("To-Do List: ", gorevler)
        else:
            print("Yapilacak görev yok.")

    elif tercih == "Q":
        print("Uygulamadan çikiliyor...")
        break

    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")