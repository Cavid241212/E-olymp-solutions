n = int(input())
count= 1

list = [["0"]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i%2==0 and j%2==0 or i%2!=0 and j%2!=0:
            list[i][j]=count
            count += 1

x=count
for i in range(n):
    for j in range(n):
        if i%2==0 and j%2!=0 or i%2!=0 and j %2==0:
            list[i][j]=count
            count+=1
            print(list[i][j],end=" ")
        else:
            print(list[i][j],end=" ")
    print()