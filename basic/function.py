# global 키워드로 변수를 지정하면 해당 함수에서 지역 변수를 만들지 않고, 함수 바깥에 선언도니 변수를 바로 참조

a = 0

def func():
    global a # 전역변수 참조
    a += 1

for i in range(10):
    func()

print(a)

# list
array = [1, 2, 3, 4]

def func():
    array.append(5)
    print(array)

func()

# 전역변수, 지역변수
array = [1, 2, 3, 4]

def func():
    array = [3, 4, 5]
    array.append(6)
    print(array)

func() # 3, 4, 5, 6
print(array) # 1, 2, 3, 4

# 여러 개의 반환 값을 가질 수 있다.
def operator(a, b):
    add_res = a + b
    sub_res = a - b
    mul_res = a * b
    div_res = a / b
    return add_res, sub_res, mul_res, div_res

a, b, c, d = operator(3, 7)
print(a, b, c, d)

# 람다 표현식
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

# sorted(정렬할 데이터, key, reverse)
# 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환
print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)
print(list(result))