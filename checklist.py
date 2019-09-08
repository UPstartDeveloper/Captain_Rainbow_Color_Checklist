import os
checklist = list()


# CREATE
def create(item):
    checklist.append(item)


# READ
def read(index):
    index = int(index)
    item = checklist[index]
    return item


# UPDATE
def update(index, item):
    checklist[int(index)] = item


# DESTROY
def destroy(index):
    checklist.pop(int(index))


# LIST ALL ITEMS
def list_all_items():
    index = 0
    for checklist_item in checklist:
        print("\033[1;33;40m{} {}\x1b[0m".format(index, checklist_item))  # yellow text
        index += 1


# MARKS ITEMS COMPLETE
def mark_completed(index):
    update(index, "{}{}".format("√", checklist[int(index)]))


# UNCHECKS ITEMS
def uncheck_item(index):
    update(int(index), read(index)[1:])


# SELECT
def select(function_code):
    function_code = function_code.upper()  # makes string comparing case insensitive
    # Create item
    if function_code == "C":
        input_item = input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = input("Index Number? ")

        # Remember that item_index must actually exist or our program crashes
        print("\033[1;33;40m{}\x1b[0m".format(read(item_index)))

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Update an item in the list
    elif function_code == "U":
        item_index = input("Enter the index of the item to be updated: ")
        item_update = input("Please enter what the item should say instead: ")
        update(item_index, item_update)
        print("\033[1;32;40m{}\x1b[0m".format("Item has been updated."))

    # Delete an item from the list
    elif function_code == "D":
        item_index = input("Enter index number of the item to be deleted: ")
        destroy(item_index)
        print("\033[1;31;40m{}\x1b[0m".format("Item has been deleted."))

    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True


# PROMPT THE USER
def user_input(prompt):
    # display a message in terminal and wait for input by user
    user_input = input(prompt)
    return user_input


# TEST
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    # print(read(1))
    list_all_items()

    select("C")
    list_all_items()

    select("R")
    list_all_items()

    user_value = user_input("Please Enter a value: ")
    print(user_value)


'''
# Run tests
test()
# Run tests for mark_completed and uncheck_item
num = input("Enter a number to check: ")
mark_completed(num)
list_all_items()
num = input("Enter the same number to uncheck: ")
uncheck_item(num)
list_all_items()
'''
running = True
while running:
    os.system('clear')  # clears terminal
    selection = user_input(
        "Press C to add to list, \n" +
        "R to Read from list, \n" +
        "P to display list, \n" +
        "U to update an item on the list \n" +
        "D to delete an item from the list \n" +
        "and Q to quit: ")
    running = select(selection)
