def podaj_dane (liczba_a, liczba_b, operacja) :
    liczba_a = float(input("Podaj pierwszą liczbę: "))
    liczba_b = float(input("Podaj drugą liczbę: "))
    operacja = (input("Podaj typ obliczenia: "))
    return liczba_a ,liczba_b ,operacja



def obliczenia (liczba_a, liczba_b, operacja):
    if operacja== "+" :
        wynik= liczba_a + liczba_b
        print( wynik)
    elif operacja =="-":
        wynik= liczba_a - liczba_b
        print( wynik)

    elif operacja =="/" and liczba_b !=0:
        wynik= liczba_a /  liczba_b
        print( wynik)
    elif operacja =="/" and liczba_b==0:
        print("Nie dziel przez zero")
    
    elif operacja == "*":
        wynik = liczba_a * liczba_b

    else:
        print ("błędny znak")

dane = podaj_dane()
obliczenia (*dane)