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

class products:

    def __init__(self,nazwa,cena):

        self.nazwa = nazwa
        self.cena = cena

    def add_product(self,product):
        self.koszyk.append(product)

    def get_products(self):
        return self.koszyk

    
class products:

    def __init__(self,nazwa,cena):

        self.nazwa = nazwa
        self.cena = cena

    def get_price(self,cena):
        return self.cena
    
    def get_name(self,nazwa):
        return self.nazwa

products = products("test",16)

products.get_name("jajka")

products.get_price(5.00)

print(products.get_name("test"))

print(products.get_price(16))

