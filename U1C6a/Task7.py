from datetime import datetime

shopping_list = []
finished = False
while not finished:
    shopping_item = input("Enter next item (-1 to end list): ")
    if shopping_item == "-1":
        confirmation = input("Are you sure you want to finish this shopping list? (yes/no): ")
        if confirmation.lower() == "yes":
            finished = True
            date = datetime.now()
            listFileName = "shopping_list{0}.{1}.{2}".format(str(date.day), str(date.month), str(date.year))
            print("Saved shopping list as: " + listFileName)
            file = open(listFileName + ".txt", "a")
            for item in shopping_list:
                file.write(item +"\n")
        elif confirmation.lower() == "no":
            continue
    else:
        shopping_list.append(shopping_item)  # add new item to the list
        print("{0} added to shopping list!".format(shopping_item))

for index in range(len(shopping_list)):
    print("item {0} is {1}".format(index, shopping_list[index]))
