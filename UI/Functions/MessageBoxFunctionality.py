# Importing the required Modules
from PySide6.QtWidgets import QDialog, QDialogButtonBox

# Importing the required UI Layout
from ui_NewGameMessageBox import Ui_NewGameDialog
from  ui_CloseGameMessageBox import Ui_CloseGameDialog

# Creating a class for NewGameDialog
class NewGameDialog(QDialog):
    """docstring for NewGameDialog."""
    def __init__(self):
        super(NewGameDialog, self).__init__()
        # Creating an instance of the UI
        self.__newGameDialogBox = Ui_NewGameDialog()
        # setting up the UI Interface
        self.__newGameDialogBox.setupUi(self)
        # Extracting the button information
        okay_button = self.__newGameDialogBox.DialogButtons.button(QDialogButtonBox.Ok)
        cancel_button = self.__newGameDialogBox.DialogButtons.button(QDialogButtonBox.Cancel)
        # Creating a slot and connection for the dialog buttons
        # self.__newGameDialogBox.DialogButtons.accepted.connect(self.accept)
        # self.__newGameDialogBox.DialogButtons.rejected.connect(self.reject)
        okay_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
    
    # Defining method to extract the board data
    def getBoardSize(self):
        # Fetching the required text from the group box
        return self.__newGameDialogBox.ChoiceMenu.currentText()[0]
    
    # Defining method to get the player options
    def getPlayerOptions(self):
        # Fetching the checked options for both the players
        return ( self.__newGameDialogBox.PlayerXGroup.checkedId(), self.__newGameDialogBox.PlayerOGroup.checkedId() )
    
    # Defining method to extract player information
    def getPlayerPreferences(self):
        # Extracting which checkbox is enabled
        button_id = self.__newGameDialogBox.PlayerOptionsGroup.checkedId()
        # Checking if player X is enabled
        if button_id == -2:
            # Returning Player X
            return f"X"
        # Checking if Player O is enabled
        elif button_id == -3:
            # Returning Player O
            return f"O"
        
# Creating a class for the Close Game Dialog
class CloseGameDialog(QDialog):
    """docstring for CloseGameDialog."""
    def __init__(self):
        super(CloseGameDialog, self).__init__()
        # Creating an instance of the UI
        self.__closeGameDialogBox = Ui_CloseGameDialog()
        # Setting up the UI interface
        self.__closeGameDialogBox.setupUi(self)
        # Extracing the button information
        okay_button = self.__closeGameDialogBox.DialogButtons.button(QDialogButtonBox.Ok)
        cancel_button = self.__closeGameDialogBox.DialogButtons.button(QDialogButtonBox.Cancel)
        # Creating a slot and connection for the dialog buttons
        okay_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)