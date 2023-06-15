N = int(input())  # プレイヤー数を取得
cards = input().split()  # カードの入力を受け取り、リストに分割

m_Card = max(cards, key=lambda x: int(x) if x != "x10" else 0)  # 点数カードの中で最大の点を持つカードを取得
result = sum([int(card) if card != "x10" else 0 for card in cards])  # 点数カードの合計点を計算

if "0" in cards:
    result -= int(m_Card)  # 点数 0 カードがある場合、最大の点を持つカードを 0 点にする

if "x10" in cards:
    result *= 10  # 点数 10 倍カードがある場合、総合点を 10 倍する

print(result)  # 総合点を出力