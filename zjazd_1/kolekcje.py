lista= [ -1,100,20 ,30,-15,12, 21, 54, 53]
dodatnie =[]
ujemne= []
for liczba in lista:
    if liczba<0 :
        ujemne.extend(liczba)

    elif liczba>0:
        dodatnie.extend(liczba)

print(len(ujemne))
print(len(dodatnie))



licznik_ujemnych= 0
licznik_dodatnich= 0
for el in lista:
    if el< 0:
        licznik_ujemnych +=1
    elif el > 0 :
        licznik_dodatnich +=1

print( "Dodatnich", licznik_dodatnich)
print( "Ujemnych", licznik_ujemnych)
