counter = 0
x = 200000001
while counter < 5:
    d = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.append([i, x // i])

    if len(d) >= 5:
        d.sort()[:5]

    print(d)
    x += 1
    counter += 1