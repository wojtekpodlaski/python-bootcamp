# 1 pobierz dane
# 2 policzyc srednia
# 3 ustalic min i max
# 4 zaprezentuj dane


LICZBA_DNI_TYGODNIA = 7
def pobieranie_danych (ile_razy= 7):
    temperatury = []
    for i in range (ile_razy):
        temp = int(input(f"Podaj temperaturę z dnia {i+1}"))
        temperatury.append(temp)
    return temperatury


def srednia_temp(temperatury):
    srednia_temperatura = sum(temperatury) / len(temperatury)
    return srednia_temperatura


def znajdz_ekstrema (temperatury):
    min_= min(temperatury)
    max_= max(temperatury)
    return min_, max_

def prezentuj_dane(srednia_temperatura, min_,max_):
    print (f"Srednia temperatura w tyodniu to {sr_temp}")
    print (f"Najwieksza temperatura w tyodniu to {max_}")
    print (f"Najmniejsza temperatura w tyodniu to {min_}")

dane = pobieranie_danych()
sr_temp = srednia_temp(dane)
min_,max_= znajdz_ekstrema(dane)
prezentuj_dane(sr_temp, min_,max_)
