class Item:

    def __init__(self, name: str, description: str, value: int, view=None):
        self.name = name
        self.description = description
        self.value = value
        self.view = view

    def get_view(self):
        return self.view

    def __str__(self):
        return f"{self.name}({self.description})"
