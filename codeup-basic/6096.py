# 2차원 배열 생성
my_pan = [0 for _ in range(19)]
for i in range(19):
    my_pan[i] = list(map(int,input().split()))

# 좌표 입력
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if my_pan[x-1][j] == 0:
            my_pan[x-1][j] = 1
        else:
            my_pan[x-1][j] = 0
        if my_pan[j][y-1] == 0:
            my_pan[j][y-1] = 1
        else:
            my_pan[j][y-1] = 0

# 출력
for i in range(19):
    for j in range(19):
        print(my_pan[i][j], end = " ")
    print()


# 다른 풀이 - bool -> int
my_pan = [0 for _ in range(19)]
for i in range(19):
    my_pan[i] = list(map(int,input().split()))

# 좌표 입력
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        my_pan[x-1][j] = int(not bool(my_pan[x-1][j]))
        my_pan[j][y-1] = int(not bool(my_pan[j][y-1]))

# 출력
for i in range(19):
    for j in range(19):
        print(my_pan[i][j], end = " ")
    print()