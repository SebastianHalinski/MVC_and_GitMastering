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


def changing_name(items):
    index_item_to_change_name = int(input('witch item name You want to change?: '))
    item_to_change_name = items.item_data[index_item_to_change_name]
    item_to_change_name.name = set_name()


def changing_description(items):
    index_of_item = int(input('witch item name You want to change?: '))
    item_to_change = items.item_data[index_of_item]
    item_to_change.description = set_description()


def delete_item(items):
    index_of_item = int(input('select item to delete by index: '))
    del items.item_data[index_of_item]


def mark_item_if_done(items):
    index_of_item = int(input('witch item is dome by index?: '))
    items.item_data[index_of_item].is_done = True
