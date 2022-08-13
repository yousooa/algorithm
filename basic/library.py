result = sum([1, 2, 3, 4, 5])
print(result) # 15

min_res = min([1, 2, 3, 4, 5])
max_res = max([1, 2, 3, 4, 5])
print(min_res, max_res) # 1 5

result = eval("(3+5)*2")
print(result) # 16

# 순열
from itertools import combinations_with_replacement, count, permutations
from math import prod
from traceback import print_tb
data = ['A', 'B', 'C']

result = list(permutations(data,2))
print(result)

# 조합
from itertools import combinations
result = list(combinations(data, 2))
print(result)

# 중복 순열과 중복 조합
# 중복 순열
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)

# 중복 조합
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))
print(result)

# 등장 횟수 세는 기능
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(counter)
print(dict(counter))

# 최대 공약수, 최소 공배수
import math

def lcm(a, b):
  return a * b // math.gcd(a, b)

print(math.gcd(21, 14))
print(lcm(14,21))