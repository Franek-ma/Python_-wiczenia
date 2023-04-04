from functions import *

liczby = [-1,34,-45,2,45,-79989,12,345,12,-46,23,-456,99]
slow = {1:"100",2:"200",3:"300"}

# odzielnie plik z funkcjami , rozwiązania i dane w pliku main.py
# funkcja która z podanej listy drukuje tylko liczby dodatnie 
# funkcja która drukuje liczby z listy podzielne przez 5
# fukcję która zwraca nową listę z liczbami mnniejszymi od zera 
# funkcję która wydrukuje element z podanego klucza 
print("Liczby dodatenie :")
positive_numbers(liczby)

print("Liczby podzielne przez 5 :")
divided_numbers(liczby)

print("Nowa lista z liczbami mniejszymi od zera : ")
new_postive_numbers_list(liczby)

#print("funkcję która wydrukuje element z podanego klucza : ")
#key_counter(slow)

# Super Fanciszek !!!
# zrobiłem małą modyfikcję w zadaniu  -  "funkcja która drukuje liczby z listy podzielne przez 5"
# raz tylko wspominałem o modulo ( % ) na lekcjach , to byo poza kursem kodland , mogłeś nie wiedzieć :) czasem się przydaje
# jutro omówimy po krótce ....i zaczynamy obiekty 
print("funkacja zwracająca wartości ze zsłownika ")
print(return_value(4,slow))

klucz = 4

if False:
    print(return_value(klucz,slow))
