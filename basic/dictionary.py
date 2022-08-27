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
# 튜플 형태로 키와 값이 쌍을 이루어 리스트가 반환
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

# get 메서드
# 딕셔너리에 존재하는 키인지 아닌지 여부에 따라 처리
# counts.get(name, 0): counts 딕셔너리에 name이라는 키가 존재할 경우 name에 대한 값을 불러오고 아닐 경우 counts 딕셔너리에 name이라는 키에 0이라는 값을 갖는 데이터를 추가하라는 의미
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

# 정렬하기
c = {'b':1, 'a':10, 'c':22}

# 키를 기준으로 정렬하기
print(sorted(c.items()))

# 값을 기준으로 정렬하기
tmp = list()
for k, v in c.items():
    tmp.append((v,k))

tmp = sorted(tmp)
print(tmp)
    

