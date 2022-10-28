# Quyidagi mashqlarni bajaring:

# Quyidagi o'zgaruvchilarni yarating:
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor"
# viloyat="Samarqand"
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(f" {kocha} ko\'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini
# qo'llab ko'ring.
kocha=input("Ko'changiz:  \n>>>")
mahalla=input("Mahallangiz:  \n>>>")
tuman=input("Shahringiz:  \n>>>")
viloyat=input("Viloyatingiz:  \n>>>")
print(f" {kocha} ko\'chasi\n {mahalla} mahallasi\n {tuman} tumani\n {viloyat} viloyati\n")
manzil=f" {kocha} ko\'chasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati\n"
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())



