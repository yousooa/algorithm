# 비트 단위 연산자
# 6059
# ~ : bitwise not
# ~n = - n - 1
a = int(input())
print(~a)

# 6060
# & : bitwise and
a, b = map(int, input().split())
print(a&b)

# 6061
# | : bitwise or
a, b = map(int, input().split())
print(a|b)

# 6062
# ^ : bitwise xor
a, b = map(int, input().split())
print(a^b)