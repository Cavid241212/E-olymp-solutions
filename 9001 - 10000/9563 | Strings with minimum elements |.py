n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
a=[]
for i in range(n):
    for j in range(m):
        a.append(mat[i][j])
x=min(a)
for i in range(len(mat)):
    if x in mat[i]:
        
        print(i+1,end=" ")