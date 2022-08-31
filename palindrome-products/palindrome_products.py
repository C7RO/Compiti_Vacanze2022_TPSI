def isPalindromo(num):
    text=str(num)
    for i,l in enumerate(text):
        if l != text[len(text)-1-i]:
            return False
    return True
        
def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    largest=0
    lista=[]
    if min_factor> max_factor:
        raise ValueError("min must be <= max")
    else:
        for n1 in range(min_factor, max_factor+1):
            l1=(max_factor-(n1-min_factor))
            if largest<= l1*l1:
                for n2 in range(min_factor, max_factor+1):
                    l2=(max_factor-(n2-min_factor))
                    if isPalindromo(l1*l2) and largest == l1*l2:
                        lista.append([l1,l2])
                    elif isPalindromo(l1*l2) and largest < l1*l2:
                        largest= l1*l2
                        lista.clear()
                        lista.append([l1,l2])
    if largest== 0:
        return (None,[])
    return (largest,lista)
    
def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    smallest=None
    if min_factor> max_factor:
        raise ValueError("min must be <= max")
    else:
        for n1 in range(min_factor, max_factor+1):
            for n2 in range(min_factor, max_factor+1):
                if isPalindromo(n1*n2):
                    return ((n1*n2),[[n1,n2]])
    return (smallest,[])