import datetime
now= datetime.datetime.now()
    print(now.year)
    print(now.month)


rok_urodzenia = float(input("Podaj swój rok urodzenia : "))

wiek = now.year- rok_urodzenia

if wiek >= 18 :
    print("Jesteś pełnoletni")

else :
    print("Nie jesteś pełnoletni")


