class Item:
    def __init__(self, name: str, bonusHealth: int) -> None:
        self._name = name
        self._bonusHealth: int = bonusHealth