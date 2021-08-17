
#liste yaratmak için köşeli parentezle birkaç değer ekliyoruz
friends = ["Ali","Veli","Kevin","Jim"]
#string, number, boolean ekliyebiliriz.
myself = ["Tahsin",20, 68.2,'E',True]

print(friends[2]) #Erisecegimiz verinin index degerini giriyoruz
print(friends[-1]) # - deger verirsek arkadan geliyor
print(friends[1:]) # iki nokta ile indexten sonrasini yazdiracak
print(friends[1:2]) #ikinci indexten sonrakileri alma dedik  [aralığı aldık]

friends[1] = "Tahsin" # 1. indexteki degeri güncelledik
print(friends[1])

#-- LIST FONKSİYONLARI --
lucky_numbers = [1,6,8,9,24,71,22,2]
friends.extend(lucky_numbers) #extends listeyi baska bir liste ekliyerek genisletiyor
friends.append("Creed") #append listeye eleman eklememizi sagliyor
friends.insert(1,"Suntheo") #insert index degeri vererek ekliyoruz ve listeyi genisletiyoruz 
#[geri kalanlarin indexi iteleniyor sona doğru]
friends.remove("Jim") #remove girilen elemani listeden çıkarıyor
friends.clear() #clear listeyi temizliyor

friends = ["Ali","Veli","Kevin","Jim","Kevin","Kevin"] #listeyi yenileyelim.

friends.pop() #pop son elemani dısarı atıyor
print(friends.index("Jim")) #index verilen ismin index degerini veriyor
print(friends.count("Kevin")) #count verilen degerin listede kaç defa geçtigini  söylüyor
friends.sort() #sort alfabetik olarak sıralıyor
lucky_numbers.sort()
lucky_numbers.reverse() #reverse listeyi ters çeviriyor
#[sort yaptıktan sonra yapınca büyükten küçüğe sıralayacak]
print(friends)
print(lucky_numbers)

friends2 = friends.copy()  #copy listeyi baska bir listeye kopyalıyor.
