LICZBA_DNI_TYGODNIA = 7
numer_dnia = 1
suma_temperatur = 0
min_= None
max_ = None
while  numer_dnia <=LICZBA_DNI_TYGODNIA :
    temp = int(input(f"Podaj temperaturę z dnia {numer_dnia}"))
    suma_temperatur += temp
    if numer_dnia ==1:
        min_=temp
        max_=temp
        else
        if temp<min_:
            min_= temp

srednia_temperatur = suma_temperatur / LICZBA_DNI_TYGODNIA
print (f"Srednia temperatura w tyodniu to {srednia_temperatur}")
