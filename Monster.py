from Character import Character

class Monster(Character):
    def __init__(self) -> None:
        super().__init__(0, 0, '🐖')
    
    @property
    def x_position(self) -> int:
        return self._x_position
    
    @property
    def y_position(self) -> int:
        return self._y_position
    
    @property
    def emoji(self) -> int:
        return self._emoji

    def move(self, direction: str) -> None:
        pass

    def attack(self, target: 'Character') -> None:
        pass

    def getEmoji(self):
        return self._emoji