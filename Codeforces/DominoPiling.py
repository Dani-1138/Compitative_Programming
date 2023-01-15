def Domino(n,m):
    if n>=1 and n<=16 and m>=1 and m<=16:
        result=(n*m)/2
        return int(result)
    
M, N= input().split()
print(Domino(int(M),int(N)))
