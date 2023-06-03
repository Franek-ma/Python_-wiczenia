from datetime import datetime




name = "Franciszek"
today = datetime.now()



footer = 'Utworzono przez {} , {}'.format(name, (str(today.day )+" ," + str(today.year)))


print(footer)