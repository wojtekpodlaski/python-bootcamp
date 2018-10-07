liczby = [5,4,2,3,8]

min_i= None
max_i= None

indeksy = list(range(len((liczby))))
for i in indeksy :
    if min_i == None or liczby[i] < liczby[min_i]:
        min_i = i
    if max_i == None or liczby[i] > liczby[max_i]:
        max_i= i
if min_i is not None  and  max_i is not None :
    tmp=liczby[min_i]
    liczby[min_i]=liczby[max_i]
    liczby[max_i]=tmp



print(liczby)

#assert liczby2== [5,4,8,3,2]

#druga opjca liczby[min_1] ,liczby[max_i] = liczby[max_i], liczby[min_i]