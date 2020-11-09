

# Could fetch from a csv file in a 2D Array to also fetch the students other data. However, in this case I am not and am hard storing the names in this list
names = ["Bob", "Dylan", "Felix", "Rodger", "Sam", "Charlie", "Violet", "Henry"]


def displayStudents(list):
    print("Students: ")
    for x in range(len(list)):
        print(x+1, ": " + str(list[x]))


def changeName(list, name, newName):
    for x in range(len(list)):
        if list[x].lower() == name.lower():
            list[x] = newName
            print("Name Successfully Changed!")


if __name__ == "__main__":
    while True:
        decision = int(input("Choose a task:\n1. Display Names\n2. Change a Students Name\n3: Exit\nAnswer: "))
        if decision == 1:
            displayStudents(names)
        elif decision == 2:
            changeName(names,
                       input("Choose a name to change: "),
                       input("Choose a new name for the student: ")
                       )
        elif decision == 3:
            exit()
        else:
            print("Not a valid option!")

