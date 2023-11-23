import random
from Player import Player
from Monster import Monster
from Head_Position import Head_Position

class GameMap:
    def __init__(self, n) -> None:
        self._size = n
        self._matrix = [[' ' for _ in range(n)] for _ in range(n)]
        self._player = None
        self._monster = None
        self._head_position = None
        self.turn = None

    # -------------- Getters -------------
    @property
    def game_matrix(self) -> list:
        return self._matrix
    
    @property
    def player(self) -> 'Player':
        return self._player
    
    @property
    def monster(self) -> 'Monster':
        return self._monster
    
    @property
    def head_position(self) -> 'Head_Position':
        return self._head_position

    # -------------- Setters -------------
    def set_game_map_Objects(self, player: 'Player', monster: 'Monster', head_position: 'Head_Position') -> None:
        self._player = player
        self._monster = monster
        self._head_position = head_position
    
    # -------------- Methods -------------
    def updateBoard(self, player: 'Player') -> None:
        pass

    def start_game(self):
        player = self.player
        monster = Monster()
        matrix = self.game_matrix
        head_position = self.head_position

        while(True):
            if(self.turn == self.player):
                looking_result = head_position.calculate_head_position()
                #Reseting board and preparing for printing emoji
                matrix[player.y_position][player.x_position] = ' '
                
                #Make move
                if(player.move(looking_result, self._size) != None):
                    #Print emoji in new position
                    matrix[player.y_position][player.x_position] = player.emoji
                    #Printing board again
                    self.displayMap()
                    self.turn = monster
                else:
                    continue
                
            break
                

    
    def populate_board(self) -> None:
        player = Player(self._size - 1, self._size - 1)
        monster = Monster()
        matrix = self.game_matrix
        head_position = Head_Position()

        #Saving objects for later use
        self.set_game_map_Objects(player, monster, head_position)

        matrix[player.y_position][player.x_position] = player.emoji
        matrix[monster.y_position][monster.x_position] = monster.emoji

        #Print board with objects already setup
        self.displayMap()

        #Player's turn
        self.turn = player

        #Let the game begins!
        self.start_game()

    def displayMap(self) -> None:
        print("+---" * self._size + "+")
        for row in self._matrix:
            print("| " + " | ".join(map(str, row)) + " |")
            print("+---" * self._size + "+")


game_map = GameMap(5)
game_map.populate_board()