def ball_passing(num_balls, passes):
    num_players = len(num_balls)  # 플레이어의 인원 수

    for pass_info in passes:
        sender = pass_info[0]  # 패스하는 플레이어의 인덱스
        receiver = pass_info[1]  # 받는 플레이어의 인덱스
        num_to_pass = pass_info[2]  # 패스할 공의 개수

        # 패스할 공의 개수를 보내는 사람이 가지고 있는 공의 개수와 비교
        if num_to_pass >= num_balls[sender]:
            num_to_pass = num_balls[sender]  # 가지고 있는 공의 개수를 초과하는 경우 모든 공을 패스

        num_balls[sender] -= num_to_pass  # 패스하는 사람으로부터 공을 감소
        num_balls[receiver] += num_to_pass  # 받는 사람에게 공을 증가

    return num_balls

# 人数を取得
N = int(input())

# 各人が最初に持っているボールの個数を取得
initial_balls = []
for _ in range(N):
    ball_count = int(input())
    initial_balls.append(ball_count)

# パス回しの情報の数を取得
M = int(input())

# パス回しの情報を取得
passing_info = []
for _ in range(M):
    pass_data = input().split()
    sender = int(pass_data[0])
    receiver = int(pass_data[1])
    num_to_pass = int(pass_data[2])
    passing_info.append([sender, receiver, num_to_pass])

# ボールのパス回しをシミュレーション
result = ball_passing(initial_balls, passing_info)

# 最終的なボールの個数を出力
for ball_count in result:
    print(ball_count)