# def prim(N):
#     primek=2
#     n=3
#     x=0
#     if N==2:
#         n=3
#     if N==1:
#         n=2
#     for i in range(10001):
#         if  i<1:
#             continue
#         if primek==N:
#             break
#         n+=1
#         if n%1==0 and n%n==0 and n%i!=0:
#             primek+=1
#             x=n
#     return n
# print(prim(6))
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








