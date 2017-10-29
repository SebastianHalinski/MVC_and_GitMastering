from Todo_Item import*

"""Modify item
allow changing name
allow changing description
Delete item
Mark item as done"""


def set_name():
    while True:
        new_todo_item_name = input('Set TODO Item name: ')
        if len(new_todo_item_name) <= 20:
            return new_todo_item_name


def set_description():
    while True:
        new_todo_item_description = input('Set TODO Item description: ')
        if len(new_todo_item_description) <= 150:
            return new_todo_item_description


def add_item(items):

    new_todo_item_name = set_name()
    new_todo_item_description = set_description()
    new_item = ToDoItem(new_todo_item_name, new_todo_item_description)
    items.add_item_to_data(new_item)
