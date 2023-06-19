from PySide6.QtWidgets import QGraphicsView, QGraphicsEllipseItem
from PySide6.QtGui import QPainter, QWheelEvent

class ZoomableGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.scene = scene
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.zoom_factor = 1.2
        self.old_scale = self.transform().m11()
        
    def wheelEvent(self, event):
    # Save the current center point in the view
        oldPos = self.mapToScene(event.position().toPoint())

        # Scale the view
        if event.angleDelta().y() > 0:
            # Zoom in
            self.scale(self.zoom_factor, self.zoom_factor)
        else:
            # Zoom out
            self.scale(1 / self.zoom_factor, 1 / self.zoom_factor)

        # Calculate the new center point after scaling
        newPos = self.mapToScene(event.position().toPoint())

        # Adjust the view to keep the elements at a constant size
        delta = newPos - oldPos
        self.translate(delta.x(), delta.y())
        
    # def __getstate__(self):
    #     state = self.__dict__.copy()
    #     # Remove non-serializable or unwanted attributes
    #     # del state['_customAttribute']
    #     # Add any additional modifications to the state if needed
    #     # ...
    #     return state

    # def __setstate__(self, state):
    #     # Restore the object state from the serialized state
    #     self.__dict__.update(state)
    #     # Perform any additional actions to initialize the object if needed
    #     # ...