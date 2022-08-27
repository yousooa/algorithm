# 정수 제곱근 판별
# https://school.programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    sqrt = n ** (1/2)
    return (sqrt + 1) ** 2 if sqrt % 1 == 0 else -1

n = 118372
print(list(map(int, str(n))))

