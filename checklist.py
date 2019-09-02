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
    checklist[index] = item


# DESTROY
def destroy(index):
    checklist.pop(index)


# LIST ALL ITEMS
def list_all_items():
    index = 0
    for checklist_item in checklist:
        print("\033[1;31;40m{} {}\x1b[0m".format(index, checklist_item))
        index += 1


# MARKS ITEMS COMPLETE
def mark_completed(index):
    update(index, "{} {}".format("√", checklist[index]))


# SELECT
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = input("Index Number? ")

        # Remember that item_index must actually exist or our program crashes
        print(read(item_index))

    # Print all items
    elif function_code == "P":
        list_all_items()

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


# Run tests
test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit ")
    running = select(selection)
