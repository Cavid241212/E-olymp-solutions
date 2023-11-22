n = int(input())   # 25 % 10 = 5  

reqemler = []
eded_cem = 0
count = 0
a = n
while n>=0:
    if a == 0:
        break
    if n == 0:
        a -= eded_cem
        count += 1
        n = a
        a = n
        eded_cem = 0
    elif n % 10 != 0:
        x = n % 10
        n //= 10
        eded_cem += x


print(count)




