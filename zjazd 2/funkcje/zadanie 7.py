def przytnij (data,start, stop):
    result= []
    for element in data:
        if start(element):
            result.append(element)
    return result

lista=[123,555,123123,555,3,3338346,1]

print (dane(lista,lambda x:x>3))


