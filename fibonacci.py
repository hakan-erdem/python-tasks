fibo = [1]
n = 9

x = 0
y = 1
for i in range(n):

    total = x + y
    fibo.append(total)

    x = y
    y = total

print(fibo)