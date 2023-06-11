from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPolygonItem
from PySide6.QtGui import QPainter, QPen, QColor, QPolygonF, QBrush
from PySide6.QtCore import Qt, QPointF
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import math, random
from CircularButtonWidget import CircularButton

class GraphScene(QGraphicsScene):
    def __init__(self, graph, layout, nodes_data):
        super().__init__()
        self.graph = graph
        self.layout = layout
        self.nodeData = nodes_data
        self.__nodes_stored = [ ]

    def drawGraph(self):
        # Set up pen for drawing edges
        # grey colour
        # edge_colour = QColor(f"#918b8b")
        edge_colour = QColor(f"#1d1d1d")
        # pen = QPen(Qt.black, 1)
        # brush = QBrush(Qt.black)
        pen = QPen(edge_colour)
        brush = QBrush(edge_colour)
        arrow = arrow = QPolygonF([QPointF(0, 0), QPointF(-6, -3), QPointF(-6, 3)])

        # Draw nodes
        node_size = 20
        for node_id in self.graph.nodes:
            pos = self.layout[node_id]
            x, y = pos[0], pos[1]
            # ellipse = QGraphicsEllipseItem(x - node_size / 2, y - node_size / 2, node_size, node_size)
            ellipse = CircularButton(x - node_size / 2, y - node_size / 2, node_size, self.nodeData[node_id])
            self.addItem(ellipse)
            # Appending the ellipse buttons into the nodes_stored
            self.__nodes_stored = self.__nodes_stored + [ ellipse ]
        
         # Draw edges with arrows
        for u, v in self.graph.edges:
            pos_u = self.layout[u]
            pos_v = self.layout[v]
            line = QGraphicsLineItem(pos_u[0], pos_u[1], pos_v[0], pos_v[1])
            line.setPen(pen)

            # Calculate the rotation angle for the arrow
            dx = pos_v[0] - pos_u[0]
            dy = pos_v[1] - pos_u[1]
            rotation = math.degrees(math.atan2(dy, dx))

            # Create arrow polygon item and set its position and rotation
            arrow_item = QGraphicsPolygonItem(arrow)
            arrow_item.setPos(pos_v[0], pos_v[1])
            arrow_item.setRotation(rotation)
            arrow_item.setPen(pen)
            arrow_item.setBrush(brush)

            self.addItem(line)
            self.addItem(arrow_item)

    # Update node colours
    def UpdateColors(self):
        # Fetching the root node information
        root_node = self.__nodes_stored[0]
        # Specifying the colour for the root node
        fillColour = QColor(f"#00a300")
        # Specifying the brush colour for the root node
        brush = QBrush(fillColour)
        # Updating the colour for the root node
        root_node.updateBrushColour(brush)
        # Fetching the best node information
        best_node = self.fetchBestNode(root_node)
        # Checking if best_node is valid
        if best_node:
            # Specifying the colour for the best node
            fillColour = QColor(f"#ff8b17")
            # Specifying the brush colour for the best node
            brush = QBrush(fillColour)
            # Updating the colour for the best node
            best_node.updateBrushColour(brush)
    
    # def updateRootNodeColor(self):
    #     # Fetching the root node information
    #     root_node = self.__nodes_stored[0]
    #     # Specifying the colour
    #     fillColour = QColor(f"#00a300")
    #     # Specifying the brush colour
    #     brush = QBrush(fillColour)
    #     # Updating the brush colour for the root node
    #     root_node.updateBrushColour(brush)
        
    def fetchBestNode(self, root_circle):
        # Defining the root node
        root_node = root_circle.node_info
        # Defining initial score
        score = float("-inf")
        # Defining the best node
        best_node = [ ]
        # Iterating through all the elements
        for child_node in root_node.ChildNodes:
            # Calculating the exploitation value
            exploitation_value = child_node.NodeScore/child_node.NodeVisits
            # Calculating the exploration value
            exploration_value = math.sqrt(2) * ( math.sqrt((math.log10(root_node.NodeVisits))/child_node.NodeVisits))
            # Calculating the total score
            total_score = exploitation_value + exploration_value
            # total_score = round(score, 2)
            # Checking the total score
            if total_score > score:
                # Updating the score value
                score = total_score
                # updating the list
                best_node = [ child_node ]
            elif total_score == score:
                # Updating the list
                best_node = best_node + [ child_node ]
        
        best_node =  best_node[0] if len(best_node) == 1 else random.choice(best_node)
        
        # Iterating through the circle to find the node
        for each_circle in self.__nodes_stored:
            # Extracting the node info stored in each circle
            node_data = each_circle.node_info
            # Checking if the nodes states are matching or not
            if best_node.NodeState == node_data.NodeState:
                return each_circle
                    
        # Returning the best node
        return None