class Bron:
    def __init__(self, name, range):
        super().__init__()
        self.name = name
        self.range = range

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
    def __init__(self, name, range, caliber, recoil, fire_mode):
        super().__init__(name, range, caliber, recoil)
        self.fire_mode = fire_mode


nerf = Zabawka("Elite", "12m", "foam darts")

ak74 = Palna("ak74","480m","5.70 mm","4500 j")

m4a1 = Karabin("m4a1","520m","5.56 mm","4200 j","on 1 s 5 bullet")

m870 = Shotgun("m870","220 m","8.97 mm","7800 j","single fire")

print(nerf.name) 

print(ak74.caliber)

print(m4a1.recoil) 

print(m870.fire_mode)

# Brawo Franciszku ! O to chodzio ..

