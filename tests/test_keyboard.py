
import pytest
from src.keyboard import Keyboard


@pytest.fixture
def some_keyboard():
    return Keyboard("Логитеч", 10, 25)


def test_keyboard(some_keyboard):
    assert some_keyboard.name == "Логитеч"
    assert some_keyboard.price == 10
    assert some_keyboard.quantity == 25
    assert some_keyboard.language == 'EN'
    some_keyboard.change_lang()
    assert some_keyboard.language == 'RU'