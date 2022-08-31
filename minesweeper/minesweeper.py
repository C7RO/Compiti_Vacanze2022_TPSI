def annotate(minefield):
    # Function body starts here
    #raise ValueError("The board is invalid with current input.")
    campo=[]
    if minefield== [] or minefield== [""]:
        return minefield
    lenprec=0
    for i,riga in enumerate(minefield):
        if lenprec == 0:
             lenprec=len(riga)
        if lenprec!= len(riga):
            raise ValueError("The board is invalid with current input.") 
        campo.append([])
        for casella in riga:
            if casella== " " or casella == "*":
                campo[i].append(casella)
            else:
                raise ValueError("The board is invalid with current input.") 
    for y,riga in  enumerate(campo):
        cont=0
        for x,casella in enumerate(riga):
            if campo[y][x]!='*':
                if y> 0:
                    if campo[y-1][x]=='*':
                        cont+=1
                    if x< len(riga)-1:
                        if campo[y-1][x+1]=='*':
                            cont+=1
                if y< len(campo)-1:
                    if campo[y+1][x]=='*':
                        cont+=1
                    if x> 0:
                        if campo[y+1][x-1]=='*':
                            cont+=1
                if x> 0:
                    if campo[y][x-1]=='*':
                        cont+=1
                    if y> 0:
                        if campo[y-1][x-1]=='*':
                            cont+=1
                if x< len(riga)-1:
                    if campo[y][x+1]=='*':
                        cont+=1
                    if y< len(campo)-1:
                        if campo[y+1][x+1]=='*':
                            cont+=1
            if cont != 0: 
                campo[y][x]=cont
            cont=0
    minefield.clear()
    for riga in campo:
        stringa=""
        for casella in riga:
            stringa+=str(casella)
        minefield.append(stringa)
    return minefield
