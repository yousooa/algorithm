# enumerate: 열거하다
# list, tuple, string 등 여러가지 자료형을 입력받으면 인덱스 값을 포함하는 enumverate 객체를 돌려준다.
a = ['ac', 'b', 'c']
print(list(enumerate(a)))
print(dict(enumerate(a)))

# 인덱스 시작 값 설정
for i in enumerate(a, start=1):
  print(i)