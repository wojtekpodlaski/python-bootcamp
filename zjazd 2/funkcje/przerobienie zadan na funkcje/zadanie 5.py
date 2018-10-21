def pobierz_dane ():
    miasto_z = input("Skąd jedziesz :")
    miasto_do = input("Dokąd :")
    spalanie = float(input("Ile pali na 100km :"))
    dystans = float(input("Jaka jest odleglość pomiędzy : "))
    cena_paliwa = float(input ("Ile kosztuje litr paliwa : "))

    return miasto_z , miasto_do, spalanie,dystans , cena_paliwa


def liczenie_kosztu (spalanie ,dystans ,cena_paliwa ):
    koszt = int(spalanie * dystans/100 *cena_paliwa)
    return koszt


dane =pobierz_dane()
print (dane)
koszt = liczenie_kosztu(dane[2],dane[3],dane[4])
print (koszt)

def drukuj_wynik(miasto_z , miasto_do, spalanie,dystans , cena_paliwa):
    output = f'''
    Miasto A {miasto_z}
    Miasto B {miasto_do}
    Dystans  {dystans}
    '''
    return output

