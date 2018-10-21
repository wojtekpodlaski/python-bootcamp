def policzyc_ilosc_znakow (napis, start="<", stop =">"):
    poziom_zaglebienia= 0
    wynik  = 0
    start_i = 0
    end_i = 0
    for znak in napis :
        if znak == start:
            poziom_zaglebienia +=1
        elif znak == stop:
            poziom_zaglebienia -=1
        else :
            wynik += poziom_zaglebienia


    return wynik
#
# def test_0_poziom_zaglebienia ():
#     assert policzyc_ilosc_znakow("to jest napis")== 0
# def test_0_poziom_zaglebienia ():
#     assert policzyc_ilosc_znakow("to jest napis")== 0


print (policzyc_ilosc_znakow("ada ma <kota <ktory <jest> psem>>>"))

def test_policz_znak_pusty_napis ():
    assert policzyc_ilosc_znakow('') ==0

def test_policzyc_znaki_jeden_level_wartosci_domyslne ():
    assert policzyc_ilosc_znakow('ala ma <kota> a kot ma ale') ==4

def test_policzyc_znaki_dwa_levele ():
    assert policzyc_ilosc_znakow('ala [kota [a kot]] ma [ale]', '[', ']') ==18

def test_policzyc_znaki_trzy_levele():
    assert policzyc_ilosc_znakow('a <a<a<a>>>') ==6



# def policzyc_ilosc_znakow(napis, start="<", end=">")      -  PRZYPADEK DLA JEDNEGO NAWIASU
#
#     wynik  = 0
#     start_i = 0
#     end_i = 0
#     if "<" in napis :
#         start_i = napis.index ('<')
#     if ">" in napis :
#         end_i = napis.index ('>')
#     if start_i and end_i :
#         wynik = end_i - start_i
#     return wynik

