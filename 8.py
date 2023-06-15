dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

dp = [[] for _ in range(27)]

n = 50
k = 26

dp[0].append((0, 0))
for s in range(1, k + 1):
    unique_positions = set()
    for pos in dp[s - 1]:
        for d in range(8):
            nx = pos[0] + dx[d]
            ny = pos[1] + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                unique_positions.add((nx, ny))
    dp[s] = list(unique_positions)

print(len(dp[k]))