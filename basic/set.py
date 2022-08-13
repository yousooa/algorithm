# 집합
# 중복을 허용 x
# 순서 x
# 리스트 혹은 문자열을 이용해서 초기화할 수 있다.
# 데이터 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.

# 집합 초기화 1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 초기화 2
data= {1, 1, 2, 3, 4, 4, 5}
print(data)

# 집합 자료형 관련 함수
data = {1, 2, 3}

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러개 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 합집합
print(a | b)

# 교집합
print(a & b)

# 차집합
print(a - b)