print("Wybierz działanie") 
print("1 - dodawanie") 
print("2 - odejmowanie") 
print("3 - mnozenie") 
print("4 - dzielenie") 

wybor = input("Wybierz cyfre odpowiadajaca wlasciwemu dzialaniu '1,2,3,4' ") 
liczba1 = int(input("podaj pierwsza liczbe dzialania ")) 
liczba2 = int(input("podaj druga liczbe dzialania ")) 

def dodawanie(x, y): 
    return x + y 

def odejmowanie(x, y): 
    return x - y 
    
def mnozenie(x, y): 
    return x * y 
    
def dzielenie(x, y): 
    return x / y 
    
if wybor == "1": 
    print("Wynik twojego dodawania to: ", dodawanie(liczba1, liczba2) ) 

if wybor == "2": 
    print("Wynik twojego odejmowania to: ", odejmowanie(liczba1, liczba2) ) 

if wybor == "3": 
    print("Wynik twojego mnożenia to: ", mnozenie(liczba1, liczba2) ) 
    
if wybor == "4": 
    print("Wynik twojego dzielenia to: ", dzielenie(liczba1, liczba2) )