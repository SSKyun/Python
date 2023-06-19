N, H, W, P, Q = map(int, input().split())

r_seat = set()
for _ in range(N):
    p, q = map(int, input().split())
    r_seat.add((p, q))

min = float('inf')
best_seats = []
for p in range(H):
    for q in range(W):
        if (p, q) not in r_seat:
            D = abs(p - P) + abs(q - Q)
            if D < min:
                min = D
                best_seats = [(p, q)]
            elif D == min:
                best_seats.append((p, q))

for seat in best_seats:
    print(seat[0], seat[1])
