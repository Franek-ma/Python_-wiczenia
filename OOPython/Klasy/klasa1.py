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


kauf1 = Zakupy("zakupy świąteczne",16)

kauf1.add_product("jajka")
kauf1.add_product("mąka")
kauf1.add_product("mleko")

print(kauf1.get_products())

# class products:

#     def __init__(self,nazwa,cena):

#         self.nazwa = nazwa
#         self.cena = cena

#     def add_product(self,product):
#         self.koszyk.append(product)

#     def get_products(self):
#         return self.koszyk

    
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

print(jajka.get_price())
print(pomidory.get_price())


