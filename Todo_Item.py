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
