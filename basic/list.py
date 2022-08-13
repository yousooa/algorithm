# slicing
# 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1 : 4])

array = [i + 1 for i in range(10)]
print(array)

array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i * i for i in range(1, 10)]
print(array)

# 2차원 리스트
# good
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

# bad
n = 4
m = 3
# 전체 리스트 안에 포함된 각 리스트가 모두 [[0] * m] 
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)

# 리스트 원소 삽입
a = [3, 1, 4]
a.append(2)
print("삽입: ", a)

# 오름차순 정렬
# 본체의 리스트를 정렬해서 변환
a.sort()
print("오름차순 정렬: ", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: ", a)

# 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)

# list에 여러 요소 한 번에 추가
a = [1,2,3,4,5]
b = [6,7,8,9,10]
# 방법 1)
a.extend(b)
print(a)
# 방법 2)
print(a + b)