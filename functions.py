
def positive_numbers(liczby):
     for nu in liczby:
        if nu > 0:
            print(nu)

def divided_numbers(liczby):
    for nu in liczby:
        # divided_number_list = nu / 5
        divided_number_list = []
        if nu % 5 == 0 :
            divided_number_list.append(nu)
            print(divided_number_list)

def new_postive_numbers_list(liczby):
    for nu in liczby:
        new_postive_counters_list = []
        if nu < 0:
            new_postive_counters_list.append(nu)
            print(new_postive_counters_list)
            
def key_counter(slow, key):
    for ke in slow:
        key_count = int(input("podaj liczbe klucza: "))
        key = key_count
        if key_count == key:
            print(slow[key_count])


def return_value(key, slownik):
    if key in slownik:
        return slownik[key]
    if key not in slownik:
        return False
    



