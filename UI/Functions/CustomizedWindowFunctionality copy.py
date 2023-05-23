# Importing the required PySide 6 Modules
from PySide6.QtWidgets import QMainWindow, QFileDialog, QDialog
# Importing the random module
import random
# Importing the system module and path function from Pathlib module
import sys
from pathlib import Path
# Specifying the required paths
IMPORT_PATHS = [
    r"UI\Layouts\MainWindow",
    r"UI\Layouts\MenuBar",
    r"UI\Layouts\GameArea",
    r"UI\Functions",
    r"UI\AI_Heuristics"
]
# sys.path.append([str(Path(each)) for each in IMPORT_PATHS])
# Appending the required path to the system
for each in IMPORT_PATHS:
    sys.path.append(str(Path(each)))

# Importing the main window layout
from ui_MainWindow import Ui_MainWindow
from MessageBoxFunctionality import NewGameDialog, CloseGameDialog
from BoardGames import TicTacToe
from PlayerInformation import Player

# Importing the layouts
# Defining a function for the customizing the main window which inherits the QMain Window
class CustomMainWindow(QMainWindow):
    """docstring for CustomMainWindow."""
    def __init__(self):
        super(CustomMainWindow, self).__init__()
        #############################################################################
        #------------------------- Displaying the window----------------------------#
        # Creating an instance of the main window from our layout
        self.__ui = Ui_MainWindow()
        # Setting up the layout
        self.__ui.setupUi(self)
        #############################################################################
        #----------------------------- Game Move Options----------------------------#
        # Hiding the Game Options
        self.__HideGameOptions()
        #############################################################################
        #------------------------------- Game Data----------------------------------#
        # Specifying the Player options
        # self.__boardSize = None
        # self.__player_options = None
        self.__game = None
        #############################################################################
        #------------------------------ Toolbar -----------------------------------#
        # Specifying the actions for the toolbar
        self.__ui.actionNewGame.triggered.connect(self.NewGameAction)
        self.__ui.actionLoadGame.triggered.connect(self.LoadGameAction)
        self.__ui.actionSaveGame.triggered.connect(self.SaveGameAction)
        self.__ui.actionCloseGame.triggered.connect(self.CloseGameAction)
        #############################################################################
        #------------------------------ Game Move Options --------------------------#
        self.__ui.RandomMoveButton.clicked.connect()
     
    ####################### Game Region Functionality ###############################
    # Defining methods to Hide Game Options
    def __HideGameOptions(self):
        # Hiding manual move Options
        self.__ui.ManualMoveFrame.setVisible(False)
        # Hiding Random Move Options
        self.__ui.RandomMoveFrame.setVisible(False)
        # Hiding AI Move Options
        self.__ui.AIMoveFrame.setVisible(False)
    
    ####################### Game Heuristic Functionality ############################
    # Defining methods to fetch the player options
    def fetchPlayerOptions(self):
        return self.__player_options
    
    # Defining methods to fetch the board size
    def fetchBoardSize(self):
        return self.__boardSize
    
    # Defining method to display the game
    def UpdateGameDisplay(self):
        self.__ui.GameInfoLabel.setText(self.__game.__str__())
    
    
    ###################### Statusbar Functionality #################################
    # Defining method to display long message in the statusbar
    def displayLongMessage(self, message):
        # Displaying the message on the status bar without any limits
        self.__ui.statusbar.showMessage(f"{message}")
    
    # Defining method to display short message on the statusbar
    def displayShortMessage(self, message):
        self.__ui.statusbar.showMessage(f"{message}", timeout=2000)
        
    # Defining method to display the player move information
    def displayPlayerMove(self):
        self.displayLongMessage(f"Player {self.__game.FindCurrentPlayer().Character} turn")
        
    ###################### Toolbar Functionality ###################################
    # Defining the event for the New game
    def NewGameAction(self):
        # Creating an instance of the NewGameDialogBox
        dialogBox = NewGameDialog()
        # Running the dialog box
        response = dialogBox.exec()
        # If response is Okay then enable the New Game
        if response == QDialog.Accepted:
            # Enabling to play the game
            self.__ui.GameRegion.setEnabled(True)
            # Enabling the game save option
            self.__ui.actionSaveGame.setEnabled(True)
            # Enabling the game close option
            self.__ui.actionCloseGame.setEnabled(True)
            # Displaying the message in the status bar
            # self.ui.statusbar.setStatusTip(f"New Game Begins")
            self.__ui.statusbar.showMessage(f"New Game Begins", timeout=2000)
            # Fetching the information of the board choice
            boardSize = int(dialogBox.getBoardSize())
            # Defining the board options
            move_options =  ["mcts", "random", "manual"]
            # Fetching the player options
            player_options = dialogBox.getPlayerOptions()
            # Defining player X
            player_X = Player(character="X", type=move_options[player_options[0]+1])
            # Defining Player Y
            player_Y = Player(character="O", type=move_options[player_options[1]+1])
            # Enable the move options
            if -2 in player_options:
                # Un-hiding the Manual Move Options
                self.__ui.ManualMoveFrame.setVisible(True)
            if -3 in player_options:
                # Un-Hiding the Random Move Options
                self.__ui.RandomMoveFrame.setVisible(True)
            if -4 in player_options:
                # Un-Hiding the AI Move Options
                self.__ui.AIMoveFrame.setVisible(True)
            # Creating an instance of the game object
            self.__game = TicTacToe(first_player=player_X, second_player=player_Y, board_size=boardSize)
            # Updating the game display
            self.UpdateGameDisplay()
            # Display the player move information
            self.displayPlayerMove()
        # If response is Cancel, then disable the new game but show the status
        else:
            # self.ui.statusbar.setStatusTip(f"User cancelled the new game")
            # self.__ui.statusbar.showMessage(f"User cancelled the new game", timeout=2000)
            self.displayShortMessage(f"User cancelled the new game")
    
    # Defining action for the close game
    def CloseGameAction(self):
        # Creating an instance of the CloseGameDialogBox
        dialogBox = CloseGameDialog()
        # Running the dialog box
        response = dialogBox.exec()
        # If response is Okay then enable the New Game
        if response == QDialog.Accepted:
            # Disabling the game region
            self.__ui.GameRegion.setEnabled(False)
            # Disabling the game save option from the toolbar
            self.__ui.actionSaveGame.setEnabled(False)
            # Hiding the game options
            self.__HideGameOptions()
            # Changing the game display label
            self.__ui.GameInfoLabel.setText(f"Create a New Game / Load Existing Game")
            # Displaying the message in the status bar
            # self.ui.statusbar.setStatusTip(f"New Game Begins")
            # self.__ui.statusbar.showMessage(f"Closed the game", timeout=2000)
            self.displayShortMessage(f"Closed the game")
        # If response is Cancel, then disable the new game but show the status
        else:
            # self.ui.statusbar.setStatusTip(f"User cancelled the new game")
            # self.__ui.statusbar.showMessage(f"The game continues", timeout=2000)
            self.displayShortMessage(f"The game continues")
        
    # Defining action for the load game
    def LoadGameAction(self):
        # Fetching thre required file name
        file_name = QFileDialog.getOpenFileName(self, caption="Load Existing Game", filter=f"All Files (*)")
        # Fetching only the filename with directory
        file_name = file_name[0]
        # Checking if the filename is valid or not
        if file_name:
            # self.__ui.statusbar.showMessage(f"Loaded the existing game", timeout=2000)
            self.displayShortMessage(f"Loaded the existing game")
        else:
            # self.__ui.statusbar.showMessage(f"User cancelled loading the game", timeout=2000)
            self.displayShortMessage(f"User cancelled loading the game")
            
    # Defining action for the Save game
    def SaveGameAction(self):
        # Fetching thre required file name
        file_name = QFileDialog.getSaveFileName(self, caption="Save Game", filter=f"All Files (*)")
        # Fetching only the filename with directory
        file_name = file_name[0]
        # Checking if the filename is valid or not
        if file_name:
            # self.__ui.statusbar.showMessage(f"Saved the game", timeout=2000)
            self.displayShortMessage(f"Saved the game")
        else:
            # self.__ui.statusbar.showMessage(f"User cancelled saving the game", timeout=2000)
            self.displayShortMessage(f"User cancelled saving the game")
            
    ###################### Game Options Functionality ###################################
    # Defining functionality for the random move button
    def RadomMoveButtonFunction(self):
        # Fetching the available states
        available_states = self.__game.AvailableStates()
        # Choosing a state at random
        selected_state = random.choice(available_states) if len(available_states) > 1 else available_states[0]
        # Updating the game board positions
        self.__game.BoardPositions = selected_state
        # Update the game display
        self.UpdateGameDisplay()
        # Checking the game status
        
        
        