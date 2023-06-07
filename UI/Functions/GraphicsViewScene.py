from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPolygonItem
from PySide6.QtGui import QPainter, QPen, QColor, QPolygonF, QBrush
from PySide6.QtCore import Qt, QPointF
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import math
from CircularButtonWidget import CircularButton

class GraphScene(QGraphicsScene):
    def __init__(self, graph, layout, nodes_data):
        super().__init__()
        self.graph = graph
        self.layout = layout
        self.nodeData = nodes_data

    def drawGraph(self):
        # Set up pen for drawing edges
        pen = QPen(Qt.black, 1)
        brush = QBrush(Qt.black)
        arrow = arrow = QPolygonF([QPointF(0, 0), QPointF(-6, -3), QPointF(-6, 3)])

        # Draw nodes
        node_size = 20
        for node_id in self.graph.nodes:
            pos = self.layout[node_id]
            x, y = pos[0], pos[1]
            # ellipse = QGraphicsEllipseItem(x - node_size / 2, y - node_size / 2, node_size, node_size)
            ellipse = CircularButton(x - node_size / 2, y - node_size / 2, node_size, self.nodeData[node_id])
            self.addItem(ellipse)
        
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
