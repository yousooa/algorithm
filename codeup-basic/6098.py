# 내가 푼 문제
# 개미굴 생성
gul = [0 for _ in range(10)]

for i in range(10):
    gul[i] = list(map(int, input().split()))

# 이동
# x, y 좌표
x = 1
y = 1

# 1) or 2) or 3) -> Stop
# 1) gul[x][y] = 2
# 2) x=8 and y=8
# 3) gul[x][y+1] = 1 and gul[x+1][y] = 1
while (gul[x][y] != 2) and (x != 8 or y != 8) and (gul[x][y+1] != 1 or gul[x+1][y] != 1):
    gul[x][y] = 9
    # 오른쪽에 벽 없음 -> 오른쪽로 이동
    if gul[x][y+1] != 1:
        y += 1
    # 오른쪽에 벽 -> 아래쪽 이동
    elif gul[x+1][y] != 1:
        x += 1
gul[x][y] = 9

# 출력
for i in range(10):
    for j in range(10):
        print(gul[i][j], end = " ")
    print()