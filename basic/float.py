# 실수 정보를 표현하는 정확도에 한계를 가진다.
a = 0.3 + 0.6
print(a) # 0.8999999999999999
if a == 0.9:
    print(True)
else:
    print(False) # 실행

# 해결
a = 0.3 + 0.6
print(round(a, 2)) # 0.9
if round(a,2) == 0.9:
    print(True) # 실행
else:
    print(False)