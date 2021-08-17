#fonksiyon tanımlarken def yazmak zorundayız
#fonksiyon içindeki tüm kodlar alt satırda bir tab içindedir

def sayHi():
    print("Hello user")

print("Top")
#fonksiyonu çağırıyoruz
sayHi()
#top ve bottom fonksiyonun çağrılış zamanını belirtmek içindir
print("Bottom")


#veri girilen fonksiyon
def sayHi2(name,age):
    print("Hey "+name+", you are "+str(age))

sayHi2("Mike",34)