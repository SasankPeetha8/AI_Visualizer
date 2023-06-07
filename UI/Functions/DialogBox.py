from PySide6.QtWidgets import QDialog, QDialogButtonBox
from ui_NodeInfoDialog import Ui_NodeDialog
from copy import deepcopy
# Creating a class
class DialogBox(QDialog):
    """docstring for DialogBox."""
    def __init__(self, node):
        super(DialogBox, self).__init__()
        self.ui = Ui_NodeDialog()
        self.ui.setupUi(self)
        self.data = node
        self.ui.NodeLabelInfo.setText(self.data.__str__())
        self.ui.nodeWinValue.setText(f"{self.data.NodeScore}")
        okay_button = self.ui.DialogButtons.button(QDialogButtonBox.Ok)
        cancel_button = self.ui.DialogButtons.button(QDialogButtonBox.Cancel)
        okay_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        self.available_states = self.FetchAllStates()
        self.index = len(self.available_states)-1
        self.ui.previousMoveButton.clicked.connect(self.previous_state_event)
        self.ui.nextMoveButton.clicked.connect(self.next_state_event)
        if self.index == 0:
            self.ui.previousMoveButton.setEnabled(False)
        if self.index == len(self.available_states)-1:
            self.ui.nextMoveButton.setEnabled(False)
        
    # Defining method to fetch all the values in the list
    def FetchAllStates(self):
        new_data = [ ]
        # Creating a copy of the node_info
        node = deepcopy(self.data)
        # Iterating through all the values
        while node:
            if node not in new_data:
                new_data = [ node ] + new_data
                # new_data = new_data + [ node ]
                
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
        # Updating the view
        self.ui.NodeLabelInfo.setText(self.available_states[self.index].__str__())
        self.ui.nodeWinValue.setText(f"{self.available_states[self.index].NodeScore}")
        
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
        self.ui.NodeLabelInfo.setText(self.available_states[self.index].__str__())
        self.ui.nodeWinValue.setText(f"{self.available_states[self.index].NodeScore}")
        
        