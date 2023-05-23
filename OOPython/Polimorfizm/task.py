# klasa Firma , nazwa , liste urzdzen , nieabstrakcyjna
# Firma ma urzadzenia - klasa abstrakcyjna - z metoda abstrakcyjan "funkcja_urzadzenia"
# klasa abstrakcyjna bedzie urzadzenie
# 3 klasy urzadzen , np , komputer, samochod , traktor ....
# zaimplementowac funkcje "funkcja_urzadzenia" dla kazdej klasy dziedziczacej
# stworzyc 3 obiekty klas urzadzen , firma ma funkceje dodaj urzadzenie 
# firma ma metode , zeby wylistowac jakie mamy urzadzenia i co robia 
from abc import ABC, abstractmethod

class Firma:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.urzadzenia = []

    def dodaj_urzadzenie(self, urzadzenie):
        self.urzadzenia.append(urzadzenie)

    def wylistuj_urzadzenia(self):
        for urzadzenie in self.urzadzenia:
            print(urzadzenie.funkcja_urzadzenia())

class Urzadzenie(ABC):
    @abstractmethod
    def funkcja_urzadzenia(self):
        pass

class Komputer(Urzadzenie):
    def funkcja_urzadzenia(self):
        return "odpalam windows..."

class Samochod(Urzadzenie):
    def funkcja_urzadzenia(self):
        return "jeżdze ..."
    
class Traktor(Urzadzenie):
    def funkcja_urzadzenia(self):
        return "Stoję i się kurzę ..."
    
komputer = Komputer()
samochod = Samochod()
traktor = Traktor()

moja_firma = Firma("Moja Firma")

moja_firma.dodaj_urzadzenie(komputer)
moja_firma.dodaj_urzadzenie(samochod)
moja_firma.dodaj_urzadzenie(traktor)

moja_firma.wylistuj_urzadzenia()
