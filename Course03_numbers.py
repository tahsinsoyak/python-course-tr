print(3/2)
print(3*5*(1*2))  
print(50%3*(20))
#direk parantez içerisinde işlem yapabiliyoruz

my_num =5
print(my_num) #değişken olarak yazdırıyoruz
print(str(my_num)+" years company history.") #sayiyi string degere dönüstürüyoruz [print içinde stringle yazmak için]***
print("------------------------")


#-- NUMBER FONKSİYONLAR --

my_num = -4
print(abs(my_num))  #absulate alarak mutlak degerini alıyoruz
print(pow(5,my_num))  #power üstünü aliyoruz yani 5 üzeri -4
print(max(4,6,7,9)) #max hangi numaranın büyük olduğunu bize geri döndürecek
print(min(4,6,7,9)) #min hangi numaranın küçük olduğunu bize geri döndürecek
print(round(5.9)) #round sayi yuvarlama fonksiyonu  [5 ve yukarısını yukarı yuvarlar]


#-- MATEMATİK KÜTÜPHANESİ --    [import en başta olmadığı için yukarda kullanamayız math kütüphanesini]
from math import *  
#math kütüphanesini import ediyoruz 
#[sağ tık yada F12 ile tanımlandığı yerde tüm fonksiyonları bulmak mümkün]
print(floor(3.7)) #floor taban, en düşük numarayı alıcak [ne olursa olsun aşşağıya yuvarlıcak]
print(ceil(3.7))  #ceil tavan, en yüksek numarayı alacak [ne olursa olsun yukarıya yuvarlıcak]
print(sqrt(36))  #sqrt squire root, kökünü alacak sayının

