# liczba = float(input("Podaj liczbe: "))
# zbior = set()
# parzyste_w_zakresie= set(range(2,100,2))
# for a in liczba :
#     if a not in zbior :
#     zbior.add(a)
#         if a in parzyste_w_zakresie
#         parzyste_w_zakresie +=1
#
# print(zbior)

liczby = set()
while True:
    komenda = input ("wprowadz liczbe lub k by zakocnzyc:")
    if komenda == 'k':
        break
    liczba= int(komenda)
    liczby.add(liczba)

print (len(liczby & set(range(2,101,2))))