# gerçek dünyadaki nesnelere 
# farkli veri tipleriyle bir nesne oluşturuyoruz.

# student dosyasından "Student" clasını import ediyoruz
from student import Student

# bir öğrenci tanımladık, [Öğrenci nesnesi = student1]
# öğrenci yarattığımızda init fonksiyonunu çağırıyoruz
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

# bütün verilere erişebiliyoruz
print(student1.gpa)
print(student2.name)