class Samochod:
    def __init__(self,name):
        self.name = name


class SamElektryczny(Samochod):
    def __init__(self,name,wb):
        self.wb = wb
        super().__init__(name)

class Spalinowy(Samochod):
    def __init__(self,name,pojemnosc):
        self.pojemnosc = pojemnosc
        super().__init__(name)


samochod1 = Spalinowy("samochód",50)

samochod2 = SamElektryczny("samochód_elektryczny",50)

print(samochod1.name)

print(samochod2.name)

#Znaleść cechę wspólną abstrakcyjną dla Broni trzech typów broni

#Klasa nadrzędna dla 3 typów broni muszą dziedzicyć conajmiej 2 cechy po klasie nadrzędnej

#Każda klasa podrzedna muśi mieć ceche swoją

#Każda z tych klas dziedziczy
