import math  # dołączamy bibliotekę matematyczną
start = "t"  # deklarujemy i inicjujemy zmienną pomocniczą
while start != "n":  # dopóki wartość zmiennej op jest inna niż znak "n"
    dane = input("Podaj 3 boki trójkąta (oddzielone przecinkami): ")

    lista = []  # definicja pustej listy
    for x in dane.split(","):
        lista.append(int(x)) #dodanie elementu do listy
    a, b, c = lista

    print("Podano boki: ", a, b, c)