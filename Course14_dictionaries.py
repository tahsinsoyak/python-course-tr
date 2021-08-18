#veri depolamamızı sağlıyor
#anahtralarla saklıyor ve anahtarı ile çağırıyoruz
#tıpkı bir sözlük gibi kelime anahtar tanımı ise value olacak

#süslü parentez içinde tanımlıyoruz
monthConversions = {
    # 1. anahtar [key] 2. ise veri [value]
    "Jan":"January",
    "Feb":"Febuary", #her bir key unique (eşsiz) olmalı
    "Mar":"March",
    "May":"May",
    6:"June", #anahtar string olmak zorunda değil
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}

#1. erişim yöntemi [anahtar girilerek]
print(monthConversions["Nov"])
#2. erişim yöntemi [get fonksiyonunu kullanıp anahtar girmek]
print(monthConversions.get("Dec"))


#olmayan değer girince "None" uyarısı alıyoruz
print(monthConversions.get("sds"))
#default değer ataması yaptık
print(monthConversions.get("sda","Not a valid Key"))


