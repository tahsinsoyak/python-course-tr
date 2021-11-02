# öğrenci sınıfı
class Student:
    # initialize fonksiyon, başlangıç fonksiyonu
    # constructor
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    # iyi öğrenci mi diye kontrol edeceğiz
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

# self.name =>  attribute [nesneye ait]
# c# Constructors işlevi görüyor inti fonksiyonu