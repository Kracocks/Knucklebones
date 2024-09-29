from random import randint

class Player:
    def __init__(self, name:str = "Player") -> None:
        self.board = [
            [0,0,0], [0,0,0], [0,0,0]
        ]
        self.name = name
        # Limit list lenght
        for column in self.board:
            column = column[:3]
        self.board = self.board[:3]
        self.total_value = 0
    
    def __repr__(self) -> str:
        repr = self.name
        repr += "+-+-+-+\n"
        repr += f"|{self.board[0][0]}|{self.board[1][0]}|{self.board[2][0]}|\n"
        repr += f"|{self.board[0][1]}|{self.board[1][1]}|{self.board[2][1]}|\n"
        repr += f"|{self.board[0][2]}|{self.board[1][2]}|{self.board[2][2]}|\n"
        repr += "+-+-+-+\n"
        return repr
        
    def get_column_value(self, ind_col:int) -> int:
        """Get the value of a column

        Args:
            ind_col (int): index of a column

        Returns:
            int: the value of a column
        """
        col_value = 0
        number_of = {
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
            6 : 0
        }
        # Count the number of occurrences for each number in le column
        for case_value in self.board[ind_col]:
            if case_value != 0:
                number_of[case_value] += 1
                
        # Calculate the number of the column depending of the occurrence
        passed_values = set()
        for case_value in self.board[ind_col]:
            if case_value != 0 and case_value not in passed_values:
                if number_of[case_value] == 1:
                    col_value += case_value
                elif number_of[case_value] == 2:
                    col_value += case_value * 4
                elif number_of[case_value] == 3:
                    col_value += case_value * 9
                else:
                    col_value += case_value
                passed_values.add(case_value)
        return col_value
    
    def remove_values(self, ind_col:int, value_to_remove:int):
        """revove all the value given and shift the value to the start of the list

        Args:
            ind_col (int): the index of a column
            value_to_remove (int): the value to remove

        Raises:
            Exception: the index given is larger than the lenght of the list
        """
        if ind_col >= 3:
            raise Exception("Not an existing column")
        for ind_case_value in range(len(self.board[ind_col])):
            if self.board[ind_col][ind_case_value] == value_to_remove:
                self.board[ind_col][ind_case_value] = 0

        #Décaler les valeurs si une valeur a été supprimé
        for ind_case_value in range(1, len(self.board[ind_col])):
            ind = ind_case_value - 1
            while self.board[ind_col][ind] == 0 and ind >= 0:
                self.board[ind_col][ind] = self.board[ind_col][ind + 1]
                self.board[ind_col][ind + 1] = 0
                ind -= 1
        
    def put_value(self, ennemy:"Player", ind_col:int, value_to_put:int) -> bool:
        """Put the given value on the given column

        Args:
            ennemy (Player): the ennemy whose value will be remove
            ind_col (int): the index of the column
            value_to_put (int): the value to put

        Raises:
            Exception: the index given is larger than the lenght of the list 

        Returns:
            bool: returns True if it has put a number otherwise False
        """
        if ind_col >= 3:
            raise Exception("Not an existing column")
        for ind_case_value in range(len(self.board[ind_col])):
            if self.board[ind_col][ind_case_value] == 0:
                self.board[ind_col][ind_case_value] = value_to_put
                ennemy.remove_values(ind_col, value_to_put)
                return True
        return False
    
    def get_column(self, ind_col:int) -> list[int]:
        """Get the column with it's values

        Args:
            ind_col (int): the index of the column

        Returns:
            list[int]: the column
        """
        return self.board[ind_col]
    
    def calc_total(self):
        """Set the total value of the player
        """
        self.total_value = self.get_column_value(0) + self.get_column_value(1) + self.get_column_value(2)
    
    def has_won(self) -> bool:
        """Returns if the player has won

        Returns:
            bool: Returns True if the player has won otherwise returns False
        """
        for column in self.board:
            return not 0 in column
        return True
            
dice_value = 0
ennemy = Player("Kracocks Bot")
player = Player("")
# while True:
#     dice_value = randint(1,6)
    