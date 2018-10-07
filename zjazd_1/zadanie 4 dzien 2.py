lista=[]
for liczba in range (101):
        if liczba % 3==0 or liczba %5 == 0:
            lista.append(liczba)

print(len(lista))
print(lista)