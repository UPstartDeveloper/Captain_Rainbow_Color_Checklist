checklist = list()


# CREATE
def create(item):
    checklist.append(item)


# READ
def read(index):
    print(checklist[index])


# UPDATE
def update(index, item):
    checklist[index] = item


# DESTROY
def destroy(index):
    checklist.pop(index)


# LIST ALL ITEMS
def list_all_items():
    for item in list:
        print(item)


# TEST
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1))


test()
