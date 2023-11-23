from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, y_position: int, x_position: int, emoji: str) -> None:
        self._y_position: int = y_position
        self._x_position: int = x_position
        self._emoji = emoji
        self._health: int = 100
    
    @abstractmethod
    def move(self, direction: str) -> None:
        pass

    @abstractmethod
    def attack(self, target: 'Character') -> None:
        pass