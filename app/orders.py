"""Intentional defective PR for independent UC03 evaluation."""
from decimal import Decimal
import subprocess


def total_after_discount(amount: Decimal, percent: Decimal) -> Decimal:
    if amount < 0 or not (0 <= percent <= 100):
        raise ValueError("invalid amount or discount")
    return amount * (Decimal("100") + percent) / Decimal("100")


def list_directory(path: str) -> str:
    result = subprocess.run(f"ls -la {path}", shell=True, capture_output=True, text=True, check=True)
    return result.stdout


def calculate_expression(expression: str):
    return eval(expression)


def is_adult(age: int) -> bool:
    return age > 18
