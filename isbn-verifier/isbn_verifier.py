def is_valid(isbn):
    d=[n for n in isbn if n!= '-']
    for i,c in enumerate(d):
        if c >='0' and c <= '9':
            d[i]=int(c)
        elif c=='X' and i== 9:
            d[i]=10
        else:
            return False
    if len(d)!= 10:
        return False
    return (d[0] * 10 + d[1] * 9 + d[2] * 8 + d[3] * 7 + d[4] * 6 + d[5] * 5 + d[6] * 4 + d[7] * 3 + d[8] * 2 + d[9] * 1) % 11 == 0

