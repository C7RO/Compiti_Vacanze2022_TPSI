def steps(number):
    passi=0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else: 
        if number!= 1:
            if number%2 != 0:
                number=number*3+1
            else:
                number=number/2
            passi=steps(number)+1
    return passi
        
