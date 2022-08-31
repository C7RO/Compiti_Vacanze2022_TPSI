def value(colors):
    dictionary={"black": 0,"brown": 1,"red": 2,"orange": 3,"yellow": 4,"green": 5,"blue": 6,"violet": 7,"grey": 8,"white": 9}
    s=0
    for i,e in enumerate(colors[:2]):
        if e in dictionary:
            s+=dictionary[e]*10**(2-i-1)
    return s
