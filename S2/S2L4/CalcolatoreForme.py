print("Ciao questo tool ti aiuterà a calcolare il perimetro di una formina a tua scelta :)")
print("Scegli una figura: ")
print("Quadrato")
print("Cerchio")
print("Rettangolo")
print("Esci")

scelta = input("\nMetti il nome di una figura sopra proposta: ")

if scelta == "Quadrato":
    lato = int(input("\nRiesci per favore a dirmi la lunghezza del lato del quadrato: "))
    print("Il perimetro del quadrato e': ", lato * 4)

elif scelta == "Cerchio":
    raggio = float(input("\nDimmi il raggio del tuo cerchio: "))
    print("La circonferenza misura: ",2 * 3.14 * raggio)

elif scelta == "Rettangolo":
    base = int(input("\nDimmi l'altezza boss: "))
    altezza = int(input("Dimmi l'altezza boss: "))
    print("Il tuo perimetro è: ", 2 * (base+altezza))

elif scelta == "Esci":
    print("Vattene allora ingrato!")
    

else:
    print("\nSei stordito? Leggi il menu delle scelte e ristarta il programma!")




