# for + if: for문 뒤에 조건을 적는다.
# if condition에 해당하는 값만 출력
a = list(range(10,20))

for i in a:
    if i == 12:
        print(i) # 12

print([i for i in a if i == 12]) # [12]

# for + if else: for문 앞에 조건을 적는다.
# for문에 해당하는 각각 원소가 if condition에 해당하는지, 아닌지
for i in a:
    if i == 12:
        print(i)
    else:
        print("no")

print([i if i == 12 else "no" for i in a])