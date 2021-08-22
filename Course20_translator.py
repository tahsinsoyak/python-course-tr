#kendimize bir dil yaratıyoruz
#ünlü harfleri g harfine çevireceğiz
#vowels => g
#for döngüsüyle bütün sesli harfleri kontrol edeceğiz


#bir kelime girmeli fonksiyonumuzu tanımlıyoruz
def translate(phrase):
    translation = ""
    #yeni kelimeyi oluşturuyoruz
    for letter in phrase:
        #her harfi ünlülerden oluşan
        #kelimeyle kontrol ediyoruz
        #letter.lower() in "aeiou" yaparak sadece küçük harfleri kontrol edebiliriz
        if letter in "AEIOUaeiou":
            if letter.isupper(): #büyük harf kontroluT
                translation = translation + "G"
            else:
                translation = translation + "g"
            #kelimemizin arasına ekliyoruz
        else:
            translation = translation + letter
            #normal harf eklenmeye devam ediyor
    return translation


print(translate(input("Enter a phrase: ")))