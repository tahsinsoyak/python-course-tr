#bir boolean tanımladık
is_male = False
is_tall = True

#tanımlamayı kontrol ettik
if is_male:
    print("You are a male")
else: #otherwise olarak kullanılıyor
    print("You are not a male")

#yada * veya seçenekli if koyduk
if is_male or is_tall:
    print("you are a male or tall or both")
else: #ikiside false olduğunda
    print("You neither male nor tall")

#ve seçenekli if
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")

#3 seçenekli if
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall): #is_tall ın tersini soruyoruz
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall or both")

