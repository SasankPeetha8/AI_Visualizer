# -*- coding: utf-8 -*-
import sys, os
from pathlib import Path
resource_file_path = Path(os.getcwd()).joinpath(Path("./UI/Resources"))
sys.path.append(str(resource_file_path))

################################################################################
## Form generated from reading UI file 'RandomMoveWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QPushButton, QSizePolicy, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(245, 78)
        self.horizontalLayout = QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.RandomMoveFrame = QGroupBox(Frame)
        self.RandomMoveFrame.setObjectName(u"RandomMoveFrame")
        self.horizontalLayout_3 = QHBoxLayout(self.RandomMoveFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.RandomMoveButton = QPushButton(self.RandomMoveFrame)
        self.RandomMoveButton.setObjectName(u"RandomMoveButton")

        self.horizontalLayout_3.addWidget(self.RandomMoveButton)


        self.horizontalLayout.addWidget(self.RandomMoveFrame)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.RandomMoveFrame.setTitle(QCoreApplication.translate("Frame", u"Random Move Options", None))
        self.RandomMoveButton.setText(QCoreApplication.translate("Frame", u"Make a Random Move", None))
    # retranslateUi

