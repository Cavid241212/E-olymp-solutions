n,m=map(int, input().split())
mat1=[list(map(int,input().split()))*m for i in range(n)]
count=0
count1=0

for i in range(n):
    for j in range(m):
        
            count+=mat1[i][j]
            
print(count)