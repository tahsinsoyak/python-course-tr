#bir veri yapısı (listeye benziyor)
#genellikle kordinatlarda kullanılıyor
#tuple'lar değiştirilemez eklenemez silinemez
#bir kez oluşturulduğunda öyle kalır
cordinates = (4,5)
#cordinates[1] = 10 'tuple' object does not support item assignment
#hatasi ile karşılaşırız ve değiştirilemez (listeden farkı)
#asla değişmiyecek bir değer için kullanılıyor
print(cordinates[1])

cordinates2 = [(2,3),(2,1),(8,6)]

print(cordinates2[2])
