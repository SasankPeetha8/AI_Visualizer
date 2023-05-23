# Importing the math module
from math import sqrt
# Defining the class for the game tree
class Tree():
    """Defining the class for the game tree"""
    def __init__(self, current_state, possible_states, parent=None ):
        # Defining the parent node
        self.__ParentNode = parent
        # Defining the current state of the node
        self.__NodeState = current_state
        # Defining the child nodes
        self.__ChildNodes = []
        # Defining the Node visits
        self.__NodeVisits = 0
        # Defining the node score
        self.__NodeScore = 0
        # Defining boolean value to check if the node is a leaf node
        self.__Is_Leafnode = True
        # Defining list to store all the possible states
        self.__PossibleStates = possible_states
        
    # Defining the properties
    @property
    def ParentNode(self):
        return self.__ParentNode
    
    @ParentNode.setter
    def ParentNode(self, val):
        self.__ParentNode = val
    
    @property
    def ChildNodes(self):
        return self.__ChildNodes[:]
    
    @ChildNodes.setter
    def ChildNodes(self, list_data):
        # Checking if the length is equal or not
        self.__ChildNodes = list_data[:]
    
    @property
    def NodeState(self):
        return self.__NodeState[:]
    
    @NodeState.setter
    def NodeState(self, list_data):
        # Checking if the length is equal or not
        if len(self.NodeState) == len(list_data):
            self.__NodeState = list_data[:]
        else:
            raise Exception("Invalid Node State")
        
    @property
    def NodeVisits(self):
        return self.__NodeVisits
    
    @NodeVisits.setter
    def NodeVisits(self, value):
        self.__NodeVisits = value
        
    @property
    def NodeScore(self):
        return self.__NodeScore
    
    @NodeScore.setter
    def NodeScore(self, value):
        self.__NodeScore = value
        
    @property
    def Is_Leafnode(self):
        return self.__Is_Leafnode
    
    @Is_Leafnode.setter
    def Is_Leafnode(self, value):
        # if type(value) == "bool":
        #     self.__Is_Leafnode = value
        # else:
        #     raise Exception("Invalid boolean for Is_Leafnode")
        self.__Is_Leafnode = value
        

    @property
    def PossibleStates(self):
        return self.__PossibleStates[:]
    
    @PossibleStates.setter
    def PossibleStates(self, list_data):
        self.__PossibleStates[:] = list_data[:]
        
    # Defining the method to display the board.
    def __str__(self, list_data=None):
        """
        Summary:
        --------
        This method is used to display the current board positions.
        Returns:
        --------
        game_positions : str
            It returns the current board positions in the form of a string.
        """
        # Fetching the board positions
        positions = self.NodeState if list_data == None else list_data
        # Creating a string to display the positions of the game.
        game_positions = "\n"
        # Fetching the board size
        board_size = sqrt(len(positions))
        # Converting the board size to integer
        board_size = int(board_size)
        # Iterating through all the positions.
        for each_position in range(1, len(positions)+1):
            # Adding elements to the string appropriately.
            game_positions = game_positions + f" {positions[each_position-1]} " 
            game_positions = f"{game_positions}\n" if each_position % board_size == 0 else f"{game_positions}"
        # Returning the Positions of the Game.
        return game_positions