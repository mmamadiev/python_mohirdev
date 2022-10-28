# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
a=[]
a.append("Abror")
a.append("Sardor")
a.append("Sarvar")
print(a)
print(f"Salom {a[0]} tuzumisan?\n{a[1]} yaxshimisan?\n{a[2]} nima gap?")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni
# yuklang (musbat, manfiy, butun, o'nlik).
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik
# amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning
# qiymatini o'zgartiring, ba'zilarini esa almashtiring.
sonlar=[]
sonlar.append(56)
sonlar.append(-89)
sonlar.append(5.3)
sonlar.append(12_56)
sonlar[0]+=2
sonlar[2]=2
print(sonlar)
print(f"{sonlar[0]*sonlar[2]}")

# t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga
# o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga
# esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib
# olib (.pop()), quyidagi ko'rinishda chiqaring:

t_shaxslar=[]
z_shaxslar=[]
t_shaxslar.append("Stiv Jobs")
t_shaxslar.append("Al-Xorazmiy")
t_shaxslar.append("At-Termiziy")
z_shaxslar.append("Ilon Musk")
z_shaxslar.append("Bil Gates")
z_shaxslar.append("Mark Sukerburg")
b=z_shaxslar.pop(0)
a=t_shaxslar.pop(0)
print(f"Men tarixiy shaxslardan {a} va zamonaviy shaxslardan {b} bilan suxbat qurishni istardim\n")

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida
# 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove()
# metodi yordamida o'chrib tashlang.
# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va
# .append() metodlari yordamida mehmonga kelgan do'stlaringizning
# ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga
# qo'shing.


friend=[]
friend.append("Sarvar")
friend.append("Sobir")
friend.append("Jo\'rabek")
friend.append("Anvar")
friend.append("Jasur")
friend.append("Jahongir")
friend.append("Aziz")
friend.append("Nurali")
friend.insert(0, "Bobomurod")
del friend[0]
print(f"Mehmonga kelishi kerak edi {friend}\n")
friend.insert(0, "Abdurauf")
friend.insert(-1, "Muzaffar")
friend.insert(3, "Abdug\'affor")
print(f"Yangi qo\'shilgan do\'stlarim {friend}\n")
mehmonlar=[]
mehmonlar.append(friend.pop(0))
mehmonlar.append(friend.pop(-2))
mehmonlar.append(friend.pop(6))
mehmonlar.insert(-1, "Xolbek")
del mehmonlar[2]
print(f"Jigarlarim {mehmonlar}")