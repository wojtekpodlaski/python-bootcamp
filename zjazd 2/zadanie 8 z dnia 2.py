nawias1 = 0
nawias2 = 0

text = input ("Podaj text")

for index , i in enumerate (text):
    if i == "<" :
        nawias1 = index

    if i == ">" :
        nawias2 = index

print (nawias2 - nawias1-1)

#sposob 2

czy_miedzy_nawiasami = False
licznik = 0

for znak in text:
    if znak =="<":
        czy_miedzy_nawiasami = True
    elif znak == ">":
        czy_miedzy_nawiasami = False
    elif czy_miedzy_nawiasami:
        licznik +=1

print (licznik)