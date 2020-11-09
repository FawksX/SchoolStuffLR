
valueList = [24, 13, 57, 45]

result = 0
index = 0

for index in range(3):
    index = index + 1
    if result < valueList[index]:
        result = valueList[index]

print(result)