from random import randint
def losuj_polozenie ():
    return randint(1,10), randint(1,10)

def minimalna_liczba_krokow (gracz_x, gracz_y , skarb_x, skarb_y):
    return abs(skarb_x-gracz_x) + abs(skarb_y-gracz_y)


def zmiana_pozycji_gracza (gracz_x, gracz_y ):



skarb_x , skarb_y = losuj_polozenie()

gracz_x , gracz_y =losuj_polozenie()

while True:
    minimalna_liczba_krokow_przed_ruch= abs(skarb_x-gracz_x) + abs(skarb_y-gracz_y)
    ruch= input("Podaj kierunek ruchu w, a , s , d")
    if ruch == "w":
         gracz_y = gracz_y +1
    if ruch== "a":
        gracz_x = gracz_x -1
    if ruch== "s":
        gracz_y = gracz_y-1
    if ruch== "d":
         gracz_x = gracz_x +1

    min_l_krokow_po_ruchu= (skarb_x-gracz_x) + abs(skarb_y-gracz_y)

    if min_l_krokow_po_ruchu > minimalna_liczba_krokow_przed_ruch :
          print ("Zimno")
    if min_l_krokow_po_ruchu < minimalna_liczba_krokow_przed_ruch :
          print ("Ciepło")
    if min_l_krokow_po_ruchu == 0:
          print ("wygrałeś")


    print (f"Położenie skarbu :x={skarb_x}, y={skarb_y}")
    print (f"Położenie gracza :x={gracz_x}, y={gracz_y}")
