def cell(P, T, N, M):
    cells = {
        'A': P,
        'B': 0,
        'C': 0
    }

    for _ in range(T):

        a_divide = cells['A'] // 2
        b_increase = a_divide * N
        c_increase = a_divide * M

        c_change = cells['C'] // 2
        a_increase = c_change

        cells['A'] += a_increase - a_divide
        cells['B'] += b_increase
        cells['C'] += c_increase - c_change

    return cells['A'], cells['B'], cells['C']

P = int(input())
N, M = map(int, input().split())
T = int(input())

result = cell(P, T, N, M)

print(result[0])
print(result[1])
print(result[2])