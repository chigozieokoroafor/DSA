def distance(strand_a, strand_b):
    new_strand_A = []
    new_strand_B = []
    for i in strand_a:
        new_strand_A.append(i)
    for j in strand_b:
        new_strand_B.append(j)

    x = 0
    count = 0
    if len(new_strand_A) != len(new_strand_B):
        raise Exception("length of strand isn't equal")
    while x<len(new_strand_A):
        if new_strand_A[x] != new_strand_B[x]:
            count = count+1
        x = x+1

    return count

