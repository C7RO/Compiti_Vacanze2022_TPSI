def convertToBase10(base, input):
    somma=0
    for i,n in enumerate(input[:]):
        somma+=(n*(base**(len(input)-i-1)))
    return somma

def decimalToBase(base, input):
    convertion=[]
    somma=input
    while somma> 0:
        print (somma)
        resto=somma%base
        convertion.append(resto)
        somma=somma//base
    if convertion==[]:
        convertion=[0]
    return convertion[::-1]

def checkList(digits, base):
    for d in digits:
        if not(d >= 0 and d < base):
            return False
    return True
    
def rebase(input_base, digits, output_base):
    if input_base< 2:
        raise ValueError("input base must be >= 2")
    elif output_base< 2:
        raise ValueError("output base must be >= 2")
    elif not(checkList(digits, input_base)):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    else:
        print(convertToBase10(input_base,digits))
        return decimalToBase(output_base, convertToBase10(input_base,digits))