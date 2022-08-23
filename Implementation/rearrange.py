# 알파벳 대문자 + 숫자(0~9) 문자열 입력
# 모든 알파벳을 오름차순으로 정렬 출력 -> 모든 숫자를 더한 값 출력

myInput = input()
alphabet = []
sum = 0
for x in myInput:
    if x.isalpha():
        alphabet.append(x)
    else:
        sum += int(x)

alphabet.sort()

if sum != 0:
    alphabet.append(str(sum))

print(''.join(alphabet))