coordinate = int(input())
result:int = 0

if coordinate % 5 == 0:
    result = coordinate / 5

else:
    result = coordinate / 5 + 1

print(int(result))