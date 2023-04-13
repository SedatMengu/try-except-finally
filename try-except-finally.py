# hata yönetimi: python herhangi bir satırda hata oluştuğunda programa devam etmez ve sonlandırır.
# try - except blokları yardımı ile önceden görebileceğimiz hatalara karşı önlem alarak proogramımızın durmasını engellemiş oluruz.

a = 5
b = 6
print(a)
print(b)
d = 0
e = a / d
print(e)
print(d)

# yukarıdaki ekran çıktısında 5 , 6 yazacak ancak daha sonra hatalı satıra geldi ve devam edemeden program sonlandı. print(d) çalışmadı.

# try - except bloüu yapısı

# try :
#   // hata vermesi muhtemel kodları buraya yazdık
# except:
#   // hata alınca ne yapacağımızı buraya yazdık.
# else:
# // except bloğunda yakalanmayan bir hata varsa bu blok çalışacak
# finally:
# // sonuç ne olursa olsun her daim çalışır.


try:
    a1 = 5 
    b1 = 6
    d1 = 0
    c1 = a1 / d1
except:
    print("sıfıra bölünemez")
    
print(a1)
print(b1)
print(d1)

# sıfıra bölünemez
# 5
# 6
# 0

# açıklama : try komutunun içerisinde hata almayı beklediğimiz satırlara karşı except bloğu içerisinde bir hata mesajı yazdık.
# ilk önce hata olduğu için hata mesajı ekrana yazıldı ve program çalışmaya devam etti. print(a1) print(b1) print(d1) olarak.
# amacımızda zaten hatayı bulunca durmasını engellemekti.

a1 = 5 
b1 = 6
d1 = 0

try:
    c1 = a1 / d1
except:
    print("sıfıra bölünemez")
    
print(a1)
print(b1)
print(d1)

# bu şekilde hata vermeyeceğinden emin olduğumuz kodları try dışına alabiliriz.


# birden fazla çeşitte hata geliyor ise ?

try:
    a=5
    b=5             
    c=a/b                       # buradan sıfıra bölünemez hatası gelecek
    d=8                         # burada tanımlanmayan değişken hatası gelecek
    isim ="ali"
    karakter=isim[1]           # buradan olmayan index hatası gelecek
except ZeroDivisionError:
    print("payda sıfır olmamalı")
except NameError:
    print("tanımalanmayan değişken mevcut")
except IndexError:
    print("indexte hata yapıyorsun")
except Exception:
    print("bilinmeyen bir hata oluştu")
else:
    print("else bloğu çalşıyor.")       # eğer except bloğundaki hatalardan herhangi birisi çalışmaz ise else devreye girer.
finally:
    print("finally bloğu çalıştı.")     # her durumda bu blok çalışır.


# kendi hatamızı oluşturmak istersek:

try:
    a=8
    if a == 8:
        raise ZeroDivisionError
except ZeroDivisionError:
    print("bu hatayı ben gönderdim")




