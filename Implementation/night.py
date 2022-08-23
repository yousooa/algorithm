# 체스판 8x8
# 나이트는 말을 타고 있기 때문에 이동은 L자 형태
# 정원 밖으로 나갈 수 x
# 1. 수평 2칸 -> 수직 1칸  ----> 4가지 경우
# 2. 수직 2칸 -> 수평 1칸  ----> 4가지 경우
# 나이트 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수 출력
# 행 위치 표현 1~8 열 위치 표현 a~h

location = input()
plans = [[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[1,-2],[-1,2],[1,2]]

columnType = ['a','b','c','d','e','f','g','h']

x = int(location[1])
y = columnType.index((location[0])) + 1
print(y)

# y좌표 쉽게 구하는 법
y = int(ord(location[0]) - ord('a')) + 1
print(y)
count = 0
for i in range(8):
  nx = x + plans[i][0]
  ny = y + plans[i][1]
  
  if nx < 1 or nx > 8 or ny < 1 or ny > 8:
    continue

  count += 1

print(count)
