class Uczen:
    
    def __init__(self, name , surname, age ):
        self.name = name
        self.surname = surname 
        self.age = age

    def get_name(self):
        return self.name
    


mat = Uczen("Mateusz","Hryciuk", 40)
luk = Uczen("Lukasz","Skywalker", -1300)
fra = Uczen("Franciszek", "Malkowski", 13)



# mat.name = "Mateusz"
# mat.surname = "Hryciuk"

# luk.name = "Lukasz"
# luk.surname = "Sywalker"


print(fra.get_name())


# stworzyć klasę zakupy - kalendarz 
# musi nazwe 
# data
# godzine 
# ile dostałem puntów rabatu 
# funkcja która zwraca każe z tych wartośći 
# koniecznie def __init__

nazwa = "zakupy"
data = "05.04.2023 r."
godzina = "15:32"
rabat = "800 punktów"

class Zakupy:

    def __init__(self,nazwa,data,godzina,rabat):
        self.nazwa = nazwa
        self.data = data
        self.godzina = godzina
        self.rabat = rabat
        

def get_Zakupy (self):
    return self


print(get_Zakupy(nazwa))

