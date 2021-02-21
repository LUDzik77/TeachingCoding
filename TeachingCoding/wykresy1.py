from matplotlib import pyplot as plt


lista1=("rodzina Dominika", 3,  3, "red", 0, 0)
lista2=("rodzina Rafala", 0,  2, "blue", 0, 1)
lista3=("rodzina Staszka", 5,  1, "green", 2, 0)
lista4=("rodzina Ludwika", 2,  3, "red", 1, 0)


dziewczyny = [lista1[2], lista2[2], lista3[2], lista4[2]]
chlopaki = [lista1[1], lista2[1], lista3[1], lista4[1]]

#print(dziewczyny)
#print(chlopaki)

etykiety = ["dziewczyny: "+str(sum(dziewczyny)), "chlopaki: "+str(sum(chlopaki))]
kolory = ["pink", "lightblue"]
dane =[sum(dziewczyny), sum(chlopaki),]
plt.title("Ilosc chopakow i dziewczyn u naszych kuzynow")

plt.pie(dane, labels=etykiety, colors=kolory, wedgeprops={'edgecolor':"black"}, shadow=True, startangle=120, autopct='%1.1f%%')
plt.show()



#BELOW  an example of a chart for a single list:

from matplotlib import pyplot as plt
lista4=("rodzina Ludwika", 2,  3, "red", 1, 0)

dziewczyny = sum([lista4[2] + lista4[5]])
chlopaki = sum([lista4[2], lista4[5]], 1)

etykiety = ["dziewczyny: "+str(dziewczyny), "chlopaki: "+str(chlopaki)]
kolory = ["yellow", lista4[3]]
dane =[dziewczyny, chlopaki]
plt.title(lista4[0])

plt.pie(dane, labels=etykiety, colors=kolory, wedgeprops={'edgecolor':"black"}, shadow=True, startangle=120, autopct='%1.1f%%')
plt.show()


# BELOW sth if we have additional time:
kuzyni = [lista1[2]+lista1[1], lista2[2]+lista2[1], lista3[2]+lista3[1], lista4[2]+lista4[1]]
rodziny = [lista1[0], lista2[0], lista3[0], lista4[0]]

plt.title("Kuzyni w naszych rodzinach")
plt.bar(rodziny, height = kuzyni, color="grey", edgecolor="black") 

plt.show()