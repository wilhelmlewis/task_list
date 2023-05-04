# print lists
def print_lists(list1, list2, list3, list4):
    print(list1)
    print(list2)
    print(list3)
    print(list4)

# create personal shopping list
def create_user_list(category, item, list, done):
    list = []
    list += category[item].append
    if item == done:
        print(list)

# add list items to correct category
def sort_category(category, item):
    for index in range(0, len(category)):
        if category[index] == item:
            category += item.sort
        else:
            continue

# print final list
def print_shopping_list(shopping_list):
    sort_category()
    print(shopping_list)

# remove item from list
def remove_list_item(list, index):
    list.remove(index)

# find and print item within list
def search_list_item(index, list, category):
    for j in range(0, len(category)):
        if j == category:
            for i in range(0, len(list)):
                if i == index:
                    print(index)
                else:
                    continue
        else:
            continue