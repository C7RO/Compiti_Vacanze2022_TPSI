def is_armstrong_number(number):
    num=number
    lista=[] 
    while number > 0:
        lista.append(number%10)
        number=int(number/10)
    lun=len(lista)
    somma= 0
    for s in lista:
        somma+=s**lun
    return num == somma