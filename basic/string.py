# lstrip(): 왼쪽 공백 제거
# rstrip(): 오른쪽 공백 제거
# strip(): 오른쪽 왼쪽 공백 제거

greet = '                     Hello Bob       '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

# 시작 문자열 찾기 - True/ False
line = 'Please have a nice day'

print(line.startswith('Please')) # T
print(line.startswith('p')) # F

# find(): 첫번째 문자 위치 출력
print(line.find('e'))

# string[start:end:step]
letters = 'qwerasdfzxcv'
print(letters[:-4]) # qwerasdf
print(letters[-4:]) # zxcv
