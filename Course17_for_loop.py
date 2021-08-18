
#döngü yaratımı

#verdiğimiz değişkenin içindeki her letteri yazdırıyoruz
for letter in "Snake":
    print(letter)


#dizi ile ilgili kullanımı
friends = ["Jim","Karen","Kevin"]
for friend in friends:
    print(friend)

#aralıktaki indexleri yazdırmak
#range önceden tanımlı aralık fonksiyonu
#range(3,10) 3ten başlıyarak 10'a kadar [10 dahil değil]
for index in range(10): 
    print(index)

len(friends) #içindeki verilerin uzunluğu [3]

#friends dizisinin uzunluğu aralığında her birinin indexle yazdırmak
for index in range(len(friends)):
    print(friends[index])

#if ile kullanımı
for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")