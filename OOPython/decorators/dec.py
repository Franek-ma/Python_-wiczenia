

def simple_decorator(func):
    def wrapper(strr):
        print("przed")
        func(strr)
        print("po")
    return wrapper




@simple_decorator
def drukuj(string_f):
    print(string_f)

drukuj("Hej2")