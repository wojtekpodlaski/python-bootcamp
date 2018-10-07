from random import randint
s_x = randint(1,10)
s_y =randint(1,10)
g_x= randint(1,10)
g_y =randint(1,10)

while True:
    minimalna_liczba_krokow_przed_ruch= abs(s_x-g_x)+ abs(s_y-g_y)
    ruch= input("Podaj kierunek ruchu w, a , s , d")
    if ruch == "w":
         g_y = g_y +1
    if ruch== "a":
        g_x = g_x -1
    if ruch== "s":
        g_y = g_y-1
    if ruch== "d":
         g_x = g_x +1

    min_l_krokow_po_ruchu= abs(s_x-g_x)+ abs(s_y-g_y)

    if min_l_krokow_po_ruchu > minimalna_liczba_krokow_przed_ruch :
          print ("Zimno")
    if min_l_krokow_po_ruchu < minimalna_liczba_krokow_przed_ruch :
          print ("Ciepło")
    if min_l_krokow_po_ruchu == 0:
          print ("wygrałeś")


    print (f"Położenie skarbu :x={s_x}, y={s_y}")
    print (f"Położenie gracza :x={g_x}, y={g_y}")
