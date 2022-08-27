# 에라토스테네스의 체
# 1)
def solution(n):
    sosu = [True] * (n + 1)
    # 0과 1은 소수가 아니다.
    sosu[0] = False
    sosu[1] = False

    for i in range(2, n + 1):
        if sosu[i]  == True:
            j = 2
            # i 배수 소수 아님
            while i*j <= n:
                sosu[i*j] = False
                j += 1
    count = 0
    for i in range(len(sosu)):
        if sosu[i] == True:
            count += 1
    print(count)

# 2)
def solution(n):
    sosu = set(range(2, n + 1))
    for i in range(2, n+1):
        sosu -= set(range(2*i,n+1,i))
    return len(sosu)