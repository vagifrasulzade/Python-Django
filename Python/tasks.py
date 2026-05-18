# 1) Ucbucaq ve Kvadrat meselesi:
"""
Hansi fiquru oyrenmek isteyirsiz: 3 ve ya 4

Daxil olan reqeme gore proqram bizden onun terefleri qeder olculerini daxil etmeyimizi isteyir:
Ex1:
Birinci terefi daxil et: 4
Ikinci terefi daxil et: 4
Ucuncu terefi daxil et: 4

Result: Bu fiqur beraberterefli ucbucaqdir

Ex1:
Birinci terefi daxil et: 4
Ikinci terefi daxil et: 4
Ucuncu terefi daxil et: 4
Dorduncu terefi daxil et: 4

Result: Bu fiqur kvadratdir.

Ucbucagin dogru olub olmadigi şərtinidə yoxlayın.

"""

# def fiqur_secimi():
#     secim = int(input("Hansi fiquru oyrenmek isteyirsiz: 3 ve ya 4\n"))
#     if secim == 3:
#         a = float(input("Birinci terefi daxil et: "))
#         b = float(input("Ikinci terefi daxil et: "))
#         c = float(input("Ucuncu terefi daxil et: "))
#         if a == b == c:
#             print("Bu fiqur beraberterefli ucbucaqdir")
#         else:
#             print("Bu fiqur ucbucaqdir, amma beraberterefli deyil.")
#     elif secim == 4:
#         a = float(input("Birinci terefi daxil et: "))
#         b = float(input("Ikinci terefi daxil et: "))
#         c = float(input("Ucuncu terefi daxil et: "))
#         d = float(input("Dorduncu terefi daxil et: "))
#         if a == b == c == d:
#             print("Bu fiqur kvadratdir.")
#         else:
#             print("Bu fiqur kvadrat deyil.")
#     else:
#         print("Yanlis secim etdiniz. Zəhmət olmasa 3 və ya 4 daxil edin.")

# print("FİQUR SEÇİMİ")
# fiqur_secimi()



# 2) Sadə bir xeberdarliq_et adlı dekorator yaradın.
"""
Bu dekorator hər hansı bir funksiyanı işə salmazdan dərhal əvvəl ekrana "Diqqət! Funksiya işə düşür..." yazısını çıxarsın.
Sonra çox sadə bir topla(a, b) funksiyası yazın və yaratdığınız dekoratoru @ işarəsi ilə bu funksiyanın üzərinə əlavə edin. Kodu işlədib nəticəni yoxlayın!
"""

# def xeberdarliq_et(func):
#     def wrapper(*args, **kwargs):
#         print("Diqqət! Funksiya işə düşür...")
#         return func(*args, **kwargs)
#     return wrapper

# @xeberdarliq_et
# def topla(a, b):
#     return a + b

# a = int(input("Birinci ədədi daxil edin: "))
# b = int(input("İkinci ədədi daxil edin: "))
# print("Toplama nəticəsi:", topla(a, b))

# 3) Avtomatik Bilet Kassanı (Generator)
"""
Təsəvvür edin ki, bankda və ya kinoteatrda növbə aparatısınız. Sizə hər dəfə müraciət ediləndə ardıcıl bir bilet nömrəsi verməlisiniz, amma aparat heç vaxt sönməməlidir (Sonsuz Dövr).
Tələb: bilet_ver() adlı bir generator funksiyası yazın. Bu funksiyanın içində while True: (sonsuz dövr) olsun. O, hər dəfə çağırılanda "BİLET-1", "BİLET-2", "BİLET-3" şəklində məlumat qaytarsın.
Funksiyanı yazdıqdan sonra ondan yalnız ilk 5 bileti alıb ekrana çap edin (qalanları üçün generatoru dondurulmuş vəziyyətdə saxlayın).
"""

def bilet_ver():
    bilet_num = 1
    while True:
        yield f"BİLET-{bilet_num}"
        bilet_num += 1
bilet_generator = bilet_ver()
for _ in range(5):
    print(next(bilet_generator))

