# Copyright 2021 Daniil O. Nepryakhin [NervoyzZz]
# Licensed under the Apache License, Version 2.0

from enum import Enum


class FieldContentEnum(Enum):
    """Enum class to describe each grid of the field content."""
    EMPTY = 0
    ONE_SHIP = 1
    TWO_SHIP = 2
    THREE_SHIP = 3
    FOUR_SHIP = 4
    UNKNOWN = 5
    UNAVAILABLE = 6


class Field:
    def __init__(self, size=10):
        self.size = size
        self.ship_count = 0
        self.content = [[FieldContentEnum.EMPTY for j in range(size)] for i in range(size)]
