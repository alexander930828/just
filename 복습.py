def sum(a):
    global n
    for i in range(a+1):
        n = n + i
    return n

n = 0
print(sum(5))


