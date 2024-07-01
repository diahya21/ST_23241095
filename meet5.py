# inputan dari user
    
coba = input("masukan nama :")
print ("coba :" , coba , "tipe datanya :" , type(coba))

# aritmatika
x = 9 
y = 3 

# penjumlahan +
hasil = x + y
print(x , '+' , y , '=', hasil)

# pengurangan -
x = 7
y = 3

hasil = x - y 
print(x , '-', y, '=', hasil)

# perkalian *
x = 11
y = 4

hasil = x * y
print(x, '*', y, '=', hasil)

# pembagian /
x = 20
y = 5

hasil = x / y
print(x , '/', y, '=', hasil)

# exponen (perpengkatan) **
x = 9
y = 3
hasil = x ** y
print(x , '^', y, '=', hasil)

# modulus (sisa pembagian) %
hasil = x % y
print(x , 'Mod', y, '=', hasil)

# floor division (pembulatan kebawah) //
hasil = x // y
print(x , '//', y, '=', hasil)

# aritmatika prioritas

# (), exponen, perkalian, penjumlahan
x = 3
y = 4
z = 5
hasil = (x ** y * z + x / y - z % x // y)
print ( x, '**' , y, '*', z , '+', x , '/' , y ,'-' , z ,'%' , x ,'//' , y, "=", hasil)












