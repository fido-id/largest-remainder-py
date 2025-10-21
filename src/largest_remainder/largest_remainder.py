"""
Largest Remainder (Hamilton method) algorithm for rounding numbers while preserving the total.

Main API:
- LargestRemainder.round(data, total=100)

Supports:
- list[float] → list[int]
- dict[key, float] → dict[key, int]
"""

from __future__ import annotations

import math
from typing import TypeVar, overload

T = TypeVar("T")


class LargestRemainder:
    @staticmethod
    def _largest_remainder_round(values: list[float], total: int = 100) -> list[int]:
        if not values:
            if total == 0:
                return []
            raise ValueError("sum of values is zero, but total is not")

        if any(v < 0 for v in values):
            raise ValueError("all values must be non-negative")

        values_sum = sum(values)
        if values_sum == 0 and total != 0:
            raise ValueError("sum of values is zero, but total is not")

        if values_sum != 0:
            scale = total / values_sum
            values = [v * scale for v in values]

        floors = [math.floor(v) for v in values]
        remainders = [v - f for v, f in zip(values, floors)]
        diff = int(round(total - sum(floors)))

        order = sorted(range(len(values)), key=lambda i: remainders[i], reverse=True)
        for i in order[:diff]:
            floors[i] += 1

        return floors

    @staticmethod
    @overload
    def round(data: list[float], total: int = 100) -> list[int]: ...
    @staticmethod
    @overload
    def round(data: dict[T, float], total: int = 100) -> dict[T, int]: ...

    @staticmethod
    def round(data: list[float] | dict[T, float], total: int = 100) -> list[int] | dict[T, int]:
        if not isinstance(total, (int, float)):
            raise TypeError("the total must be a number")
        if total < 0:
            raise ValueError("the total must be non-negative")

        if isinstance(data, dict):
            if not data:
                return {}
            keys = list(data.keys())
            values = list(data.values())
            rounded_values = LargestRemainder._largest_remainder_round(
                values=values,
                total=int(total),
            )
            return dict(zip(keys, rounded_values))
        elif isinstance(data, list):
            return LargestRemainder._largest_remainder_round(values=data, total=int(total))
        else:
            raise TypeError("Input must be a list or a dictionary")
