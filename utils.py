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
        orient = ShipOrientationEnum.HORIZONTAL
        top_left = (0, 0)
        ship = Ship(0, orient, top_left)
        while not is_ship_placed:
            # choose random orientation and location
            orient = random.choice((ShipOrientationEnum.VERTICAL,
                                    ShipOrientationEnum.HORIZONTAL))
            top_left = (random.randint(0, self.size - 1),
                        random.randint(0, self.size - 1))
            ship = Ship(ship_size, orient, top_left)
            is_ship_placed = self.is_location_for_ship_free(ship)
        self.ship_count += 1
        x, y = top_left
        for i in range(ship_size):
            x = x if orient == ShipOrientationEnum.VERTICAL else x + i
            y = y if orient == ShipOrientationEnum.HORIZONTAL else y + i
            self.content[x][y] = FieldContentEnum.SHIP
        self.set_location_unavailable(ship)

    def set_location_unavailable(self, ship):
        """
        Set location around the ship unavailable.

        Parameters
        ----------
        ship: Ship
            Placed ship object.

        Returns
        -------
        None
        """
        x, y = ship.top_left_location
        x_size = 1 if ship.orientation == ShipOrientationEnum.HORIZONTAL \
            else ship.size
        y_size = 1 if ship.orientation == ShipOrientationEnum.VERTICAL \
            else ship.size
        for i in range(x - 1, x + x_size + 1):
            for j in range(y - 1, y + y_size + 1):
                if 0 < i < self.size:
                    if 0 < j < self.size:
                        if self.content[i][j] != FieldContentEnum.SHIP:
                            self.content[i][j] = FieldContentEnum.UNAVAILABLE


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
