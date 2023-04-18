from datetime import datetime

class Zakupy:

    
    koszyk = []
    
    def __init__(self,nazwa,rabat):
        self.nazwa = nazwa
        self.data = str(datetime.now().date())
        self.godzina = str(datetime.now().strftime("%H:%M:%S"))
        self.rabat = rabat
        
    def get_zakupy(self):
        return self.nazwa +"  "+ self.data +"  "+ self.godzina +"  "+ str(self.rabat) + "%"

    def add_product(self,product):
        self.koszyk.append(product)

    def get_products(self):
        return self.koszyk

    def zakoncz():
        pass

    def get_name_products(self):
        names = []
        for name in self.koszyk:
            names.append(name.get_name())    
        return names
    
    def get_total_price(self):
        total_price = 0
        for price in self.koszyk:
            total_price += price.get_price()
        return "wartość koszyka: " + str(total_price)

            
    
class Product:

    def __init__(self,nazwa,cena):

        self.nazwa = nazwa
        self.cena = cena

    def get_price(self):
        return self.cena
    
    def get_name(self):
        return self.nazwa

jajka = Product("jaka wiejkie",12)

chleb = Product("chleb smaczny ", 10)

pomidory = Product("malinowe", 20)

pomidory2 = Product("jakbłkowe", 45)

zakupy_dzis = Zakupy("zakupy",20)

zakupy_dzis.add_product(jajka)
zakupy_dzis.add_product(chleb)
zakupy_dzis.add_product(pomidory)
zakupy_dzis.add_product(pomidory2)

print(zakupy_dzis.get_name_products())

print(zakupy_dzis.get_total_price())

#Stworzyć dodatkową funkcję w klasie Zakupy, która listuje produkty nazwa paragon
