import csv
from src.exceptions import InstantiateCSVError
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    items_list_file = os.path.join("..", "src", "items.csv")

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise TypeError("Можно складывать только один товар с другим")
        return self.quantity + other.quantity


    @staticmethod
    def string_to_number(string):
        return int(string.split('.')[0])


    @classmethod
    def instantiate_from_csv(cls, csv_filename=items_list_file):
        """
        Инициализирует экземпляры класса из csv файла.


        :csv_filename: Адрес файла csv
        """

        try:
            with open(csv_filename, newline='\n') as csv_file:
                reader = csv.DictReader(csv_file)
                try:
                    for row in reader:
                        if len(row) != 3:
                            raise InstantiateCSVError
                        print(row)
                        print(cls.all)
                        print(row["name"], float(row["price"]), int(row["quantity"]))
                        cls(row["name"], float(row["price"]), int(row["quantity"]))
                except InstantiateCSVError as err:
                    print(err.message)
        except FileNotFoundError:
            print('_Отсутствует файл item.csv_')


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """
        Если длина названия больше 10 символов - лишние обрезаются.

        :name: Имя товара.
        """
        self.__name = name[:10] if len(name) > 10 else name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

a = Item.instantiate_from_csv("../tests/test_items.csv")