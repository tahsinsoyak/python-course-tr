secret_word = "snake" #bulunmasını istediğimiz kelime
guess = "" #tahmini depolayacağımız değişken
guess_count = 0 #tahmin edilme sayısı
guess_limit = 3   #tahmin hakkı
out_of_guesses = False #true olduğunda hakları bitti demektir

#tahmin kelimeye eşit olmadıkça devam ediyor
#ve hakları kaldığında devam edicek [false oldukça devam]
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You Lose!")
else:
    print("You win!")

