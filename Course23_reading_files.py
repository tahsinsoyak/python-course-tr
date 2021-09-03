#açmak için yol girebiliriz
#aynı klasördeyse isim yazabiliriz
#1. değer dosya ismi, 2. değer yapacağımızı işlem
# [w] write yazdırmak [r] read okumak
# [a] pen, veri eklebiliriz [r+] reading plus hem yazmak hem okumak

employee_file = open("employees-testfile.txt", "r") #verileri değişkende saklıyoruz

#okunabilir mi okunamaz mı
#yukarda open yaptığımızda w yapsaydık okuyamazdık
print(employee_file.readable())
#bütün verileri okuyacak
print(employee_file.read())
#sadece tek satırı okumak [dosya açıksa birdaha read yapamayız]
#ard arda yazarak bütün satırları okuyabiliriz
print(employee_file.readline())

#bütün verileri bir diziye atıyor
# [1] komutuyla 2. elemana erişebiliriz file.readlines()[1]
print(employee_file.readlines())

#her zaman açtığımızda dosyayı kapamamız gerekmektedir
employee_file.close()