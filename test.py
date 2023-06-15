def dilation(image):
    H = len(image)
    W = len(image[0])
    result = [["."] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if image[i][j] == "#":
                result[i][j] = "#"
                if i > 0:
                    result[i - 1][j] = "#"
                if i < H - 1:
                    result[i + 1][j] = "#"
                if j > 0:
                    result[i][j - 1] = "#"
                if j < W - 1:
                    result[i][j + 1] = "#"

    return result


def erosion(image):
    H = len(image)
    W = len(image[0])
    result = [["."] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if image[i][j] == "#":
                if i > 0 and image[i - 1][j] == "#":
                    result[i][j] = "#"
                if i < H - 1 and image[i + 1][j] == "#":
                    result[i][j] = "#"
                if j > 0 and image[i][j - 1] == "#":
                    result[i][j] = "#"
                if j < W - 1 and image[i][j + 1] == "#":
                    result[i][j] = "#"

    return result


def process_image(image, operations):
    for op in operations:
        if op == "D":
            image = dilation(image)
        elif op == "E":
            image = erosion(image)

    return image


# 入力受け取り
H, W, N = map(int, input().split())
image = []
for _ in range(H):
    row = list(input().strip())
    image.append(row)
operations = input().strip()

# 画像処理の実行
output_image = process_image(image, operations)

# 結果の出力
for row in output_image:
    print("".join(row), flush=True)