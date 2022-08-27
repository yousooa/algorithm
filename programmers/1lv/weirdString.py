# 이상한 문자 만들기

# 힌트
s = "    easefsd   sefasfsd   "
a = s.split()
b = s.split(" ")
print(a) # ['easefsd', 'sefasfsd']
print(b) # ['', '', '', '', 'easefsd', '', '', 'sefasfsd', '', '', ''] 공백까지 인식

y = "asddf"
for i, j in enumerate(y):
    print(i, j)
# 0 a
# 1 s
# 2 d
# 3 d
# 4 f

def solution(s):
    return ' '.join(map(lambda x: ''.join([a.upper() if idx % 2 == 0 else a.lower() for idx, a in enumerate(x)]), s.split(" ")))