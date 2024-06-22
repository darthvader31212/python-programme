import random

gesuchte_zahl = random.randint(1,100)
anzahl_versuche = int(input("wie viele versuche möchtest du haben\n"))
eingegebene_zahl = int(input("gib eine zahl zwischen 1-100 ein\n"))

nicht_gefunden = True
versuche_uebrig = anzahl_versuche > 0

while nicht_gefunden and versuche_uebrig:
    if (gesuchte_zahl == eingegebene_zahl):
        nicht_gefunden = False
    elif gesuchte_zahl > eingegebene_zahl:
        print ("die gesuchte zahl ist grösser als deine eingegebene\n")
        eingegebene_zahl = int(input("gib eine grössere zahl ein\n"))
    else:
        print ("die gesuchte zahl ist kleiner als deine eingegebene zahl\n")
        eingegebene_zahl = int(input("gib eine kleinere zahl ein\n"))
    anzahl_versuche = anzahl_versuche - 1
    versuche_uebrig = anzahl_versuche > 0

if not nicht_gefunden:
    print (f"du hast es geschafft und hättest noch {anzahl_versuche} Versuche übrig\n")
elif not versuche_uebrig:
    print ("leider nicht gerschafft, du hast keine Versuche mehr übrig\n")
