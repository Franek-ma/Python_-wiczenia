class Bron:

    number_of_wepons = 0

    def __init__(self, name, range):
        super().__init__()
        self.name = name
        self.range = range
        Bron.number_of_wepons += 1

class Zabawka(Bron):
    def __init__(self, name, range, bullet):
        super().__init__(name, range)
        self.bullet = bullet

class Palna(Bron):
    def __init__(self, name, range, caliber, recoil):
        super().__init__(name, range)
        self.caliber = caliber
        self.recoil = recoil

class Karabin(Palna):
    def __init__(self, name, range, caliber, recoil, speed):
        super().__init__(name, range, caliber, recoil)
        self.speed = speed

class Shotgun(Palna):

    shotgun_nuber = 0

    def __init__(self, name, range, caliber, recoil, fire_mode):
        super().__init__(name, range, caliber, recoil)
        self.fire_mode = fire_mode
        Shotgun.shotgun_nuber += 1
        


nerf = Zabawka("Elite", "12m", "foam darts")

ak74 = Palna("ak74","480m","5.70 mm","4500 j")

m4a1 = Karabin("m4a1","520m","5.56 mm","4200 j","on 1 s 5 bullet")

m870 = Shotgun("m870","220 m","8.97 mm","7800 j","single fire")

test_2 = Shotgun("test","300 m","9.02 mm","8900 j","single fire")

print(Bron.number_of_wepons)

print(Shotgun.shotgun_nuber)

#Stworzyć klasę Firma w tej klasie muśi być spis użadzeń

#Napisać Klasę urządzenie mają być dodawane do listy w Firmie

#Trzy klasy dziedziczące po klasie urządzenia: It, pojazdy, maszyny rolnicze

