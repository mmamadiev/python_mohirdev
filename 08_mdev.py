# O'zingizga ma'lum davlatlarning ro'yxatini
# tuzing va ro'yxatni konsolga chiqaring
# Ro'yxatning uzunligini konsolga chiqaring
# sorted() funktsiyasi yordamida ro'yxatni 
# tartiblangan holda konsolga chiqaring
# sorted() yordamida ro'yxatni teskari 
# tartibda konsolga chiqaring
# Asl ro'yxatni qaytadan konsolga chiqaring
# reverse() metodi yordamida ro'yxatni ortidan 
# boshlab chiqaring
# sort() metodi yordamida ro'yxatni avval 
# alifbo bo'yicha, keyin esa alifboga teskari 
# tartibda konsolga chiqaring.
davlatlar=[]
davlatlar.append("Afrika")
davlatlar.append("Braziliya")
davlatlar.append("Bangladesh")
davlatlar.append("Xitoy")
davlatlar.append("Yaponiya")
davlatlar.append("Germaniya")
davlatlar.append("Rossiya")
davlatlar.append("Finlandiya")
davlatlar.append("Latviya")
davlatlar.append("Hindiston")
davlatlar.append("Pokiston")
print(davlatlar,"\n")
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar,"\n")
davlatlar.reverse()
print(davlatlar,"\n")
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar,"\n")

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi
# ayirmani hisoblang va konsolga chiqaring
# Ro'yxatdagi elementlar sonini hisoblang
# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta
# qiymatni konsolga chiqaring
sonlar=list(range(120,1201,2))
print(sonlar)
print(f''' Jami: {sum(sonlar)}
Ro\'yxatda eng kattasi {max(sonlar)}
Eng kichigi {min(sonlar)}
sonlar ayirmasi {max(sonlar)-min(sonlar)}''')
print(len(sonlar))
print(f"Ro'yxat boshi \n{sonlar[:20]}")
print(f"Ro'yxat o\'rtasi \n{sonlar[260:280]}")
print(f"Ro'yxat oxiri \n{sonlar[-21:-1]}")
a=sonlar[:20]
b=sonlar[260:280]
c=sonlar[-21:-1]
print(len(a))
print(len(b))
print(len(c))
























