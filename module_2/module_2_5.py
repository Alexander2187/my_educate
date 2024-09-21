def get_matrix(n, m, value):
    up = []
    if (n <= 0 or m <= 0):
        return up
    for i in range(n):
        down = []
        for k in range(m):
            down.append(value)
        up.append(down)
    return up


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
