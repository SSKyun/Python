N = int(input())  # パイザ氏の旅程の日数

min_time = float('inf')  # 最も短い時間を無限大で初期化
max_time = float('-inf')  # 最も長い時間をマイナス無限大で初期化

for _ in range(N):
    s, f, t = map(int, input().split())  # 出発地の現地時間, 飛行時間, 到着地の現地時間

    time = (t - s + 24) % 24 + f  # パイザ氏の1日の時間を計算

    min_time = min(min_time, time)  # 最も短い時間を更新
    max_time = max(max_time, time)  # 最も長い時間を更新

# 結果の出力
print(min_time)
print(max_time)