liczby= []
while len(liczby) <10:
    nowa_liczba= int(input("Proszę podać liczbę" ))
    liczby.append(nowa_liczba)

srednia=sum(liczby)/len(liczby)

print(srednia)