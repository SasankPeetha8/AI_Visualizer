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
        self.nodes_stored = [ ]
        self.circles_available = { }
        
        

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
            self.nodes_stored = self.nodes_stored + [ ellipse ]
            # Appending the nodes and circles into a dictionary
            self.circles_available[self.nodeData[node_id]] = ellipse
        
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
        root_node = self.nodes_stored[0]
        # Specifying the colour for the root node
        fillColour = QColor(f"#00a300")
        # Specifying the brush colour for the root node
        brush = QBrush(fillColour)
        # Updating the colour for the root node
        root_node.updateBrushColour(brush)
        # Fetching the best node information
        # best_node = self.fetchBestNode(root_node)
        best_node = self.fetchAllBestNodes(root_node)
        # Fetching the number of visits of the root node
        rootVisits = root_node.node_info.NodeVisits
        # Creating a list
        rootVisits = list(range(1, rootVisits+1))
        # Checking if best_node is valid
        if len(best_node):
            # Specifying the colour for the best node
            fillColour = QColor(f"#ff8b17")
            # Specifying the brush colour for the best node
            brush = QBrush(fillColour)
            for each_circle in best_node:
            # Updating the colour for the best node
                each_circle.updateBrushColour(brush)
                # Updating hte z value to display on the top
                each_circle.zValue = 1
                each_circle.updateZValue()
                # Fetching the node data
                node_iterations = each_circle.node_info.minIterations
                # Extracting the difference
                difference = list(set(rootVisits) - set(node_iterations))
                # Fetching the last value
                each_circle.node_info.best_node = True
                each_circle.node_info.requiredIterations = difference[-1] if len(difference) > 0 else 0
                
    # Defining method to find all the best nodes
    def fetchAllBestNodes(self, circle_data):
        best_circles = self.fetchBestNode(circle_data)
        if best_circles:
            for each_circle in best_circles:
                sub_best_circle = self.fetchAllBestNodes(each_circle)
                if sub_best_circle:
                    best_circles = best_circles + sub_best_circle
        return best_circles        
    
    # def updateRootNodeColor(self):
    #     # Fetching the root node information
    #     root_node = self.nodes_stored[0]
    #     # Specifying the colour
    #     fillColour = QColor(f"#00a300")
    #     # Specifying the brush colour
    #     brush = QBrush(fillColour)
    #     # Updating the brush colour for the root node
    #     root_node.updateBrushColour(brush)
    
    # Fetch the node score value
    def CalculateScore(self, node_data, isNormalise):
        # Calculating the exploitation value
        exploitation_value = node_data.NodeScore/node_data.NodeVisits
        # Calculating the exploration value
        exploration_value = math.sqrt(2) * ( math.sqrt((math.log(node_data.ParentNode.NodeVisits))/node_data.NodeVisits))
        # Calculating the total score
        total_score = exploitation_value + exploration_value
        # Normalising the score
        if total_score > 1 and isNormalise:
            # Fetching all the sibling nodes
            sibling_nodes = node_data.ParentNode.ChildNodes[:]
            sibling_scores = self.fetchAllScores(sibling_nodes)
            total_score = self.normalize_score(total_score, sibling_scores[0], sibling_scores[-1])
        # Returning total score
        return total_score
    
    def fetchAllScores(self, nodes_list):
        scores_list = [ ]
        for each_node in nodes_list:
            score = self.CalculateScore(each_node, False)
            scores_list = scores_list + [ score ]
        # Sorting the list values
        scores_list.sort()
        return scores_list
    
    def normalize_score(self, score, min_score, max_score):
        return score/max_score
    
    def fetchBestNode(self, root_circle):
        # Defining the root node
        root_node = root_circle.node_info
        # Defining initial score
        score = float("-inf")
        # Defining the best node
        best_node = [ ]
        # Checking if the child nodes are valid or not
        if len(root_node.ChildNodes):    
            # Iterating through all the elements
            for child_node in root_node.ChildNodes:
                total_score = self.CalculateScore(child_node, True)
                
                # # Calculating the exploitation value
                # exploitation_value = child_node.NodeScore/child_node.NodeVisits
                # # Calculating the exploration value
                # exploration_value = math.sqrt(2) * ( math.sqrt((math.log10(root_node.NodeVisits))/child_node.NodeVisits))
                # # Calculating the total score
                # total_score = exploitation_value + exploration_value
                # # total_score = round(score, 2)
                # # Checking the total score
                if total_score > score:
                    # Updating the score value
                    score = total_score
                    # updating the list
                    best_node = [ child_node ]
                elif total_score == score:
                    # Updating the list
                    best_node = best_node + [ child_node ]
            
            # Circles found
            circles_found = [ ]
            # Iterating through the circle to find the node
            for each_node in best_node:
                circles_found = circles_found + [ self.circles_available[each_node] ]
                # node_state = each_node.NodeState
                # for each_circle in self.nodes_stored:
                #     # Extracting the node info stored in each circle
                #     circle_state = each_circle.node_info.NodeState
                #     # Checking if the nodes states are matching or not
                #     if node_state == circle_state:
                        
                #         # circles_found = circles_found + [ each_circle ]
                #         circles_found = circles_found + [ self.circles_available[each_circle.node_info] ]
                #         break
                # Continuing with another node
                # continue
                        
            # Returning the best node
            return circles_found
        
        else:
            return False
    
    # Updating the size of all the elements stored
    def modifyNodeSize(self, percent, scope):
        
        # Calculating the size of the node
        if scope == "increase":
            size = 30 - ( 30 * percent)
            size = 30 if size > 30 else size
        elif scope == "decrease":
            size = 30 - ( 30 * percent)
        for each_node in self.nodes_stored:
            each_node.updateNodeSize(size)
            
    # Updating the size of the arrow
    def modifyArrowSize(self, percent, scope):
        # Calculating the size of the arrow
        for each_arrow in self.arrows_stored:
            # Size of the arrow
            points = each_arrow.polygon()
            for each_point in points:
                new_x = each_point.x() - percent