# "a" append, dosyaya ekleme yapma
# dosyanın sonuna text ekleme
employee_file = open("employees-testfile.txt", "a")

# "w" overwrite yaparak bütün herşeyi silip sadece eklediğimizi yazar
# olmayan dosyadan denersek yeni bir dosya oluşturur.
employee_file = open("employees-testfile2.txt", "w")

#ekleme yapıyoruz write fonksiyonuyla
# "\n" yeni satıra iniyoruz
employee_file.write(" \nToby - Human Resources4")

employee_file.close()

#bütün dosya biçimlerini tanımlayıp yazdırıyoruz
website_file = open("index.html", "w")
website_file.write("<p>This is html</p>")
website_file.close()