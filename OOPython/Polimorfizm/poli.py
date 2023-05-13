from abc import ABC , abstractmethod

class Computer(ABC):
    
    @abstractmethod
    def uruchamiam_sie(self):
        pass



class Laptop(Computer):
    def uruchamiam_sie(self):
        print("Staruje Linuks")

class LaptopSzkolny(Computer):
    def uruchamiam_sie(self):
        print("Staruje Windows")

class Telefon(Computer):

    def uruchamiam_sie(self):
        print("Startuje Android")


l1 = Laptop()

#com = Computer() tutaj blad , nie mozna utwurzy obiektu z klasy abstrakcyjnej

l2 = LaptopSzkolny()
t1 = Telefon()

l1.uruchamiam_sie()

l2.uruchamiam_sie()
t1.uruchamiam_sie()

l = []

l.append(l1)
l.append(l2)
l.append(t1)

print(l)


for item in l:
    item.uruchamiam_sie()




