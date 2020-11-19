#Aufgabe 2 Kassensystem


Preis_A1= float(input("Bitte geben Sie den Preis für Artikel 1: "))
Anzahl_1=int(input("Bitte geben Sie die Anzhal des Artikels: "))
Preis_A2= float(input("Bitte geben Sie den Preis für Artikel 2: "))
Anzahl_2=int(input("Bitte geben Sie die Anzhal des Artikels: "))
Preis_A3= float(input("Bitte geben Sie den Preis für Artikel 3: "))
Anzahl_3=int(input("Bitte geben Sie die Anzhal des Artikels: "))
Preis_A4= float(input("Bitte geben Sie den Preis für Artikel 4: "))
Anzahl_4=int(input("Bitte geben Sie die Anzhal des Artikels: "))
Preis_A5= float(input("Bitte geben Sie den Preis für Artikel 5: "))
Anzahl_5=int(input("Bitte geben Sie die Anzhal des Artikels: "))


Artikeln=["Bannanen/Preis" ,"Äpfeln/Preis","Glassreiniger/Preis","Käse/Preis","Eier/Preis"]
Menge=[Anzahl_1,Anzahl_2,Anzahl_3,Anzahl_4,Anzahl_5]

Rechnung1=Preis_A1*Anzahl_1
Rechnung2=Preis_A2*Anzahl_2
Rechnung3=Preis_A3*Anzahl_3
Rechnung4=Preis_A4*Anzahl_4
Rechnung5=Preis_A5*Anzahl_5

Rechnung_g=Rechnung1+Rechnung2+Rechnung3+Rechnung4+Rechnung5
print()
#Artikeln.insert(1,Anzahl_1)
#Artikeln.insert(3,Anzahl_2)
#print(*Artikeln,"Anzahl" ,sep="\n")

print(Artikeln[0],":",Preis_A1,"Euro")
print("Artikel/Anzahl",":",Menge[0])
print(Artikeln[1],":",Preis_A2,"Euro")
print("Artikeln/Anzahl",":",Menge[1])
print(Artikeln[2],":",Preis_A3,"Euro")
print("Artikel/Anzahl",":",Menge[2])
print(Artikeln[3],":",Preis_A4,"Euro")
print("Artikel/Anzahl",":",Menge[3])
print(Artikeln[4],":",Preis_A5,"Euro")
print("Artikel/Anzahl",":",Menge[4])
print()
print(Preis_A1,'Euro x',Anzahl_1,"=",round(Rechnung1,2),"Euro")
print(Preis_A2,'Euro x',Anzahl_2,"=",round(Rechnung2,2),"Euro")
print(Preis_A3,'Euro x',Anzahl_3,"=",round(Rechnung3,2),"Euro")
print(Preis_A4,'Euro x',Anzahl_4,"=",round(Rechnung4,2),"Euro")
print(Preis_A5,'Euro x',Anzahl_5,"=",round(Rechnung5,2),"Euro")
print("---------------------")
print("Gesamt: ",round(Rechnung_g,2),"Euro")
print()
print("Vielen Dank für Ihreren Einkauf :D")