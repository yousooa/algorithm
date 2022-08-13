data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'

data = {
    '사과': 'apple',
    '바나나': 'banana'
}

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# key와 value 같이 출력
print(data.items())

# key만 출력
print(data.keys())

# value만 출력
print(data.values())

for key in data.keys():
    print(data[key])

# 요소 삭제
# del 이나 pop 이용해서 삭제
# del은 시간이 거의 두배 더 빠름
# dict.pop()은 런타임 오류를 피하는데 도움이 됨
del data['사과']
print(data)
