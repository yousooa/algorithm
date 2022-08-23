# 정수 n이 입력되면 00시 00분 00초 ~ N시 59분 59초까지
# 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램

h = int(input())
count = 0

for i in range(h+1):
  for m in range(60):
    for s in range(60):
      if '3' in str(i) + str(m) + str(s):
        count += 1

print(count)

# 완전 탐색 문제: 가능한 경우의 수를 모두 검사해보는 탐색 방법