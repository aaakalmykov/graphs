from random import shuffle, randint
n = int(input('Кількість вершин: ') or randint(1, 100))
minw = int(input('Мінімальна можлива вага ребра: ') or randint(0, 1000))
maxw = int(input('Максимальна можлива вага ребра: ') or randint(minw, 1000))
edges = [(i, j + (j >= i), randint(minw, maxw)) for i in range(n) for j in range(n - 1)]
m = int(input('Кількість ребер (від 0 до {}): '.format(n * (n - 1))) or randint(0, n * (n - 1)))
shuffle(edges)
edges = sorted(edges[: m])

inf = float('inf')
matrix = [[inf for j in range(n)] for i in range(n)]
for e in edges:
    matrix[e[0]][e[1]] = e[2]

b = [[j for j in i] for i in matrix]
p = [[i for j in range(n)] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if b[i][k] + b[k][j] < b[i][j]:
                b[i][j] = b[i][k] + b[k][j]
                p[i][j] = k
for i in range(n):
    for j in range(n):
        if b[i][j] == inf:
            p[i][j] = -1

l = max(len(str(j)) for i in b for j in i)
print('\n\nМатриця суміжностей:')
print('\n'.join(map(lambda x: ' '.join(map(lambda x: str(x).replace('inf', '∞').rjust(l), x)), matrix)))
print('\n\nB:')
print('\n'.join(map(lambda x: ' '.join(map(lambda x: str(x).replace('inf', '∞').rjust(l), x)), b)))
print('\n\nP:')
print('\n'.join(map(lambda x: ' '.join(map(lambda x: str(x + 1).replace('inf', '∞').rjust(l), x)), p)))

