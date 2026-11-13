from decimal import Decimal
from app.orders import total_after_discount, is_adult


def test_discount():
    assert total_after_discount(Decimal("100"), Decimal("20")) == Decimal("80")


def test_adult_boundary():
    assert is_adult(18)
    assert not is_adult(17)
