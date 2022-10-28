#  Foydalanuvchidan juft son kiritishni so'rang.
# Agar foydalanuvchi juft son kiritsa "Rahmat!",
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

juft=int(input(f"Juft son kiriting:  \n>>>"))
if juft%2==0:
    print(f"{juft} soni juft")
else:
    print(f"{juft} toq son")

# Foydalanuvchi yoshini so'rang, va muzeyga
# kirish uchun chipta narhini quyidagicha chiqaring:

# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
yosh=int(input(f"Yoshingizni kiriting: "))
if 4>yosh or yosh>60:
    print(f"{yosh} yosh sizga chipta bepul!")
elif 18>yosh:
    print(f"{yosh} yosh sizga chipta narxi 10000 so\'m!")
else:
    print(f"{yosh} yosh sizga chipta narxi 20000 so\'m!")

# Foydalanuvchidan ikita son kiritishni so'rang,
# sonlarni solishtiring va ularning teng yoki 
# katta/kichikligi haqida xabarni chiqaring

a=int(input(f"Son kiriting:  \n>>>"))
b=int(input(f"Son kiriting:  \n>>>"))
if a==b: print(f"{a} va {b} sonlar teng")
elif a>b: print(f"{a} son katta {b} dan")
else:   print(f"{b} son katta {a} dan") 


# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni
# kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan
# savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni,
# mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa 
# "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" 
# degan xabarlarni chiqaring.  

mahsulotlar=["Un", "Makaron", "Sabzi", "Non", "Yog\'", "Gurunch","Piyoz", "Banan", "Tuz", "Kartoshka"]
savat=[] 
for l in range(5):
    savat.append(input(f"{l+1}-mahsulotingizni kiriting:\n>>>"))
for narsa in savat:
    if narsa in mahsulotlar:
        print(f"{narsa} bor")
    else:
        print(f"{narsa} yo\'q")

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot
# kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang,
# bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas 
# degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan
# barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi 
# mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

    
mahsulotlar=["Un", "Makaron", "Sabzi", "Non", "Yog\'", "Gurunch","Piyoz", "Banan", "Tuz", "Kartoshka"]
savat=[] 
bor_mahsulotlar=[]
mavjud_emas=[]

for l in range(5):
    savat.append(input(f"{l+1}-mahsulotingizni kiriting:\n>>>"))
for narsa in savat:
    if narsa in mahsulotlar:
        bor_mahsulotlar.append(narsa)        
        print(f"{narsa} bor")
    else:
        mavjud_emas.append(narsa)
        print(f"{narsa} yo\'q")
if mavjud_emas:
    print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan mahsulotlar do\'konimizda bor")

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login
# qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va
# foydalanuvchi kiritgan loginni foydalanuvchilar degan 
# ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda 
# bunday login mavjud bo'lsa, "Login band, yangi login 
# tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" 
# xabarini chiqaring.

foydalanuvchilar=[]
foydalanuvchilar.append("admin")
foydalanuvchilar.append("login")
foydalanuvchilar.append("Bonamur")
foydalanuvchilar.append("Miraziz")
foydalanuvchilar.append("Abdulaziz")
k=input("Login kiriting:\n>>> ")
if k.lower() in foydalanuvchilar:
    print(f"{k} logini BAND")
else:
    print(f"{k} HUSH KELIBSIZ")

# Foydalanuvchidan biror butun son kiritishni so'rang. 
# Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan 
# qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

son=int(input("Butun son kiriting:\n>>> "))
for k in (range(2,11)):
    if son%k==0:
        print(f"{son}/{k}={son/k} qoldiqsiz")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    