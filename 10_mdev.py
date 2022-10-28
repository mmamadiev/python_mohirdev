# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# degan ro'yxat tuzing, ro'yxat elementlarining birinchi 
# harfini katta qilib konsolga chqaring. GM uchun ikkala 
# harfni katta qiling.
yangi_cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for k in yangi_cars:
    if k=="gm":
        print(k.upper())
    else:
        print(k.title())

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
yangi_cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for k in yangi_cars:
    if k!="gm":
        print(k.title())
    else:
        print(k.upper())
        
# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa,
# "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"
# xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, 
# {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
user=input("Loginni kiriting:\n>>>")
if user.lower()=="admin":
    print('''Xush kelibsiz, Admin!
Foydalanuvchilar ro'yxatini ko'rasizmi?''')
else:
    print(f"Login xato, {user}")

# Foydalanuvchidan 2 ta son kiritishni so'rang
# Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng"
# ekan degan yozuvni konsolga chiqaring.
a=int(input("1-sonni kiritng:\n>>>"))
b=int(input("2-sonni kiritng:\n>>>"))
if a==b:
    print(f"{a} va {b} sonlar teng!")
else:
    print(f"{a} va {b} sonlar teng emas!")
    
# Foydalanuvchidan istalgan son kiritishni so'rang.
# Agar son manfiy bo'lsa konsolga "Manfiy son", 
# agar musbat bo'lsa "Musbat son" degan xabarni 
# chiqaring.
 
a=int(input("Son kiritng:\n>>>"))
if a>0:
    print(f"{a} musbat son")
else:
    print(f"{a} manfiy son")

# Foydalanuvchidan son kiritishni so'rang, agar son
# musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
# Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni
# chiqaring.

a=int(input("Son kiritng:\n>>>"))
if a>0:
    print(f"{a**(1/2)}")
else:
    print("Musbat son kiriting")























    