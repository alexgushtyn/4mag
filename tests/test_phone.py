
import pytest
from src.phone import Phone


@pytest.fixture
def some_phone():
    return Phone("Нокийя", 10, 25, 2)


def test_phone_init(some_phone):
    assert some_phone.name == "Нокийя"
    assert some_phone.price == 10
    assert some_phone.quantity == 25
    assert some_phone.number_of_sim == 2