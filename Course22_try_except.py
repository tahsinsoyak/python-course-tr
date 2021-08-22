
#ne olursa olsun yakalıyor
try:
    #veri alırken girilen verinin farklı türde olmasını engelleyebiliriz
    number = int(input("Enter a number: "))
    print(number)
except:
    #yakaladığımızda mesaj yazdırıyoruz
    print("Invalid Input")

#normalde sayıyı 0 a bölemeyiz
#belirlediğimiz hatayı arayabiliriz ona göre bir çıktı verebiliriz
try:
    value = 10/0
except ZeroDivisionError: #sıfıra bölme hatası
    print("Divided by zero")
except ValueError: #değer hatası
    print("Invalid input")
except BufferError as err: #hatayı yazdırabiliriz
    print(err)