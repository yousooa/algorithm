print((lambda x, y: x+ y)(2, 3))

# map(함수, 리스트): 리스트로부터 원소를 하나씩 꺼내서 함수를 적용 -> 그 결과를 리스트에 추가
print(list(map(lambda x: x ** 2, range(5))))

# filter(함수, 리스트): 리스트에 들어있는 원소들을 함수에 적용시켜 결과가 참인 값들로 새로운 리스트 만들어줌
print(list(filter(lambda x: x < 5, range(10))))