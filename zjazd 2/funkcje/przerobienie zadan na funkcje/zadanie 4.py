# cena_za_kg = 10
# waga= 2.5
# naleznosc = waga * cena_za_kg



def oblicz_naleznosc(cena_za_kg, waga):
    naleznosc= cena_za_kg * waga
    return naleznosc

def drukuj(waga, cena_za_kg):
    out=f"""Cena za kg{cena_za_kg}
    Waga: {waga}
    Należnosc: {oblicz_naleznosc(cena_za_kg,waga)}
    """
    print(out)


print (drukuj(5,123))


def test_naleznosci ():
    assert oblicz_naleznosc(4,10) == 40