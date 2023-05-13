from abc import ABC , abstractmethod

class Bron(ABC):
    @abstractmethod
    def fire(self):
        pass
    def numbers(self,n):
        for i in range(n):
            self.fire()
    

class Shotgun(Bron):
    def fire(self):
        print("Strzelam Shotgun")


class karabin(Bron):
    def fire(self):
        print("Strzelam karabin")

class proca(Bron):
    def fire(self):
        print("Strzelam proca")

sh = Shotgun()
ka = karabin()
pr = proca()
    
l = [sh,ka,pr]



for item in l:
    item.numbers(3)