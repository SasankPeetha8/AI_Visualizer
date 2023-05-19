# Importing the required PySide 6 Modules
from PySide6.QtWidgets import QMainWindow, QFileDialog, QDialog

# Importing the system module and path function from Pathlib module
import sys
from pathlib import Path
# Specifying the required paths
IMPORT_PATHS = [
    r"UI\Layouts\MainWindow",
    r"UI\Layouts\MenuBar",
    r"UI\Layouts\GameArea",
    r"UI\Functions"
]
# sys.path.append([str(Path(each)) for each in IMPORT_PATHS])
# Appending the required path to the system
for each in IMPORT_PATHS:
    sys.path.append(str(Path(each)))

# Importing the main window layout
from ui_MainWindow import Ui_MainWindow
from MessageBoxFunctionality import NewGameDialog, CloseGameDialog 

# Importing the layouts
# Defining a function for the customizing the main window which inherits the QMain Window
class CustomMainWindow(QMainWindow):
    """docstring for CustomMainWindow."""
    def __init__(self):
        super(CustomMainWindow, self).__init__()
        # Creating an instance of the main window from our layout
        self.__ui = Ui_MainWindow()
        # Setting up the layout
        self.__ui.setupUi(self)
        # Specifying the actions for the toolbar
        # self.__ui.actionNewGame.triggered.connect(self.NewGameAction)
        self.__ui.actionLoadGame.triggered.connect(self.LoadGameAction)
        self.__ui.actionSaveGame.triggered.connect(self.SaveGameAction)
        self.__ui.actionCloseGame.triggered.connect(self.CloseGameAction)
        
    ################# ACTIONS ######################
    # Defining action for the close game
    def CloseGameAction(self):
        # Creating an instance of the CloseGameDialogBox
        dialogBox = CloseGameDialog()
        # Running the dialog box
        response = dialogBox.exec()
        # If response is Okay then enable the New Game
        if response == QDialog.Accepted:
            # Enabling to play the game
            self.__ui.GameRegion.setEnabled(False)
            # Displaying the message in the status bar
            # self.ui.statusbar.setStatusTip(f"New Game Begins")
            self.__ui.statusbar.showMessage(f"Closed the game", timeout=2000)
        # If response is Cancel, then disable the new game but show the status
        else:
            # self.ui.statusbar.setStatusTip(f"User cancelled the new game")
            self.__ui.statusbar.showMessage(f"The game continues", timeout=2000)
        
    # Defining action for the load game
    def LoadGameAction(self):
        # Fetching thre required file name
        file_name = QFileDialog.getOpenFileName(self, caption="Load Existing Game", filter=f"All Files (*)")
        # Fetching only the filename with directory
        file_name = file_name[0]
        # Checking if the filename is valid or not
        if file_name:
            self.__ui.statusbar.showMessage(f"Loaded the existing game", timeout=2000)
        else:
            self.__ui.statusbar.showMessage(f"User cancelled loading the game", timeout=2000)
            
    # Defining action for the Save game
    def SaveGameAction(self):
        # Fetching thre required file name
        file_name = QFileDialog.getSaveFileName(self, caption="Save Game", filter=f"All Files (*)")
        # Fetching only the filename with directory
        file_name = file_name[0]
        # Checking if the filename is valid or not
        if file_name:
            self.__ui.statusbar.showMessage(f"Saved the game", timeout=2000)
        else:
            self.__ui.statusbar.showMessage(f"User cancelled saving the game", timeout=2000)
    