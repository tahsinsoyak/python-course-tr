#karşılaştırma ifi yapıyoruz
#hangi sayı büyük fonksiyonu
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else:
        return num3

print(max_num(3,56,5))


#string karşılaştırmasıda yapabiliriz
def isDog(string1):
    if "dog" == string1:
        return True
    else:
        return False

print(isDog("saaa"))

# --KARŞILAŞTIRMA OPERATORLERİ-- #
# !=
# ==
# <= , >= , < , >

