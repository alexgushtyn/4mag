from src.item import Item

class Keyboard_langswich:
    __language = 'EN'

    def change_lang(self):
        self.__language = 'ENRU'.replace(self.__language, '')

    @property
    def language(self):
        return self.__language


class Keyboard(Item, Keyboard_langswich):
    __language = 'EN'
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)