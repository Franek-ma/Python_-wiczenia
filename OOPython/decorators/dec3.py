def li_pa(func):
    def wrapper():
        lista = func()
        lista_2 = []
        for i in lista:
            if i % 2 == 0:
                lista_2.append(i)

        return lista_2
    return wrapper    



        



@li_pa
def generator_li():
    lista = []
    for i in range(1,11):
        lista.append(i)

    return lista

@li_pa
def genarator_li2():
    lista_li2 = []
    for i in range(1,101):
        lista_li2.append(i)

    return lista_li2




print(generator_li())        
print(genarator_li2())


