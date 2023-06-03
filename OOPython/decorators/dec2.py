def dekorator(func):
    def wrapper(l):
        print("oto twoja lista")
        func(l)
        print("zapisano do bazy danych")
    return wrapper





lista = ["coś",123,"Python","dekorator"]


@dekorator
def liczby(lista):
    for li in lista:
        print(li)

liczby(lista)

@dekorator
def drukuje(string):
    print(string)


drukuje("drukuje...")