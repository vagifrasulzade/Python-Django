# Home Task
"""
Tapşırıq 1: "Heyvanlar Aləmi və Duck Typing"
- "Qartal" və "Teyyare" adlı iki fərqli sinif yaradın. Bu siniflərin bir-biri ilə heç bir qohumluğu (inheritance) olmasın.
- Hər iki sinfə "uc()" metodu əlavə edin. Qartal üçün "Qartal qanad çalaraq uçur", Təyyarə üçün "Təyyarə mühərriklə uçur" çap edilsin.
- Çöldə "goy_uzune_ bax(obyekt)" adlı funksiya yazın. Bu funksiya daxilinə gələn obyektin kimliyini yoxlamadan sadəcə "uc()" metodunu çağırsın. (Duck Typing sınağı).

Tapşırıq 2: "Hero vs Monster" (Inheritance & Overriding)
- "Personaj" adlı ana sinif yaradın: ad, can atributları olsun.
- "Doyuscu" sinfi yaradın (Personajdan miras alsın). "hucum_et()" metodu "Qılıncla zərbə endirdi!" desin.
- "Sehrbaz" sinfi yaradın (Personajdan miras alsın). Eyni adlı "hucum_et()" metodunu əzin (override) və "Alov topu atdı!" yazdırın.
- Bu personajları bir listə yığın və dövr (loop) vasitəsilə hamısını eyni anda hücuma keçirdin (Polymorphism).

Tapşırıq 3: "Kitabxana Sistemi" (Class Methods & Properties)
- "Kitab" sinfi yaradın: __ad, __muellif (gizli atributlar).
- "@property" istifadə edərək bu atributlar üçün getter və setter yazın (Məsələn, kitab adı boş qoyula bilməz).
- "@classmethod" yaradın: "str_ile_yarat(melumat)". Bu metod "Səfillər-Viktor Hüqo" kimi bir mətni qəbul edib onu parçalasın və yeni bir Kitab obyekti qaytarsın.
"""


#1

# class Qartal:
#     def uc(self):
#         print("Qartal qanad çalaraq uçur")

# class Teyyare:
#     def uc(self):
#         print("Təyyarə mühərriklə uçur")

# def goy_uzune_bax(obyekt):
#     obyekt.uc()

# qartal = Qartal()
# teyyare = Teyyare()

# goy_uzune_bax(qartal)
# goy_uzune_bax(teyyare)


#2

# class Personaj:
#     def __init__(self, ad, can):
#         self._ad = ad
#         self._can = can

#     def hucum_et(self):
#         print("Sade hucum etdi!")

# class Doyuscu(Personaj):
#     def hucum_et(self):
#         print(f"{self._ad} Qılıncla zərbə endirdi!")

# class Sehrbaz(Personaj):
#     def hucum_et(self):
#         print(f"{self._ad} Alov topu atdı!")

# personajlar = [Doyuscu("Ali", 100), Sehrbaz("Veli", 80)]

# for personaj in personajlar:
#     personaj.hucum_et()


#3
# Tapşırıq 3

class Kitab:
    def __init__(self, ad, muellif):
        self.ad = ad
        self.muellif = muellif

    @property
    def ad(self):
        return self.__ad

    @ad.setter
    def ad(self, value):
        if not value.strip():
            raise ValueError("Kitab adı boş ola bilməz!")
        self.__ad = value

    @property
    def muellif(self):
        return self.__muellif

    @muellif.setter
    def muellif(self, value):
        if not value.strip():
            raise ValueError("Müəllif adı boş ola bilməz!")
        self.__muellif = value

    @classmethod
    def str_ile_yarat(cls, melumat):
        ad, muellif = melumat.split("-")
        return cls(ad.strip(), muellif.strip())


kitab1 = Kitab("1937", "Qurban Səid")
print(kitab1.ad, "-", kitab1.muellif)

kitab2 = Kitab.str_ile_yarat("Dəli Kür-İsmayıl Şıxlı")
print(kitab2.ad, "-", kitab2.muellif)
