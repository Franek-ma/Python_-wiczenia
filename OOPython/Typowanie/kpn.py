# lista = ["papier","kamień","nożyce"]

# cpoints = 0
# upoints = 0

# run = True
# imie = input("Podaj imię :")
# print("Witaj ", imie , " zagrajmy w papier-kamień-nożyce  !")


# while run:
#     comp_guess = random.randint(0,2)
#     user_guess = int(input("Podaj swój wybór 0 - papier , 1 -  kamień , 2 - nożyce , 3 - koniec gry "))
    
#     if user_guess == 3:
#         run = False 
       
#         print("Koniec gry")
        
    
#     if user_guess > 3 or user_guess < 0 :
#         print("Podaj właścwie dane")
  
    
#     if comp_guess == user_guess:
#         print("Komputer wybrał :" , lista[comp_guess])
#         print("Ty wybrałeś : ", lista[user_guess])
#         print("Remis !")
    
#     elif comp_guess == 0 and user_guess == 1:
#         print("Komputer wybrał :" , lista[comp_guess])
#         print("Ty wybrałeś : ", lista[user_guess])
#         print("Wygrał komputer !")
#         cpoints += 1 # cpoints = cpoints + 1 
        
#     elif comp_guess == 0 and user_guess == 2:
#         print("Komputer wybrał :" , lista[comp_guess])
#         print("Ty wybrałeś : ", lista[user_guess])
#         print("Twoja wygrana!")
#         upoints += 1
    
#     elif comp_guess == 1 and user_guess == 0:
#         print("Komputer wybrał :" , lista[comp_guess])
#         print("Ty wybrałeś : ", lista[user_guess])
#         print("Twoja wygrana!")
#         upoints += 1
        
        
#     elif comp_guess == 1 and user_guess == 2:
#         print("Komputer wybrał :" , lista[comp_guess])
#         print("Ty wybrałeś : ", lista[user_guess])
#         print("Wygrał komputer !")
#         cpoints += 1
        
#     elif comp_guess == 2 and user_guess == 0:
#         print("Komputer wybrał :" , lista[comp_guess])
#         print("Ty wybrałeś : ", lista[user_guess])
#         print("Wygrał komputer !")
#         cpoints += 1
        
#     elif comp_guess == 2 and user_guess == 1:
#         print("Komputer wybrał :" , lista[comp_guess])
#         print("Ty wybrałeś : ", lista[user_guess])
#         print("Twoja wygrana!")
#         upoints += 1
    
#     print("")    
#     print("Punkty komputera : " , cpoints)
#     print("Twoje punkty  : " , upoints)
#     print("")