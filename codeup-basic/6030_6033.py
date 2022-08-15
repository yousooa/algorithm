# chr() : 정수값 -> 문자
# ord() : 문자 -> 정수값

# 6030
# 영문자 1개 입력받아 십진수로 출력
n = ord(input())
print(int(n))

# 6031
# 10진 정수를 입력받아 유니코드 문자로 출력
n = int(input())
print(chr(n))

# 6033
# 문자 1개를 입력받아 다음 문자 출력하기
n = ord(input())
print(chr(n+1))