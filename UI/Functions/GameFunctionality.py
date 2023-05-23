# Importing the required modules
# Importing the system module and path function from Pathlib module
import sys, random
from pathlib import Path
# Specifying the required paths
IMPORT_PATHS = [
    r"UI\Functions",
    r"UI\AI_Heuristics"
]
# sys.path.append([str(Path(each)) for each in IMPORT_PATHS])
# Appending the required path to the system
for each in IMPORT_PATHS:
    sys.path.append(str(Path(each)))

from CustomizedWindowFunctionality import CustomMainWindow
from PlayerInformation import Player
from BoardGames import TicTacToe

# Creating a class for Game Functionality
class GamePrinciples(CustomMainWindow):
    """docstring for GamePrinciples."""
    def __init__(self):
        super(GamePrinciples, self).__init__()
        # Creating an instance of the UI
        # self.__UI = CustomMainWindow()
        # # Setting up the UI instance
        # # self.__UI.setupUi()
        # Fetching the board positions
        self.BoardSize = self.fetchBoardSize()
        print(f"Board Size: {self.BoardSize}")
        # Fetching the player options
        # playerOptions = self.__UI.fetchPlayerOptions()
        # Available move options
        move_options = ["mcts", "random", "manual"]
        # # Defining player X
        # self.Player_X = Player(character="X", type=move_options[playerOptions[0]+1])
        # # Defining the player O
        # self.Player_O = Player(character="O", type=move_options[playerOptions[1]+1])
        # # Creating an instance of the Tic Tac Toe game
        # self.Game = TicTacToe(first_player=self.Player_X, second_player=self.Player_O, board_size=self.BoardSize)      
        
        # # Creating slots and connections
        # self.__UI.RandomMoveButton.triggered.connect(self.RandomMoveAction)
        
        
    # # Defining method to display the output
    # def show(self):
    #     self.__UI.show()
        
    # Defining method to take random moves
    def RandomMoveAction(self):
        possible_moves = self.Game.AvailableStates
        selected_move = random.choice(possible_moves) if len(possible_moves) > 1 else possible_moves[0]
        self.Game.BoardPositions = selected_move
        current_Player = self.Game.FindCurrentPlayer().Character
        self.__UI.displayLongMessage(f"Player {current_Player} turn..")
        
    