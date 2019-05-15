def prim(n):
    primlist = [2]
    num = 3
    while len(primlist) < n:
        for p in primlist:
            if num % p == 0:
                break
        else:
            primlist.append(num)
        num += 2
    return primlist[-1]
print(prim(9)) #csak teszt








