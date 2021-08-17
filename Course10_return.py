#fonksiyonlardan geri dönüşte veri almak için
#return çağrısından sonra hiçbir kod çalışmaz
#return break yapıyor fonksiyona

def cube(num):
    num*num*num

print(cube(3)) #bu şekilde çağırdığımızda none yazıyor

def square(num):
    return num*num

print(square(2)) #şimdi return olduğu için doğru cevabı alacağız

result = square(4) #atama yaptık
print(result)
