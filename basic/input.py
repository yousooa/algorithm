# map() : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
# ex) list(map(int, input().split()))

data = list(map(int, input().split()))

data.sort()
print(data)

a, b, c = map(int, input().split())
print(a, b, c)

# 사용자로부터 입력을 최대한 빨리 받아야 하는 경우 -> sys라이브러리에 sys.stdin.realine() 이용, 단 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 사용
import sys
data = sys.stdin.readline().rstrip()

print(data)

# end
print("7", end = " ")
print("6", end = " ")

# f
answer = 7
print(f"정답은 {answer}입니다.")