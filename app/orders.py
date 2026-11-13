"""Order processing baseline with intentionally safe implementation."""
from decimal import Decimal
import subprocess


def total_after_discount(amount: Decimal, percent: Decimal) -> Decimal:
    if amount < 0 or not (0 <= percent <= 100):
        raise ValueError("invalid amount or discount")
    return amount * (Decimal("100") - percent) / Decimal("100")


def list_directory(path: str) -> str:
    result = subprocess.run(["ls", "-la", path], capture_output=True, text=True, check=True)
    return result.stdout


def is_adult(age: int) -> bool:
    return age >= 18
