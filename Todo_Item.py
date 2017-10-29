import csv


class ToDoItem():
    """
    Add ToDo item consisting of the following attributes:
    name - string, max 20 characters
    description - string, max 150 characters
    is_done - bool, false by default"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_done = False


class ItemList():

    def __init__(self):
        self.item_data = []

    def add_item_to_data(self, item):
        self.item_data.append(item)
        return self.item_data

    def import_data(self, file_name):
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                name = row[0]
                description = row[1]
                item_status = row[2]
                if item_status == 'True':
                    new_item = ToDoItem(name, description)
                    new_item.is_done = True
                    self.item_data.append(new_item)
                elif item_status == 'False':
                    new_item = ToDoItem(name, description)
                    new_item.is_done = False
                    self.item_data.append(new_item)

    def export_data(self, file_name):
        with open(file_name, 'w') as csvfile:
            for row in self.item_data:
                writer = csv.writer(csvfile)
                to_write = row.name, row.description, row.is_done
                writer.writerow(to_write)
