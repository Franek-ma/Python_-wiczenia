import random
#funkcja randowa, która generuje listę 100 liczb od 1 do 1000 i zwraca listę. dekolator bieże tylko liczby większe od 500
def decolator_li(func):
    def wrapper():
        lista = func()
        lista_li = []
        for li in lista:
            if li > 500:
                lista_li.append(li)
        
        return lista_li
    return wrapper


@ decolator_li
def genarator_licz():
    lista = []
    for i in range(1,1001):
        if i % 10 == 0:
            lista.append(i)

    return lista

print(genarator_licz())