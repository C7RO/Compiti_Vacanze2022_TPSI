def is_pangram(sentence):
    sentence=sentence.lower()
    l='a'
    p=True
    while l <= 'z' and p==True:
        tro=False
        for r in sentence:
            if r== l:
                tro=True
        p=tro
        l=chr(ord(l)+1)
    return p