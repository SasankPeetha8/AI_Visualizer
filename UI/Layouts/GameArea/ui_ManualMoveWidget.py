# -*- coding: utf-8 -*-
import sys, os
from pathlib import Path
resource_file_path = Path(os.getcwd()).joinpath(Path("./UI/Resources"))
sys.path.append(str(resource_file_path))

################################################################################
## Form generated from reading UI file 'ManualMoveWidget.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ManualMoveWidget(object):
    def setupUi(self, ManualMoveWidget):
        if not ManualMoveWidget.objectName():
            ManualMoveWidget.setObjectName(u"ManualMoveWidget")
        ManualMoveWidget.resize(358, 135)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ManualMoveWidget.sizePolicy().hasHeightForWidth())
        ManualMoveWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(ManualMoveWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ManuaMoveFrame = QGroupBox(ManualMoveWidget)
        self.ManuaMoveFrame.setObjectName(u"ManuaMoveFrame")
        self.verticalLayout_4 = QVBoxLayout(self.ManuaMoveFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ManualOptionsFrame = QFrame(self.ManuaMoveFrame)
        self.ManualOptionsFrame.setObjectName(u"ManualOptionsFrame")
        self.ManualOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.ManualOptionsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.ManualOptionsFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ManualMoveLabel = QLabel(self.ManualOptionsFrame)
        self.ManualMoveLabel.setObjectName(u"ManualMoveLabel")

        self.horizontalLayout_2.addWidget(self.ManualMoveLabel)

        self.ManualLineInput = QLineEdit(self.ManualOptionsFrame)
        self.ManualLineInput.setObjectName(u"ManualLineInput")

        self.horizontalLayout_2.addWidget(self.ManualLineInput)


        self.verticalLayout_4.addWidget(self.ManualOptionsFrame)

        self.ManualMoveButton = QPushButton(self.ManuaMoveFrame)
        self.ManualMoveButton.setObjectName(u"ManualMoveButton")

        self.verticalLayout_4.addWidget(self.ManualMoveButton)


        self.horizontalLayout.addWidget(self.ManuaMoveFrame)


        self.retranslateUi(ManualMoveWidget)

        QMetaObject.connectSlotsByName(ManualMoveWidget)
    # setupUi

    def retranslateUi(self, ManualMoveWidget):
        ManualMoveWidget.setWindowTitle(QCoreApplication.translate("ManualMoveWidget", u"Frame", None))
        self.ManuaMoveFrame.setTitle(QCoreApplication.translate("ManualMoveWidget", u"Manual Move Options", None))
        self.ManualMoveLabel.setText(QCoreApplication.translate("ManualMoveWidget", u"Enter your move: ", None))
        self.ManualLineInput.setText("")
        self.ManualMoveButton.setText(QCoreApplication.translate("ManualMoveWidget", u"Make Manual Move", None))
    # retranslateUi

