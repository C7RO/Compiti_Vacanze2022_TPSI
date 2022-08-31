def is_isogram(string):
    i=True
    string=string.lower()
    for index,t in enumerate(string):
        for l in string[index+1:]:
            if t==l and t!= " " and t != "-":
                i=False
    return i
