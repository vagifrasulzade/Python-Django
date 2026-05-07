"""
Tapşırıq 1: Encapsulation (Gizlilik) - "Ağıllı Telefon"
Bir "Telefon" sinfi (class) yaradın.
- Bu telefonun "model" və gizli "__batareya" (başlanğıcda 100 olsun) atributları olsun.
- "istifade_et(deqiqe)" adlı metod yazın. Hər 1 dəqiqə istifadə batareyanı 1% azaltsın.
- "zaryadka_yig()" adlı metod yazın. Bu metod batareyanı yenidən 100% etsin.
- Şərt: Elə bir məntiq qurun ki, batareya heç vaxt 0-dan aşağı düşməsin (0 olanda ekrana "Telefon söndü" yazsın) və kənardan heç kim kodla "menim_telefonum.__batareya = 5000" yaza bilməsin!


Tapşırıq 2: Inheritance və Polymorphism - "Qaraj"
Bir "Neqliyyat" (Ana sinif) yaradın. Onun sadəcə bir metodu olsun: "hereket_et()". Bu metod ekrana "Nəqliyyat hərəkət edir" yazsın.
- Daha sonra bu sinifdən miras (inherit) alan 3 fərqli törəmə sinif yaradın: "Avtomobil", "Velosiped" və "Qayiq".
- Polymorphism tətbiq edin: Hər bir törəmə sinifdə "hereket_et()" metodunu əzərək (override) özünəməxsus hərəkət formasını yazın (Məsələn: Avtomobil "Mühərriklə sürülür", Velosiped "Pedal çevrilir", Qayıq "Suda üzür").
- Bu 3 obyektdən ibarət bir list (siyahı) yaradın və "for" dövrünə salaraq hamısının hərəkət metodunu işə salın.

Tapşırıq 3: Duck Typing - "Müzakirə Klubu"
Python-da obyektin sinfi yox, bacarığı önəmlidir! (Ördək testi).
- Bir-biri ilə heç bir əlaqəsi olmayan (miras almayan) 3 sinif yaradın: "It", "Robot" və "Insan".
- Hər üç sinfin içində mütləq "danis()" adlı metod olsun (İt "Haf-haf", Robot "Bip-bop", İnsan "Salam" desin).
- Çöldə, heç bir sinfə aid olmayan sadə bir "konsert_ver(istirakci)" funksiyası yazın. Bu funksiya ona verilən obyektin sadəcə "danis()" metodunu işə salsın.
- Obyektləri yaradıb tək-tək bu funksiyaya göndərin və nəticəni izləyin!

"""

#1 

# class Telefon:
#     def __init__(self,model):
#         self.model = model
#         self.__batareya = 100
    
#     def istifade_et(self,deqiqe):
#         if self.__batareya > 0:
#             self.__batareya -= deqiqe
#             if self.__batareya < 0:
#                 self.__batareya = 0
#             print(f"{deqiqe} dəqiqə istifadə edildi. Qalan batareya: {self.__batareya}%")
#             if self.__batareya == 0:
#                 print("Telefon söndü")
#         else:
#             print("Telefon söndü")

#     def zaryadka_yig(self):
#         self.__batareya = 100
#         print("Batareya tam dolduruldu. Batareya: 100%")
    
#     def batareya_goster(self):
#         return self.__batareya
    
# menim_telefonum = Telefon("iPhone 15")

# menim_telefonum.istifade_et(30)
# menim_telefonum.istifade_et(80)   
# menim_telefonum.zaryadka_yig()

            
#2

# class Neqliyyat:
#     def hereket_et(self):
#         print("Nəqliyyat hərəkət edir")
    
# class Avtomobil(Neqliyyat):
#     def hereket_et(self):
#         print("Mühərriklə sürülür")

# class Velosiped(Neqliyyat):
#     def hereket_et(self):
#         print("Pedal çevrilir")
# class Qayiq(Neqliyyat):
#     def hereket_et(self):
#         print("Suda üzür")

# neqliyyatlar = [Avtomobil(), Velosiped(), Qayiq()]
# for n in neqliyyatlar:
#     n.hereket_et()


#3
class It:
    def danis(self):
        print("Haf-haf")

class Robot:
    def danis(self):
        print("Bip-bop")

class Insan:
    def danis(self):
        print("Salam")

def konsert_ver(istirakci):
    istirakci.danis()
    
it = It()
robot = Robot()
insan = Insan()

konsert_ver(it)
konsert_ver(robot)
konsert_ver(insan)