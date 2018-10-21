#
# def formatuj(*args, **kwargs):
#     out = []
#     for text in args :
#         for k in kwargs :
#         text = text.replace(f'${k}', str(kwargs[k]))
#         out.append (text)
#     return "\n".join(out)
#
#
#
# def test_formatuj ():
#     assert formatuj(
#         10,
#         'koszt $cena PLN,'
#         'kwota $cena brutto'
#     ) == "koszt 10 PLN\nkwota 10 brutto"

def podzielna_przez_2(x):
    return x%2 ==0
print (podzielna_przez_2(12))
print (podzielna_przez_2(11))

y = lambda x: x%2 ==0


def wybierz (dane, warunek ):
    out=[]
    for element in dane:
        if warunek(element):
            out.append(element)
    return (out)

def podzielna_przez_3(x):
    return x%3==0

lista =[1,2,3,4,5, 234,2366,12334]
print(wybierz(lista,podzielna_przez_2))
print(wybierz(lista,lambda x: x%3==0))
print(wybierz(lista,podzielna_przez_3))


