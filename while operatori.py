# while operatori
#
# son = 1
# while son <= 5:
#     print(son, end='')
#     son = son + 1
#
# kiritilgan sonning kvadratini chiqaruvchi dastur
#
# print("Kiritilgan sonning kvadratini chiqaruvchi dastur.")
# savol = "Istalgan son kiriting: "
#
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat) ** 2)
#
# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son ** 2} ga teng")
#
# sonlar = list(range(1, 100))
# for son in sonlar:
#     if son == 50:
#         break
#     print(f"{son} ning kvadrati {son ** 2} ga teng")
#
# numbers = list(range(0, 100, 2))
# a = input("Nima qilay?")
# while a == "hisobla":
#     for number in numbers:
#         print(number ** 2)
#
#
# bo'sh ro'yxat ga yaqin do'stlarni qo'shish dasturi while yordamida
#
# ismlar = []
#
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n = 1
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob == 'ha':
#         n += 1
#         continue
#     else:
#         break
#
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
#
#
# While yordamida lug'atni to'ldirish dasturi
#
# print("Do;stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingizni ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
#
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
#
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")
#
# print(dostlar)


# Ro'yxatdan lug'atga element ko'chirish

# talabalar = ["jonibek", "husan", "olim", "botir"]
# baholangan_talabalr = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalr[talaba] = baho


# savatcha = []
# while True:
#     mahsulot = input("Mahsulotingizni savatchaga qo'shing: ")
#     savatcha.append(mahsulot)
#     javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
#     if javob != 'ha':
#         break

# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.


# savatcha = []
#
# while True:
#     mahsulot = input("Mahsulotingizni savatchaga qo'shing: ")
#     savatcha.append(mahsulot)
#     javob = input("Yana mahsulot kiritasizmi? (ha/yo'q)")
#     if javob != 'ha':
#         break


