wymiar_x = float(input("Podaj pozycję na osi x"))
wymiar_y = float(input("Podaj pozycję na osi y"))

if wymiar_x> 100 or wymiar_y >100 or wymiar_x <0 or wymiar_y < 0 :
    print("Obszar poza granicą tablicy")

elif wymiar_x<10 and wymiar_y<10 :
    print("Gracz znajduje się w lewym dolnym rogu")
elif wymiar_x <10 and wymiar_y>90 :
    print("Gracz znajduje się w lewym górnym rogu")
elif wymiar_x>90 and wymiar_y<10 :
    print("Gracz znajduje się w prawym dolnym rogu")
elif wymiar_x>90 and wymiar_y>90 :
    print("Gracz znajduje się w prawym górnym rogu")
elif wymiar_x<10 :
    print("Gracz znajduje się na lewej krawędzi")
elif wymiar_x>90 :
    print("Gracz znajduje się na prawej krawędzi")
elif wymiar_y<10 :
    print("Gracz znajduje się na dolnej krawędzi")
elif wymiar_y>90 :
    print("Gracz znajduje się na górnej krawędzi")
else :
    print( "jesteś w centrum")