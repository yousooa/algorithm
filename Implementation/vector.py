# 동 북 서 남
# x는 세로축 y는 가로축
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x = 2
y = 2

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)

# 예제
# (1, 1)에서 시작
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(4):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
print(x, y)