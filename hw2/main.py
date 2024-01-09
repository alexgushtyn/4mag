import csv

class Item:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self._name = value[:10]
        else:
            self._name = value

    @staticmethod
    def string_to_number(number_string):
        try:
            number = int(number_string)
            return number
        except ValueError:
            raise ValueError("Invalid input")

    @classmethod
    def instantiate_from_csv(cls):
        with open("src/items.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                item_name = row["name"]
                quantity = cls.string_to_number(row["quantity"])
                price = float(row["price"])