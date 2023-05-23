from abc import ABC,abstractmethod 
import random

class Game(ABC):
    @abstractmethod
    def run(self):
        pass

class User:
    def __init__(self):
        name = input("Podaj imię: ")
        self.name = name

class Kpn(Game):
    def __init__(self,user):
        self.user = User

    upoints = 0

    run = True
    print("Witaj ", str(User) , "zagrajmy w papier-kamień-nożyce  !")




    def run(self):
        lista = ["papier","kamień","nożyce"]

        cpoints = 0
        upoints = 0

        run = True
        print("Witaj ", str(User) , " zagrajmy w papier-kamień-nożyce  !")

        while run:
            comp_guess = random.randint(0,2)
            user_guess = int(input("Podaj swój wybór 0 - papier , 1 -  kamień , 2 - nożyce , 3 - koniec gry "))
    
            if user_guess == 3:
                run = False 
        
                print("Koniec gry")
            
        
            if user_guess > 3 or user_guess < 0 :
                print("Podaj właścwie dane")
    
        
            if comp_guess == user_guess:
                print("Komputer wybrał :" , lista[comp_guess])
                print("Ty wybrałeś : ", lista[user_guess])
                print("Remis !")
            
            elif comp_guess == 0 and user_guess == 1:
                print("Komputer wybrał :" , lista[comp_guess])
                print("Ty wybrałeś : ", lista[user_guess])
                print("Wygrał komputer !")
                cpoints += 1 # cpoints = cpoints + 1 
                
            elif comp_guess == 0 and user_guess == 2:
                print("Komputer wybrał :" , lista[comp_guess])
                print("Ty wybrałeś : ", lista[user_guess])
                print("Twoja wygrana!")
                upoints += 1
            
            elif comp_guess == 1 and user_guess == 0:
                print("Komputer wybrał :" , lista[comp_guess])
                print("Ty wybrałeś : ", lista[user_guess])
                print("Twoja wygrana!")
                upoints += 1
                
                
            elif comp_guess == 1 and user_guess == 2:
                print("Komputer wybrał :" , lista[comp_guess])
                print("Ty wybrałeś : ", lista[user_guess])
                print("Wygrał komputer !")
                cpoints += 1
                
            elif comp_guess == 2 and user_guess == 0:
                print("Komputer wybrał :" , lista[comp_guess])
                print("Ty wybrałeś : ", lista[user_guess])
                print("Wygrał komputer !")
                cpoints += 1
                
            elif comp_guess == 2 and user_guess == 1:
                print("Komputer wybrał :" , lista[comp_guess])
                print("Ty wybrałeś : ", lista[user_guess])
                print("Twoja wygrana!")
                upoints += 1
            
            print("")    
            print("Punkty komputera : " , cpoints)
            print("Twoje punkty  : " , upoints)
            print("")

class Aad_game(Game):
    def __init__(self,user):
        self.user = User

    upoints = 0

    run = True
    print("Witaj ", str(User) , "zagrajmy w dodawnie!")

    def run(self):
        p_score = 0
        run = True

        while run:
            number_a = random.randint(1,67)
            number_b = random.randint(1,66)
            c_answer = number_a - number_b
            questions = int(input("podaj prawidłową odpowiedz:" + str(number_a) + "-" + str(number_b) + " = "))
            if questions == c_answer:
                p_score += 1
            else:
                p_score -= 2
            print("Twoje punkty  : " , str(p_score))
            print("")
            
class divide_game(Game):
    def __init__(self,user):
        self.user = User

    upoints = 0

    run = True
    print("Witaj ", str(User) , "zagrajmy w wmożenie!")

    def run(self):
        p_score = 0
        run = True

        while run:
            number_a = random.randint(1,67)
            number_b = random.randint(1,66)
            c_answer = number_a * number_b
            questions = int(input("podaj prawidłową odpowiedz:" + str(number_a) + "*" + str(number_b) + " = "))
            if questions == c_answer:
                p_score += 1
            else:
                p_score -= 2

            print("Twoje punkty  : " , str(p_score))
            print("")



class GameControler:
    def start(self):
        games_list = ["papier-kamień-nożyce : 1","dodawanie : 2 ","mnożenie : 3"]
        print("Zaraz będziesz mógl wybrać grę :")
        user = User()
        print(games_list)
        choice = int(input("W którą grę chcesz zagrać: "))
        if choice == 1:
            kpn = Kpn(user)
            kpn.run()

        if choice == 2:
            global Aad_game
            Aad_game = Aad_game(user)
            Aad_game.run()

        if choice == 3:
            global divide_game
            divide_game = divide_game(user)
            divide_game.run()

games = GameControler()

games.start()