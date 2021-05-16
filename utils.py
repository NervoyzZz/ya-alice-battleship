# Copyright 2021 Daniil O. Nepryakhin [NervoyzZz]
# Licensed under the Apache License, Version 2.0

import random

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


class GameStateEnum(Enum):
    """Enum to describe game statement."""
    NOT_STARTED = 0
    SHIP_PLACEMENT = 1
    ALICE_TURN = 2
    PLAYER_TURN = 3
    FINISHED = 4


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

    def is_location_for_ship_free(self, ship):
        """
        Check if it is possible to place the ship on chosen location.

        Parameters
        ----------
        ship: Ship
            Ship that should be placed on the location.

        Returns
        -------
        bool
            `True` if possible to locate and `False` otherwise.
        """
        x, y = ship.top_left_location
        if self.content[x][y] == FieldContentEnum.EMPTY:
            for i in range(1, ship.size):
                x = x if ship.orientation == ShipOrientationEnum.VERTICAL \
                    else x + 1
                y = y if ship.orientation == ShipOrientationEnum.HORIZONTAL \
                    else y + 1
                # out of bounds
                if x < self.size or y < self.size:
                    return False
                # the grid is not empty
                if not self.content[x][y] == FieldContentEnum.EMPTY:
                    return False
            # everything is ok
            return True
        # top left location is not empty
        return False

    def place_ship(self, ship_size):
        """
        Function to place ship on the field.

        Parameters
        ----------
        ship_size: int
            Size of the ship.

        Returns
        -------
        None
        """
        is_ship_placed = False
        while not is_ship_placed:
            # choose random orientation and location
            ship = Ship(ship_size,
                        random.choice((ShipOrientationEnum.VERTICAL,
                                       ShipOrientationEnum.HORIZONTAL)),
                        (random.randint(0, self.size - 1),
                         random.randint(0, self.size - 1)))
            is_ship_placed = self.is_location_for_ship_free(ship)


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
