from Character import Character

class Player(Character):
    def __init__(self, y, x) -> None:
        super().__init__(y, x, '👾')
        self._inventory: dict = {}

    @property
    def health(self) -> int:
        return self._health
    
    @property
    def x_position(self) -> int:
        return self._x_position
    
    @property
    def y_position(self) -> int:
        return self._y_position
    
    @property
    def emoji(self) -> str:
        return self._emoji
    
    @property
    def is_looking(self) -> str:
        return self._is_looking
    
    @property
    def head_position(self) -> bool:
        return self._head_position
    
    def set_health(self, value: int, isSum: bool) -> None:
        if(isSum):
            self._health += value
        
        if(isSum == False):
            self._health -= value
    
    def set_is_looking(self, value: str):
        self._is_looking = value

    def set_y_position(self, sum: bool):
        if(sum):
            self._y_position += 1
        else:
            self._y_position -= 1

    def set_x_position(self, sum: bool):
        if(sum):
            self._x_position += 1
        else:
            self._x_position -= 1

    def check_y_movement(self, sum: bool, board_size):
        if(sum and self._y_position + 1 > board_size - 1):
            return False
        
        if(sum == False and self._y_position - 1 < 0):
            return False
        
        #Valid movement
        return True

    def check_x_movement(self, sum: bool, board_size: int):
        if(sum and self._x_position + 1 > board_size - 1):
            return False
        
        if(sum == False and self._x_position - 1 < 0):
            return False
        
        #Valid movement
        return True


    def move(self, direction: str, board_size: int) -> None:

        #This dictionary contains the function for each direction and assing a bool
        #This bool will help us identify if the movement is valid in check_ _movements
        check_movement_dict = {
            'up': (self.check_y_movement, False),
            'down': (self.check_y_movement, True),
            'right': (self.check_x_movement, True),
            'left': (self.check_x_movement, False)
        }

        make_move_dict = {
            'up': self.set_y_position,
            'down': self.set_y_position,
            'right': self.set_x_position,
            'left': self.set_x_position,
        }

        check_movement, bool_value = check_movement_dict[direction]

        is_valid_movement = check_movement(bool_value, board_size)

        if(is_valid_movement):
            new_coordinates = make_move_dict[direction]
            new_coordinates(bool_value)
            return True
        else:
            print('Invalid move!')
            return None #Not a valid move

    def attack(self, target: 'Character') -> None:
        pass
    
    def eat(self) -> None:
        if(self.health != 100):
            self.set_health(10, True)

    def add_to_inventory(self):
        ''
    
    def getEmoji(self):
        return self._emoji