# 약수의 합
# 2로 나누면 성능 좋아짐
def solution(n):
  return sum([i for i in range(1, n // 2 + 1) if n % i == 0])

print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))