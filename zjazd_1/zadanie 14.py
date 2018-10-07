znalezione_max = None
znalezione_min = None


while True:
    dane_wejsciowe= input("Podaj liczbę lub wpisz KONIEC by zakonczyć")
    if dane_wejsciowe.lower() == "koniec":
        break
    liczba = int(dane_wejsciowe)
    if znalezione_max is None or liczba> znalezione_max:
        liczba= znalezione_max
    if znalezione_min is None or liczba< znalezione_min:
        liczba= znalezione_min

if not znalezione_max:
    print ("nie wprowadzono danych")

else:
    print (znalezione_max)
    print (znalezione_min)
