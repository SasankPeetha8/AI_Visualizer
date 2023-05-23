# Importing the required modules
# Importing the system module and path function from Pathlib module
import sys
from pathlib import Path
# Specifying the required paths
IMPORT_PATHS = [
    r"UI\Layouts\GameArea",
    r"UI\Functions"
]

from ui_RandomMoveWidget import Ui_RandomMoveWidget

# Creating a class for GamePlayFunctions
class RandomMoveFunctionality(object):
    """docstring for RandomMoveFunctionality."""
    def __init__(self):
        super(RandomMoveFunctionality, self).__init__()
        # Creating an instance of the Random Move functionality
        self.__ui = Ui_RandomMoveWidget()
        # Setting up the UI
        self.__ui.setupUi(self)
        
    