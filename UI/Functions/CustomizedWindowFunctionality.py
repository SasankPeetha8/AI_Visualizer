# Importing the required PySide 6 Modules
from PySide6.QtWidgets import QMainWindow, QFileDialog, QDialog, QGraphicsView
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
from AI import MCTS

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
        self.MCTS_Data = None
        #############################################################################
        #------------------------------ Toolbar -----------------------------------#
        # Specifying the actions for the toolbar
        self.__ui.actionNewGame.triggered.connect(self.NewGameAction)
        self.__ui.actionLoadGame.triggered.connect(self.LoadGameAction)
        self.__ui.actionSaveGame.triggered.connect(self.SaveGameAction)
        self.__ui.actionCloseGame.triggered.connect(self.CloseGameAction)
        #############################################################################
        #------------------------------ Game Move Options --------------------------#
        self.__ui.RandomMoveButton.clicked.connect(self.RadomMoveButtonFunction)
        self.__ui.ManualMoveButton.clicked.connect(self.ManualMoveButtonFunction)
        # Defining slots and connections for AI move values
        self.__ui.ThinkingTypeOptions.buttonClicked.connect(self.UpdateAIValuesFunction)
        self.__ui.L_LimitButton.clicked.connect(self.AI_Buttons_Function)
        self.__ui.M_LimitButton.clicked.connect(self.AI_Buttons_Function)
        self.__ui.H_LimitButton.clicked.connect(self.AI_Buttons_Function)
        self.__ui.HighestLimit.clicked.connect(self.AI_Buttons_Function)
        # Defining slots and connections for AI Build Tree
        self.__ui.AIBuildTreeButton.clicked.connect(self.AIBuildTreeButtonFunction)
        self.__ui.AIMoveButton.clicked.connect(self.MakeAIMoveFunction)
        self.__ui.AIDisplayTreeButton.clicked.connect(self.DisplayTreeFunction)
        self.unique_nodes = { }
        
        self.scene = None
        self.view = QGraphicsView()
        self.scroll_area = None
        self.v_layout = None
        
     
    ####################### Game Region Functionality ###############################
    # Defining methods to Hide Game Options
    def __HideGameOptions(self):
        # Hiding manual move Options
        self.__ui.ManualMoveFrame.setVisible(False)
        # Hiding Random Move Options
        self.__ui.RandomMoveFrame.setVisible(False)
        # Hiding AI Move Options
        self.__ui.AIMoveFrame.setVisible(False)
        # Hide Tree View Functionality
        self.__ui.TreeVisualizer.setVisible(False)
        # Hide Tree View Label
        self.__ui.TreeDisplayLabel.setVisible(False)
        
    ####################### Tree View Functionality #################################
    
    
    ####################### Game Heuristic Functionality ############################
    # Defining methods to fetch the player options
    def fetchPlayerOptions(self):
        return self.__player_options
    
    # Defining methods to fetch the board size
    def fetchBoardSize(self):
        return self.__boardSize
    
    # Defining method to display the game
    def UpdateGameDisplay(self):
        # Updating the game info label
        self.__ui.GameInfoLabel.setText(self.__game.__str__())
        # Checking game status
        game_status = self.CheckGametatus()
        # If game can continue, then updating the move options and game status info
        if game_status:
            # Updating the game move options
            self.UpdateMoveOptions()
            # Updating the game display
            self.displayPlayerMove()
        
    # Defining method to disable the game play area
    def __disableGamePlayArea(self):
        # Disabling the game play area
        self.__ui.GameRegion.setEnabled(False)
        
    # Defining method to enable the game play area
    def __enableGamePlayArea(self):
        # Enabling the game play area
        self.__ui.GameRegion.setEnabled(True)
    
    # Defining method to check game status
    def CheckGametatus(self):
        # Initalising the boolean value
        continueGame = True
        # Checking if the game is won or not
        winner = self.__game.IsWin()
        # Checking if any winner is found or not
        if winner and winner != "None":
            # Displaying the win status
            self.displayLongMessage(f"Player {winner} has won the game.")
            # Disabling to continue the game
            continueGame = False
        # Checking if the game is draw
        elif self.__game.IsDraw():
            # Displaying the game play area
            self.displayLongMessage(f"The Game is draw.")
            # Disabling to continue the game
            continueGame = False
        # Returning the game status
        # Disabling the game play area
        if not continueGame:
            self.__disableGamePlayArea()
        # returning the flag value
        return continueGame
    
    # Defining the method to update the move status based on the game positions
    def UpdateMoveOptions(self):
        # Disabling all the moves
        self.__ui.AIMoveFrame.setEnabled(False)
        self.__ui.RandomMoveFrame.setEnabled(False)
        self.__ui.ManualMoveFrame.setEnabled(False)
        
        # Fetching the status of the current player
        currentPlayer = self.__game.FindCurrentPlayer().Type
        # Checking if the current player and preferred player are same
        if currentPlayer.lower() == "ai":
            # Displaying the random and AI moves
            self.__ui.AIMoveFrame.setEnabled(True)
            # self.__ui.IterationsCheckBox.setEnabled(True)
            # self.__ui.TimeCheckBox.setEnabled(True)
            # self.__ui.AITypeBox.setEnabled(True)
        elif currentPlayer.lower() == "random":
            # Disbling the random move frame
            self.__ui.RandomMoveFrame.setEnabled(True)
        elif currentPlayer.lower() == "manual":
            # Disabling the manual move frame
            self.__ui.ManualMoveFrame.setEnabled(True)
            
    
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
            # self.__ui.GameRegion.setEnabled(True)
            self.__enableGamePlayArea()
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
            move_options =  ["ai", "random", "manual"]
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
                # Un-Hiding the Tree Visualizer
                self.__ui.TreeVisualizer.setVisible(True)
                # Un-Hiding the Tree Visualizer Label
                self.__ui.TreeDisplayLabel.setVisible(True)
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
            # self.__ui.GameRegion.setEnabled(False)
            self.__disableGamePlayArea()
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

    # Defining functionality for the Manual move button
    def ManualMoveButtonFunction(self):
        # Fetching the available positions
        available_positions = self.__game.AvailablePositions()
        # Fetching the manual line input value
        move_value = self.__ui.ManualLineInput.text()
        # Converting the input value to integer
        try:
            # Type casting the input value
            move_value = int(move_value) - 1
            # Checking if the provided value present in the available positions
            if move_value not in available_positions:
                # If not available, rise error
                raise ValueError
            # If available, then update the board positions accordingly
            else:
                # Fetching the current player character
                current_player = self.__game.FindCurrentPlayer().Character
                # Fetching the game board positions
                positions = self.__game.BoardPositions
                # Updating the current player character in the board position
                positions[move_value] = current_player
                # Updating the board positions in the game
                self.__game.BoardPositions = positions
                # Updating the game display
                self.UpdateGameDisplay()
        # If Invalid input provided, raise an error
        except ValueError:
            # Displaying the error message in the status bar
            self.displayShortMessage(f"INVALID INPUT PROVIDED, Please retry")
            
    # Defining functionality for the AI Move Button
    def AI_Buttons_Function(self):

        # Fetching the information from the AI Limit Type
        button_id = self.__ui.ThinkingTypeOptions.checkedId()

        # Fetching the Button Name
        button = self.sender().objectName()

        # Checking if the button is L_LimitButton
        if button == "L_LimitButton":
            # Fetching the value of the button text
            limit = self.__ui.L_LimitButton.text()

        elif button == "M_LimitButton":
            # Fetching the value of the button text
            limit = self.__ui.M_LimitButton.text()

        elif button == "H_LimitButton":
            # Fetching the value of the button text
            limit = self.__ui.H_LimitButton.text()

        elif button == "HighestLimit":
            limit = self.__ui.HighestLimit.text()

        # Removing the required text values
        limit = limit[:limit.index(" ")]

        # Checking if the checked box is iterations 
        if button_id == -2:
            # Converting the button to integer
            limit = int(limit)
            # Creating the MCTS Object based on iterations
            # self.__AI_Data = MCTS(self.__game, itertions=limit, time=None)
            # print(f"MCTS: Iterations-{limit}, time-None")
            self.MCTS_Data = MCTS(self.__game, itertions=limit, time=None)

        # Checking if the checked box is time
        elif button_id == -3:
            # Removing the required text values
            limit = float(limit)
            # Creating the MCTS Object based on time
            # self.__AI_Data = MCTS(self.__game, itertions=None, time=limit)
            # print(f"MCTS: Iterations-None, time-{limit}")
            self.MCTS_Data = MCTS(self.__game, itertions=None, time=limit)

        # Building the MCTS Tree
        self.BuildMCTSTreeInformation()
            
    # Defining method to provide functionality to update AI Values
    def UpdateAIValuesFunction(self):
        # Fetching the information from the AI Limit type
        button_id = self.__ui.ThinkingTypeOptions.checkedId()
        # Checking if the checked box is iterations
        if button_id == -2:
            # Updating the values of the Buttons
            self.__ui.L_LimitButton.setText(f"1 Iteration")
            self.__ui.M_LimitButton.setText(f"10 Iterations")
            self.__ui.H_LimitButton.setText(f"100 Iterations")
            self.__ui.HighestLimit.setText(f"1000 Iterations")
        elif button_id == -3:
            # Updating the values fo the buttons
            self.__ui.L_LimitButton.setText(f"0.01 Sec")
            self.__ui.M_LimitButton.setText(f"0.1 Sec")
            self.__ui.H_LimitButton.setText(f"1 Sec")
            self.__ui.HighestLimit.setText(f"2 Sec")
    
    # Defining method to provide functionality to build MCTS Tree
    def AIBuildTreeButtonFunction(self):
        # Fetching the information from the AI limit type
        button_id = self.__ui.ThinkingTypeOptions.checkedId()
        # Fetching the text from the AI Entry Box
        try:
            limit = float(self.__ui.AILimitsEdit.text())
            # Checking if the checked box is iterations
            if button_id == -2:
                # Updating the text in the text field
                self.__ui.AILimitsEdit.setText(f"{int(limit)}")
                # Updating the MCTS data
                # print(f"MCTS: Iterations-{int(limit)}, Time-None")
                self.MCTS_Data = MCTS(game_object=self.__game, itertions=int(limit), time=None)
                self.displayLongMessage(f"Game Positions: {self.__game.BoardPositions}")
            elif button_id == -3:
                # Updating the MCTS Data
                # print(f"MCTS: Iterations-None, Time-{float(limit)}")    
                self.MCTS_Data = MCTS(game_object=self.__game, itertions=None, time=limit)
                self.displayLongMessage(f"Game Positions: {self.__game.BoardPositions}")
        except ValueError:
            self.displayShortMessage(f"Invalid limit provided for MCTS")
        
    # Defining method build MCTS Tree Data
    def BuildMCTSTreeInformation(self):
        # Updating the game object
        self.MCTS_Data.game_object = self.__game
        # Finding current game player
        currentPlayer = self.__game.FindCurrentPlayer()
        # Fetching information if Re-Use check box is enabled or not
        enableMCTSReuse = self.__ui.EnableReUseCheckBox.isEnabled()
        # Checking if the Re-Use button is available or not
        if enableMCTSReuse and currentPlayer.GameTree != None and currentPlayer.GameTree != False:
            # Finding the current game state from the existing game tree
            game_tree = self.MCTS_Data.FindState(currentPlayer.GameTree, self.__game.BoardPositions)
            # Checking if the game tree is valid or not
            if game_tree:
                # Building the game tree
                currentPlayer.GameTree = self.MCTS_Data.BuildTree(tree_data=game_tree)
            else:
                # Building the game tree
                currentPlayer.GameTree = self.MCTS_Data.BuildTree()
            # self.displayLongMessage(f"Building game Tree with Old Game Tree")
        else:
            # Building the game tree
            currentPlayer.GameTree = self.MCTS_Data.BuildTree()
            # self.displayLongMessage(f"Building game Tree with New Game Tree")
            
    # Defining method to make a move from the MCTS Data
    def MakeAIMoveFunction(self):
        # Fetching the current player
        currentPlayer = self.__game.FindCurrentPlayer()
        # Finding the best positions
        best_positions = self.MCTS_Data.BestMove(currentPlayer.GameTree)
        # Updating the nodes as per the positions
        currentPlayer.GameTree = self.MCTS_Data.FindState(tree_data=currentPlayer.GameTree, positions=best_positions)
        # Updating the game positions
        self.__game.BoardPositions = best_positions
        # Updating the game display
        self.UpdateGameDisplay()

    # Defining method to extract the unique nodes
    def extractUniqueNodes(self, tree_node):
        # Checking if the tree_node is present in the unique node keys
        if id(tree_node) not in self.unique_nodes.keys():
            self.unique_nodes[id(tree_node)] = tree_node
        # Iterating through all the child nodes
        for each_child in tree_node.ChildNodes:
            self.extractUniqueNodes(each_child)

    # Defining method to display the MCTS Tree
    def DisplayTreeFunction(self):
        from copy import deepcopy
        # Finding current game player
        currentPlayer = self.__game.FindCurrentPlayer()
        # Finding current game player
        # currentPlayer = self.__game.FindCurrentPlayer(self.__game.BoardPositions)
        print(f"Current Player Character : {currentPlayer.Character}")
        
        # Fetching the MCTS Information
        game_tree = deepcopy(currentPlayer.GameTree)
        
        self.unique_nodes = { }
        self.extractUniqueNodes(game_tree)
        
        # print(f"Game Tree: {game_tree}, Type: {type(game_tree)}")
        
        from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem, QScrollArea, QVBoxLayout, QFrame
        from PySide6.QtGui import QPainter, QPen, QColor
        from PySide6.QtCore import Qt
        import matplotlib.pyplot as plt
        import networkx as nx
        from networkx.drawing.nx_agraph import graphviz_layout
        from GraphicsViewScene import GraphScene

        # Creating a new directed graph
        graph = nx.DiGraph()

        # unique_nodes = None
        unique_nodes = deepcopy(self.unique_nodes)
        
        # list out keys and values separately
        uniqueNodes_Keys = list(unique_nodes.keys())
        uniqueNodes_Values = list(unique_nodes.values())
 
        # print key with val 100
        # position = val_list.index(100)
        # print(key_list[position])

        graph.clear()

        for each_key in unique_nodes.keys():
            # Extracting the game tree object from dictionary
            node_data = unique_nodes[each_key]
            # Fetching the parent value
            parent_node = node_data.ParentNode
            # Checking if parent node is valid
            if parent_node:
                parent_position = uniqueNodes_Keys[uniqueNodes_Values.index(parent_node)]
                node_position = uniqueNodes_Keys[uniqueNodes_Values.index(node_data)]
                graph.add_edge(parent_position, node_position)
            else:
                continue

        # dict_values = list(node.treeStructure)
        # Creating the layout for the nodes
        layout = graphviz_layout(graph, prog="twopi", args='')

        # Defining the node size
        node_size = 20

        # view = None
        # self.view = QGraphicsView()
        view = 0
        # if self.scene:
            
        #     # self.scroll_area.close()
        #     self.view.destroy
        #     del self.view
        #     # self.view.deleteLater()
        #     self.v_layout.removeWidget(self.scroll_area)
        #     self.__ui.TreeVisualizer.setLayout(self.v_layout)
        
        self.scene = GraphScene(graph, layout, unique_nodes)
        # print(f"Scenes Views: {self.scene.views.__dict__}")
        # self.scene.setSceneRect(0,0, 800, 400)
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.scene.drawGraph()
        # Create a QScrollArea
        # self.scroll_area = QScrollArea()
        # self.scroll_area.setWidget(self.view)
        # self.scroll_area.setWidgetResizable(True)  # Allow the view to resize with the scroll area
        # self.v_layout = QVBoxLayout()
        # self.v_layout.addWidget(self.scroll_area)
        
        self.__ui.TreeVisualizer.setWidget(self.view)
        self.__ui.TreeVisualizer.setWidgetResizable(True)
        
        # self.__ui.TreeVisualizer.setLayout(self.v_layout)
        
        self.UpdateGameDisplay()
        
        # Set the QScrollArea as the central widget
        # window = QMainWindow()
        # window.setCentralWidget(scroll_area)

        # # Show the main window
        # window.show()
        # application.exec()