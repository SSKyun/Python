def count_repaint(board):
    min_count = float('inf')  # 최소 개수를 저장할 변수, 초기값은 무한대로 설정

    # 8x8 크기의 체스판을 모든 가능한 위치에서 탐색
    for i in range(len(board) - 7):
        for j in range(len(board[0]) - 7):
            count_w = 0  # 맨 왼쪽 위가 흰색인 경우 칠해야 하는 개수
            count_b = 0  # 맨 왼쪽 위가 검은색인 경우 칠해야 하는 개수

            # 체스판의 현재 위치에서 8x8 영역을 탐색
            for x in range(i, i + 8):
                for y in range(j, j + 8):
                    if (x + y) % 2 == 0:
                        # (x+y)가 짝수인 경우, 현재 칸이 흰색이어야 함
                        if board[x][y] != 'W':
                            count_w += 1
                        else:
                            count_b += 1
                    else:
                        # (x+y)가 홀수인 경우, 현재 칸이 검은색이어야 함
                        if board[x][y] != 'B':
                            count_w += 1
                        else:
                            count_b += 1

            # 현재 위치에서 다시 칠해야 하는 최소 개수를 갱신
            min_count = min(min_count, count_w, count_b)

    return min_count


# 보드 입력 받기
M, N = map(int, input().split())
board = []
for _ in range(M):
    row = input()
    board.append(row)

# 최소 개수 출력
print(count_repaint(board))