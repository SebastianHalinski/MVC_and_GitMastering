from controler import*
import os


def starting_scereen():
    print("""Hello!!!
Choose Your option:
(1) to Add TODO Item
(2) to Modify Item
(3) to Mark Iteam as done
(4) to Delete Item
(5) to Display Item's list
(6) to Display specyfic info about items
(0) to Exit""")


def modify_items(items):
    print("""(1) to Modify name
(2) to Modify description""")
    user_input = input('Your option: ')
    if user_input == '1':
        changing_name(items)
    elif user_input == '2':
        changing_description(items)


def user_option_choice():
    possible_choice = ['1', '2', '3', '4', '5', '6', '0']
    while True:
        user_input = input('Your option: ')
        if user_input in possible_choice:
            return user_input


def main():
    items = ItemList()
    file_name = 'todo_items.txt'
    items.import_data(file_name)
    while True:
        os.system('clear')
        starting_scereen()
        user_input = user_option_choice()
        if user_input == '1':
            os.system('clear')
            add_item(items)
        elif user_input == '2':
            os.system('clear')
            print(get_todo_items_table(items))
            modify_items(items)
        elif user_input == '3':
            os.system('clear')
            print(get_todo_items_table(items))
            mark_item_if_done(items)
        elif user_input == '4':
            os.system('clear')
            print(get_todo_items_table(items))
            delete_item(items)
        elif user_input == '5':
            os.system('clear')
            print(get_todo_items_table(items))
            input('Enter to continue')
        elif user_input == '6':
            os.system('clear')
            print(get_todo_items_table(items))
            get_specyfic_info_of_todoitem(items)
            input('Enter to continue')
        elif user_input == '0':
            items.export_data(file_name)
            exit()


if __name__ == "__main__":
    main()
