def isVocale(l):
    return l=='a' or l=='e' or l == 'i' or l=='o' or l=='u'

def translateWord(text):
    if isVocale(text[0]) or text[0:2]=="xr" or text[0:2]== "yt":
        text+=""
    elif text[0]!='y':
        if not(isVocale(text[1])):
            if text[1:3]=="qu":
                text=text[3:] +text[0:3]
            else:
                text=text[2:] +text[0:2]
        else:
            if text[0:2]=="qu":
                text=text[2:] +text[0:2]
            else:
                text=text[1:] +text[0]
    if not(isVocale(text[0])) and text[0:2]!="xr" and text[0:2]!= "yt":
        text=text[1:]+text[0]
    return text+"ay"
     
def translate(text):
    t=""
    text=text.split(" ")
    for i,word in enumerate(text):
        t+=translateWord(word)
        if i < len(text)-1:
            t+=" "
    return t
