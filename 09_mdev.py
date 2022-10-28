# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing,
#  va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta
# takrorlandi" degan xabarni chiqaring (n o'rniga kod necha
# marta takrorlanganini yozing)
dostlar=[]
dostlar.append("Sobir")
dostlar.append("Jasur")
dostlar.append("Ne\'mat")
dostlar.append("Abdurauf")
dostlar.append("Qodirbek")
for xabar in dostlar:
    print(f"Salom {xabar} ertaga xasharga kel!")
print(len(dostlar))

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing
# Ro'yxatning xar bir elementining kubini yangi qatordan
# konsolga chiqaring.
t_sonlar=list(range(11,101,2))
print("Har bir elementning natijalar")
for natija in t_sonlar:
    print(f"{natija} ning kubi {natija**3}")

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni
# so'rang, va kinolar degan ro'yxatga saqlab oling.
# Natijani konsolga chiqaring.
kinolar=[]
print("5 ta sevimli filmingizni kiriting:")
for kino in range(5):
    kinolar.append(input(f"{kino+1}-kino filmingiz?"))
print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini
# (suhbatlashganini) so'rang, va har bir suhbatlashgan 
# odamning ismini birma-bir so'rab ro'yxatga yozing. 
# Ro'yxatni konsolga chiqaring.
ismlar=[]
a=int(input("Nechta foydalanuvchi bilan suhbatlashdingiz?\n>>>"))
for j in range(a):
    ismlar.append(input(F"{j+1}-suhbatdoshingiz kim?"))
print(ismlar)
















