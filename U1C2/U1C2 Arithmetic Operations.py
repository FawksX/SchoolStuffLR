

def addTotal(amount):
    ints = []
    for x in range(amount):
        getInt = int(input("Input an integer (" + str(int(len(ints)+1)) + "/" + str(amount) + "): "))
        ints.append(getInt)
    total = sum(ints)
    print(total)


def multiplyTotal(amount):
    ints = []
    for x in range(amount):
        getInt = int(input("Input an integer (" + str(int(len(ints)+1)) + "/" + str(amount) + "): "))
        ints.append(getInt)
    total = 1
    for x in ints:
        total *= x
    print(total)

def calculateVolume():
    width = int(input("Width of pool: "))
    height = int(input("Height of pool: "))
    length = int(input("Length of pool: "))
    volume = width * height * length
    print("Volume: " + volume)

addTotal(3)
multiplyTotal(2)
calculateVolume()

