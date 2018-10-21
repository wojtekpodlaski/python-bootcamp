# def drukuj_linie ():
#     print ("-")
#
# def zwroc_wartosc_wpisana():
#     wartosc = input ("podaj wartosc")
#     return wartosc
#
# x= zwroc_wartosc_wpisana()
#
#
#
#
#
# def sumator (a):
#     return sum(a)
#
# a = [1,2,3,4,5]
#
# print (sumator(a))
#
#

def kalkulator (a, b , operacja ="+"):
    if operacja == "+":
        return a+b
    elif operacja == "-":
        return a-b

print (kalkulator(1 ,2))
print (kalkulator (1 , 2,"-"))



def foo (a):
    if a> 2:
        b= "haha"
    print (b)

foo (4)