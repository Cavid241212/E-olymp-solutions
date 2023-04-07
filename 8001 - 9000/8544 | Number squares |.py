n=int(input())
for i in range(1,n+1):
    if i**2<=n:
        i**=2
        print(i,end=" ")
    else:
        break