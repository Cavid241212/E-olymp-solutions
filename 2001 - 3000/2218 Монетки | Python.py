n=int(input())
reshka=0
gerb=0
for i in range(n):
    qepik=int(input())
    if qepik==1:
        reshka+=1
    else:
        gerb+=1
print(min(reshka,gerb))