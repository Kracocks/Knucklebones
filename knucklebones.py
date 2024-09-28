from random import randint
from typing import Tuple

class Player:
    def __init__(self) -> None:
        self.board = [
            [0,0,0], [0,0,0], [0,0,0]
        ]
        self.value = 0
        
    def get_column_value(self, col:int) -> int:
        col_value = 0
        number_of = {
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
            6 : 0
        }
        for case_value in self.board[col]:
            if case_value != 0:
                number_of[case_value] += 1  
        for case_value in self.board[col]:
            if number_of[case_value] == 1:
                col_value += case_value
            elif number_of[case_value] == 2:
                col_value += case_value * 4
            else:
                col_value += case_value  
        return col_value
    
    def remove_values(self, col:int, value_to_remove:int):
        for ind_case_value in range(len(self.board[col])):
            if self.board[col][ind_case_value] == value_to_remove:
                self.board[col][ind_case_value] = 0
        
            
    def put_value(self, ennemy:"Player", col:int, value_to_put:int) -> bool:
        for ind_case_value in range(len(self.board[col])):
            if self.board[col][ind_case_value] == 0:
                self.board[col][ind_case_value] = value_to_put
                ennemy.remove_values(col, value_to_put)
                return True
        return False
            
dice_value = 0
ennemy = Player()
player = Player()

# while True:
#     dice_value = randint(1,6)
    