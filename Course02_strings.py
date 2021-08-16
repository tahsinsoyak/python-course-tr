print("Tahsin\nSoyak") 
#alt satira atlamak için \n => newline

print("Tahsin \"Suntheo\' Soyak")
#escape karekter olarak biliniyor
#yazıldıktan sonra ne gelirse gelsin tek karekter öylece basilacak demek.
#eğer tirnak isareti koymak istiyorsak bu sekilde koyuyoruz
#ters slash ve koyacağımız şeyi ardına koyuyoruz


phrase ="Tekrar"
#değiskene akdardik

print(phrase+" deneyiniz.")


print("-------------------------")

#-- STRİNG FONKSİYONLAR --
print(phrase.capitalize())
print(phrase.upper()) #büyük karekter yapıyor
print(phrase.lower()) #küçük karekter yapiyor
print(phrase.isupper()) #yüksek karekter mi? diye sorup boolean sonuç veriyor
print(phrase.split("ek")) #verdiğimiz stringten itibaren kesip ikiye bölüyor
print(len(phrase)) #kaç karekter olduğunu öğreniyoruz
print(phrase[0]) #verdiğimiz indexteki hafri söyleyecek
print(phrase.index("r")) #verdiğimiz stringin indexsini söyleyecek
#içinde olmayan bir karekter sorduğumuzda hata verir
print(phrase.replace("Tekrar","Kazandınız")) #kelime değisimi için kullanılan fonksiyon
#ilk kelime değişecek kelime, 2. ise ne olacağı

print(phrase.upper().isupper())
#arka arkaya fonksiyon kullanilaniliyor. ***
