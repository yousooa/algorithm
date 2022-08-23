location = input()
plans = [[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[1,-2],[-1,2],[1,2]]

columnType = ['a','b','c','d','e','f','g','h']

x = int(location[1])
y = columnType.index((location[0])) + 1
print(y)

# y좌표 쉽게 구하는 법
y = int(ord(location[0]) - int(ord('a'))) + 1
print(y)