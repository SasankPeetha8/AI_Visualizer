# Importing Pickle Module
import pickle

# Creating class to store the information
class UserData:
    def __init__(self, dictionary):
        self.data = dictionary
        

"""
Required data to store:
self.__game
self.MCTS_Data
self.unique_nodes
self.scene
self.view
self.scroll_area
self.v_layout 

# Fetch Player Information
self.__player_options
# Fetch board size
self.__boardSize
# 

# UI Data
self.__ui.ManualMoveFrame.isVisible()
self.__ui.RandomMoveFrame.isVisible()
self.__ui.AIMoveFrame.isVisible()
self.__ui.TreeVisualizer.isVisible()
self.__ui.TreeDisplayLabel.isVisible()
self.__ui.EnableReUseCheckBox.isVisible()
self.__ui.ManualEntryFrame.isVisible()
self.__ui.SearchStateButton.isVisible()
self.__ui.GameRegion.isEnabled()
self.__ui.AIMoveFrame.isEnabled(False)
self.__ui.RandomMoveFrame.isEnabled(False)
self.__ui.ManualMoveFrame.isEnabled(False)
self.__ui.actionSaveGame.isEnabled(True)
self.__ui.actionCloseGame.isEnabled(True)
self.__ui.ManualLineInput.text()
self.__ui.AILimitsEdit.text()
self.__ui.stateValue.text()
self.__ui.ManualEntryFrame.isVisible(True)
self.__ui.SearchStateButton.isVisible(True)


self.__ui.ThinkingTypeOptions.checkedId()
self.__ui.ThinkingTypeOptions.setId
self.__ui.ThinkingTypeOptions.checkedId()
self.__ui.ThinkingTypeOptions.setId


# RUN AT END
self.UpdateGameDisplay()


"""