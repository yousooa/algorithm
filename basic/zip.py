# 두 그룹의 데이터를 서로 엮어주는 파이썬 내장 함수
# 여러 개의 iterable 자료형이 개수가 동일할 때 사용
# iterable 자료형의 각각의 요소를 나눈 후 순서대로 묶어서 요소의 개수만큼 새로운 iterable 자료형을 생성
# iterable 자료형: 반복 가능한 자료형 ex) list, tuple

# zip
numbers = [1,2,3]
letters = ['a', 'b', 'c']
for pair in zip(numbers, letters):
    print(pair)

for number, upper, lower in zip('12345','ABCDE','abcde'):
    print(number, upper, lower)

# unzip
numbers = (1,2,3)
letters = ('a', 'b', 'c')
pairs = list(zip(numbers, letters))
print(pairs)
numbers, letters = zip(*pairs)
print(numbers)
print(letters)

# dictionary 만들기
key = [1,2,3]
value = ['a', 'b', 'c']
print(dict(zip(key, value)))

# 프로그래머스 - 행렬의 덧셈
# https://school.programmers.co.kr/learn/courses/30/lessons/12950

# arr1[0] + arr2[0] / arr1[1] + arr2[1]
# arr1[0][0] + arr2[0][0] / arr1[0][1]
def solution(arr1, arr2):
    answer = [ [c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer