"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import os.path
from src.exceptions import *
from src.item import Item

filename = os.path.join("..", "src", "items.csv")

@pytest.fixture
def some_item():
    return Item("Товар", 10, 25)


def test_item_init(some_item):
    assert some_item.name == "Товар"
    assert some_item.price == 10
    assert some_item.quantity == 25
    assert isinstance(some_item.all[0], Item)


def test_item_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 250


def test_item_apply_discount(some_item):
    some_item.pay_rate = 0.5
    some_item.apply_discount()
    assert some_item.price == 5


def test_item_protected_setter_getter(some_item):
    some_item.name = "Новый товар"
    assert some_item.name == "Новый това"


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv(filename)
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_str_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_magic_method_repr(some_item):
    assert repr(some_item) == "Item('Товар', 10, 25)"


def test_magic_method_repr(some_item):
    assert str(some_item) == "Товар"


def test_magic_method_add(some_item):
    assert some_item + some_item == 50
    with pytest.raises(TypeError) as err:
        some_item + 25
    assert str(err.value) == "Можно складывать только один товар с другим"


def test_exceptions():
    """ПРОШУ ПОМОЩИ
    при отсутствии файла или повреждённом файле ошибки появляются, всё как положено, я проверял.
    Но как их тестировать? Что я сделал не так?"""

    with pytest.raises(FileNotFoundError) as err:
        Item.instantiate_from_csv('')
    assert "Отсутствует файл item.csv" in str(err.value)
    with pytest.raises(InstantiateCSVError) as er:
        Item.instantiate_from_csv('test_items.csv')
    assert "Файл item.csv поврежден" in str(er.value)