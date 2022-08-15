# 아무것도 처리하고 싶지 않을 때 pass 키워드 사용

# 조건부 표현식(삼항 연산자)
# [true_value] if [condition] else [false_value]
score = 85
result = "success" if score >= 80 else "fail"
print(result)

# 0 < x < 20 가능 그러나 x > 0 and x < 20 이렇게 쓰도록 하자
x = 15
if 0 < x < 20:
    print("x는 0초과 20미만입니다.")