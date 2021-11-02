import random 
#random kütüphanesini dahil ettik

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles =  ["John Lennon", "Paul    McCartnety", "George Harrison", "Ringo Star"]


#dosya uzantısını çektiğimiz fonksiyon
def get_file_ext(filename):
    return filename[filename.index(".")+1:]

#rastgele sayı tanımladığımız fonksiyon
def roll_dice(num):
    return random.randint(1,num)