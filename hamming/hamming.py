def distance(strand_a, strand_b):
    if len(strand_a)!= len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        l= 0
        for i,b in enumerate(strand_a):
            if strand_b[i]!= b:
                l+=1
        return l
