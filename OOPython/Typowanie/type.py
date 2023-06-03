


def checking(s: str , i: int ) -> str:

    return i * s

checking(1,2)



def mapa(lam , lista):
    result = []
    for item in lista:
        new = lam(item)
        result.append(new)
    return result    


num = [1,2,3,4,5]

lam = lambda x : x * x
lam2 = lambda x : x * x * x

print(mapa(lam2,num))



