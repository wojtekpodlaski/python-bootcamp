miasto_z = input("Skąd jedziesz :")
miasto_do = input("Dokąd :")
spalanie = float(input("Ile pali na 100km :"))
dystans = float(input("Jaka jest odleglość pomiędzy : "))
cena_paliwa = float(input ("Ile kosztuje litr paliwa : "))

trasa = f"Trasa pomiedzy {miasto_z} a {miasto_do}"

koszt_przejazdu = (dystans/100)*cena_paliwa*spalanie

output = f"""
Miasto A : {miasto_z}
Miasto B : {miasto_do}
Dystans : {dystans}
Cena paliwa : {cena_paliwa}
Spalanie : {spalanie}

Koszt przejazdu  {miasto_z}- {miasto_do} to {koszt_przejazdu} PLN


"""
print(output)
