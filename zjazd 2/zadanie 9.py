produkty = {"maslo": 7, "bataty" :4  , "pomidory": 6}
magazyn = {"maslo": 100, "bataty" :200  , "pomidory": 300}
do_zaplaty= 0
while True :
    print ("Nasz zielnik oferuje : ")
    for produkt in produkty :
        print(f' - {produkt} -  {produkty[produkt]} PLN')

    komenda = input("Co chesz zrobic? [k]upic, [z]akonczyc, [d]odac ?")
    if komenda == "z":
        break
    elif komenda == "k":
        produkt_wybrany = input ("Co chcesz kupić ? ")
        if produkt_wybrany not in produkty:
            print ("Nie ma takiego produktu ")
            continue
        waga  = float(input(f"Ile chcesz kupic  [{produkt_wybrany}]"))
        if magazyn[produkt_wybrany] <waga:
        print (f"Mamy za mało[{produkt_wybrany}]")
        continue
        magazyn[produkt_wybrany] = magazyn[produkt_wybrany] - waga
        cena = produkty[produkt_wybrany]
        koszt = waga * cena
        do_zaplaty += koszt
    elif komenda == "d":
    produkt_do_dodania = input ("Jaki produkt chcesz dodac")
    if produkt_do_dodania not in magazyn :
        magazyn[produkt_do_dodania]= 0
        cena_nowego_produktu= float(input("Podaj cene nowego produkty"))
        produkty[produkt_do_dodania]= cena_nowego_produktu
        ile_produktu_dodajemy = float(input("Ile dodajemy produktu"))
        magazyn[produkt_do_dodania] += ile_produktu_dodajemy
    else :
        print ("Niepoprawna komenda")
    print(f"Cena to : {koszt} ")
    print (do_zaplaty)
