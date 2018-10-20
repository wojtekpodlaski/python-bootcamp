napis = input("Podaj słowo ")
liczniki_liter = {}

#zliczyc
for litera in napis :
    if litera in liczniki_liter:
        liczniki_liter[litera] = liczniki_liter[litera] +1
    else liczniki_liter[litera]= 1 :

# wyswietlic
for litera in napis:
    print (f"litera : {litera} wystąpiła {liczniki_liter[litera]} razy")


#
# elif :
#     liczniki_liter[litera] += 1
#
# #drugie
#     for litera in napis:
#         liczniki_liter[litera]= liczniki_liter.get(litera , 0) +1