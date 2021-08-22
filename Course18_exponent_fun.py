print(2**3) #2^3 yapmak için bunu kullanabiliriz

#üssünü alma işlemini uzatarak yapıyoruz
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 3))

print(pow(2,3)) #bu özel tanımlanmış fonksiyonu kullanabiliriz