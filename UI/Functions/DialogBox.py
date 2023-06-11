# Importing the system module and path function from Pathlib module
import sys
from pathlib import Path
# Specifying the required paths
IMPORT_PATHS = [
    r"UI\Layouts\Dialog"
]
# sys.path.append([str(Path(each)) for each in IMPORT_PATHS])
# Appending the required path to the system
for each in IMPORT_PATHS:
    sys.path.append(str(Path(each)))

from PySide6.QtWidgets import QDialog, QDialogButtonBox
from ui_NodeInfoDialog import Ui_NodeDialog
from copy import deepcopy
import math

# Creating a class
class DialogBox(QDialog):
    """docstring for DialogBox."""
    def __init__(self, node):
        super(DialogBox, self).__init__()
        self.ui = Ui_NodeDialog()
        self.ui.setupUi(self)
        self.data = node
        self.ui.NodeLabelInfo.setText(self.data.__str__())
        # Defining the Okay Button
        okay_button = self.ui.DialogButtons.button(QDialogButtonBox.Ok)
        # Defining the cancel button
        cancel_button = self.ui.DialogButtons.button(QDialogButtonBox.Cancel)
        # Creating the connect event for the okay button
        okay_button.clicked.connect(self.accept)
        # Creating the connect event for the cancel button
        cancel_button.clicked.connect(self.reject)
        # Fetching the available state
        self.available_states = self.FetchAllStates()
        self.index = len(self.available_states)-1
        self.updateTitle = False
        # Updating all values
        self.UpdateAllValues()
        # Creating connect event for the previous move button
        self.ui.previousMoveButton.clicked.connect(self.previous_state_event)
        # Creating the connect event for the next move button
        self.ui.nextMoveButton.clicked.connect(self.next_state_event)
        # Disabling the buttons
        if self.index == 0:
            self.ui.previousMoveButton.setEnabled(False)
        if self.index == len(self.available_states)-1:
            self.ui.nextMoveButton.setEnabled(False)
        # Disabling the Best Move and Best move itertions
        # self.ToogleBestMove(False)
    
    # Defining method to enable or disable the Best move
    def ToogleBestMove(self, bool_value):
        # Toogle Best Move Lable
        self.ui.bestNodeLabel.setVisible(bool_value)
        # Toogle Best Move value
        self.ui.bestNodeValue.setVisible(bool_value)
        # Toogle best iterations Label
        self.ui.bestNodeIterationsLabel.setVisible(bool_value)
        # Toogle best iterations Value
        self.ui.bestNodeIterationsValue.setVisible(bool_value)
    
    # Fetch the node score value
    def CalculateScore(self, node_data):
        # Calculating the exploitation value
        exploitation_value = node_data.NodeScore/node_data.NodeVisits
        # Calculating the exploration value
        exploration_value = math.sqrt(2) * ( math.sqrt((math.log10(node_data.ParentNode.NodeVisits))/node_data.NodeVisits))
        # Calculating the total score
        total_score = exploitation_value + exploration_value
        # Returning total score
        return total_score
    
    # Defining method to update all the values on the Node Dialog Box
    def UpdateAllValues(self, node_data=None):
        # Checking if the node_data is None or not
        node_data = node_data if node_data else self.data
        # Checking if the node is best node or not
        if node_data.best_node:
            # Display the best node values
            self.ToogleBestMove(True)
            self.BestStateDisplay(node_data)
        else:
            self.ToogleBestMove(False)
            
        # Checking if the root node is not none
        if node_data.ParentNode:
            # Displaying the node win label
            self.ui.nodeWinLabel.setVisible(True)
            self.ui.nodeWinValue.setVisible(True)
            # Updating the node win rate value
            self.ui.nodeWinValue.setText(f"{self.CalculateScore(node_data)}")
        else:
            # Hiding node win label
            self.ui.nodeWinLabel.setVisible(False)
            # Hiding node win value
            self.ui.nodeWinValue.setVisible(False)
            
        # Updating the node type value
        self.ui.nodeTypeValue.setText(f"{node_data.NodeType}")
        # Updating the node visit count
        self.ui.nodeVisitValue.setText(f"{node_data.NodeVisits}")
        # Updating the available child node values
        self.ui.childNodeValue.setText(f"{len(node_data.ChildNodes)}")
        # Fetching the node depth value
        depth_value = self.FindNodeDepth(deepcopy(node_data))
        # Updating the node depth value
        self.ui.nodeDepthValue.setText(f"{depth_value}")
        # Updating the text value
        self.ui.NodeLabelInfo.setText(node_data.__str__())
        # Updating the creation value
        self.ui.createIterationValue.setText(f"{node_data.Creation}")
        if self.updateTitle:
            self.updateTitleValue()

    def updateTitleValue(self):
        self.ui.NodeStateLabel.setText(f"States Found - {self.index+1}")
    
    def FindNodeDepth(self, node):
        index = 0
        while node.ParentNode:
            node = node.ParentNode
            index = index + 1
        return index
    
    # Defining method to fetch all the values in the list
    def FetchAllStates(self):
        new_data = [ ]
        # Creating a copy of the node_info
        node = deepcopy(self.data)
        # Iterating through all the values
        while node:
            if node not in new_data:
                new_data = [ node ] + new_data
            node = node.ParentNode
        return new_data
    
    # Defining method for the previous state event
    def previous_state_event(self):
        # Fetching the current index value
        self.index = self.index - 1
        # Updating the value
        if self.index == 0:
            self.ui.previousMoveButton.setEnabled(False)
        else:
            self.ui.previousMoveButton.setEnabled(True)
        if self.index == len(self.available_states)-1:
            self.ui.nextMoveButton.setEnabled(False)
        else:
            self.ui.nextMoveButton.setEnabled(True)
        # # Updating the view
        # self.ui.NodeLabelInfo.setText(self.available_states[self.index].__str__())
        # self.ui.nodeWinValue.setText(f"{self.available_states[self.index].NodeScore}")
        self.UpdateAllValues(self.available_states[self.index])
        
    # Defining method for the next state event
    def next_state_event(self):
        # Fetching the current index value
        self.index = self.index + 1
        # Updating the value
        if self.index == 0:
            self.ui.previousMoveButton.setEnabled(False)
        else:
            self.ui.previousMoveButton.setEnabled(True)
        if self.index == len(self.available_states)-1:
            self.ui.nextMoveButton.setEnabled(False)
        else:
            self.ui.nextMoveButton.setEnabled(True)
        # Updating the view
        # self.ui.NodeLabelInfo.setText(self.available_states[self.index].__str__())
        # self.ui.nodeWinValue.setText(f"{self.available_states[self.index].NodeScore}")
        self.UpdateAllValues(self.available_states[self.index])
        
    # Defining method for the best state
    def BestStateDisplay(self, node):
        # Enabling the display
        self.ToogleBestMove(True)
        # Updating the best move label
        self.ui.bestNodeValue.setText(f"{node.best_node}")
        # Updating the best move value
        self.ui.bestNodeIterationsValue.setText(f"{node.requiredIterations}")
        
        