def find_longest_swipe(numbers):
    n = len(numbers)
    max_swipe = 1

    # 横方向のスワイプをチェック
    for i in range(n):
        count = 1
        for j in range(n-1):
            if numbers[i][j] + 1 == numbers[i][j+1]:
                count += 1
            else:
                count = 1
            if count > max_swipe:
                max_swipe = count

    # 縦方向のスワイプをチェック
    for i in range(n):
        count = 1
        for j in range(n-1):
            if numbers[j][i] + 1 == numbers[j+1][i]:
                count += 1
            else:
                count = 1
            if count > max_swipe:
                max_swipe = count

    # 斜め方向のスワイプをチェック（右斜め上方向）
    for i in range(n-1):
        count = 1
        for j in range(n-1):
            if numbers[i][j] + 1 == numbers[i+1][j+1]:
                count += 1
            else:
                count = 1
            if count > max_swipe:
                max_swipe = count

    # 斜め方向のスワイプをチェック（左斜め上方向）
    for i in range(n-1):
        count = 1
        for j in range(1, n):
            if numbers[i][j] + 1 == numbers[i+1][j-1]:
                count += 1
            else:
                count = 1
            if count > max_swipe:
                max_swipe = count

    return max_swipe


# 入力の読み込み
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(list(map(int, input().strip())))

# 結果の出力
result = find_longest_swipe(numbers)
print(result)