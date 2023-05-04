from list_helper import *

# shopping choices
groceries = ["tomatoes", "lettuce", "bananas", "apples"]
clothes = ["t-shirts", "levis", "jackets", "hoodies"]
electronics = ["4k tv", "dell", "apple iphone", "samsung"]
books = ["national geographic", "lord of the rings", "divergent", "the bible"]

print_lists(groceries, clothes, electronics, books)
shopping_list = []

# ask user to create personal list
done = False
while done:
    item = input("Enter an item you would like to purchase into a shopping list (enter \"done\" when you would like to stop): ")
    if item == "done":
        break
    category = input("Enter the category that item falls into: ")
    create_user_list(category, item, shopping_list, False)

# print final list
print_shopping_list(shopping_list)

# ask user about removing an item
remove = input("Would you like to remove an item from this list? ")
if remove == "yes":
    index = input("Which item would you like to remove? ")
    if index != shopping_list:
        print("Error, this item doesn't exist on your shopping list")
    else:
        remove_list_item(shopping_list, index)

# ask user if they want to search list
index = input("Which item would you like to search for? ")
category = input("What category is the item? ")
search_list_item(index, shopping_list, category)
if index == "":
    print("Error item doesn't exist in this list")