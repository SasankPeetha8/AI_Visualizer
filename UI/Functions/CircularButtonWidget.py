# Importing the required modules
from PySide6.QtWidgets import QGraphicsEllipseItem
from PySide6.QtGui import QPen, QBrush, QColor
from PySide6.QtCore import Qt

# Creating a class which inherits the Ellipse Item
class CircularButton(QGraphicsEllipseItem):
    """docstring for CircularButton."""
    def __init__(self, x_pos, y_pos, size, node_data):
        # Returning a Ellipse Item with given X and Y co-ordinates followed by width and height
        super(CircularButton, self).__init__(x_pos, y_pos, size, size)
        
        # Defining the positions
        self.xPosition = x_pos
        self.yPosition = y_pos
        self.size = size
        
        # Defining the node info
        self.node_info = node_data
        
        # Defining the node fill colour
        # self.__fillColour = QColor(f"#00aba9")
        self.__fillColour = QColor(f"#63dbea")
        # Defining the node outline colour
        self.__outlineColour = QColor(f"#1d1d1d")
        # Creating a new pen
        self.__pen = QPen(self.__outlineColour)
        # Creating a new brush
        self.__brush = QBrush(self.__fillColour)
        
        # Specifying to use the pen
        self.setPen(self.__pen)
        # Specifying to use the brush
        self.setBrush(self.__brush)
        
        # Accepting the events
        self.setAcceptHoverEvents(True)
    
    # Defining the mouse press event
    def mousePressEvent(self, event):
        # Checking if the mouse press event is left mouse button
        if event.button() == Qt.LeftButton:
            # Specifying the colour of the brush
            brush = QBrush(Qt.black)
            # Specifying to use the brush
            self.setBrush(brush)
            # print(f"Mouse Left Button is pressed")
            
    # Defining the mouse release event
    def mouseReleaseEvent(self, event):
        # Checking if the mouse release event is left mouse button
        if event.button() == Qt.LeftButton:
            # # Specifying the colour of the brush
            # self.__brush = QBrush(Qt.blue)
            # Specifying to use the brush
            self.setBrush(self.__brush)
            # print(f"Mouse Left Button is released")
            # print(f"{self.node_info}")
            from DialogBox import DialogBox
            dialog_box = DialogBox(self.node_info)
            dialog_box.exec()
            
    # Defining method to update the brush colour
    def updateBrushColour(self, brush_info):
        # # Specifying the colour
        # self.__fillColour = QColor(f"#00a300")
        # # Specifying the brush colour
        # self.__brush = QBrush(self.__fillColour)
        # Specifying to use the brush
        # updating the universal brush colour
        self.__brush = brush_info
        self.setBrush(brush_info)