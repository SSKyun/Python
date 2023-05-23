test = input("두 개의 변수를 띄어쓰기로 입력하세요: ")
N, M = map(int, test.split())

if 8 <= N <= 50 and 8 <= M <= 50:
    is_alternating = True  # BW가 번갈아 나오는지 여부를 판단하는 변수

    for _ in range(N):
        row = input("한 줄을 입력하세요: ")
        
        # BW가 번갈아 나오는지 확인
        if is_alternating and row[0] != row[1] and all(row[i] != row[i+1] for i in range(1, M-1, 2)):
            print("OK")
        else:
            print("err")

        # BW가 번갈아 나오는지 여부 갱신
        is_alternating = not is_alternating

else:
    print("err")