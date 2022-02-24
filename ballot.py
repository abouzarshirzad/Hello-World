n = int(input())
A = list()
C = list()
D = dict()

for i in range(0,n):
    B = input()
    A.append(B)

for i in range(0,n):
    a = A.count(A[i])
    C.append(a)

for i in range (0,n):
    D[A[i]]=C[i]

Y = list(D.values())
Z = list(D.keys())

print(A)
print(C)
print(D)
print(Y)
print(Z)

for i in range(0,len(D)):
    print(Z[i], Y[i])
    
