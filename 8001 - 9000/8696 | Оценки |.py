n = input()
digit_counts = [n.count(str(i)) for i in range(10)]
max_count = max(digit_counts)

if digit_counts.count(max_count) == 1:
    print(digit_counts.index(max_count))
else:
    print("=")
