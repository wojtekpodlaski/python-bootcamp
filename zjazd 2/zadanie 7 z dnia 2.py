slowo = input( "Podaj slowo : ")
a=0
samogloski = 'aeiou'

for i in slowo :
    if i in samogloski :
        a +=1
print (f"W tekscie znajduje sie {a}")