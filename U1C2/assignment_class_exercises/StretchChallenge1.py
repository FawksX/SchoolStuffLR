

def calculateArea(length, width, border):
    if border == 0:
        areaNoBorder = length * width
        return areaNoBorder
    elif border == 1:
        areaWithBorder = length+border * width+border
        return areaWithBorder

def turfCost(area):
    return str(area*10)


if __name__ == "__main__":
    length = int(input("Length of Garden (m): "))
    width = int(input("Width of Garden (m): "))
    border = int(input("Border (0 if no border) (m): "))
    print("Area of Garden: " + str(calculateArea(length, width, border)))
    print("Cost of Turf: " + str(turfCost(calculateArea(length, width, border))))
