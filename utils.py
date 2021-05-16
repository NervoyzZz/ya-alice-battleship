# Copyright 2021 Daniil O. Nepryakhin [NervoyzZz]
# Licensed under the Apache License, Version 2.0

from enum import Enum


class FieldContentEnum(Enum):
    """Enum class to describe each grid of the field content."""
    EMPTY = 0
    SHIP = 1
    UNKNOWN = 2
    UNAVAILABLE = 3


class ShipOrientationEnum(Enum):
    """Enum to describe possible orientations of the ships."""
    HORIZONTAL = 0
    VERTICAL = 1


class Field:
    """Class to describe battle fields."""
    def __init__(self, size=10):
        """
        Method to init `Field` class.

        Parameters
        ----------
        size: int
            Optional. Size of the field. Field is a square of the `size`.
        """
        self.size = size
        self.ship_count = 0
        self.content = [
            [FieldContentEnum.EMPTY for j in range(size)]
            for i in range(size)
        ]


class Ship:
    """Class to describe ship object."""
    def __init__(self, size, orientation, top_left_location):
        """
        Method to init `Ship` class.

        Parameters
        ----------
        size: int
            Size of the ship.
        orientation: ShipOrientationEnum
            Orientation of the ship.
        top_left_location: Tuple
            Location of the top left chunk of the ship.
            Indexes of corresponding Field object.
        """
        self.size = size
        self.health = size
        self.orientation = orientation
        self.top_left_location = top_left_location
