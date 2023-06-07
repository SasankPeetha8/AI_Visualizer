# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NodeInfoDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_NodeDialog(object):
    def setupUi(self, NodeDialog):
        if not NodeDialog.objectName():
            NodeDialog.setObjectName(u"NodeDialog")
        NodeDialog.resize(453, 268)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NodeDialog.sizePolicy().hasHeightForWidth())
        NodeDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(NodeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.NodeStateLabel = QLabel(NodeDialog)
        self.NodeStateLabel.setObjectName(u"NodeStateLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.NodeStateLabel.sizePolicy().hasHeightForWidth())
        self.NodeStateLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(13)
        self.NodeStateLabel.setFont(font)
        self.NodeStateLabel.setScaledContents(False)
        self.NodeStateLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.NodeStateLabel)

        self.ChoiceFrame = QFrame(NodeDialog)
        self.ChoiceFrame.setObjectName(u"ChoiceFrame")
        sizePolicy.setHeightForWidth(self.ChoiceFrame.sizePolicy().hasHeightForWidth())
        self.ChoiceFrame.setSizePolicy(sizePolicy)
        self.ChoiceFrame.setFrameShape(QFrame.StyledPanel)
        self.ChoiceFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ChoiceFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.NodeLabelInfo = QLabel(self.ChoiceFrame)
        self.NodeLabelInfo.setObjectName(u"NodeLabelInfo")
        sizePolicy.setHeightForWidth(self.NodeLabelInfo.sizePolicy().hasHeightForWidth())
        self.NodeLabelInfo.setSizePolicy(sizePolicy)
        self.NodeLabelInfo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.NodeLabelInfo)


        self.verticalLayout.addWidget(self.ChoiceFrame)

        self.WinStatusFrame = QFrame(NodeDialog)
        self.WinStatusFrame.setObjectName(u"WinStatusFrame")
        self.WinStatusFrame.setFrameShape(QFrame.StyledPanel)
        self.WinStatusFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.WinStatusFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.nodeWinLabel = QLabel(self.WinStatusFrame)
        self.nodeWinLabel.setObjectName(u"nodeWinLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.nodeWinLabel.sizePolicy().hasHeightForWidth())
        self.nodeWinLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.nodeWinLabel)

        self.nodeWinValue = QLabel(self.WinStatusFrame)
        self.nodeWinValue.setObjectName(u"nodeWinValue")
        sizePolicy1.setHeightForWidth(self.nodeWinValue.sizePolicy().hasHeightForWidth())
        self.nodeWinValue.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.nodeWinValue)


        self.verticalLayout.addWidget(self.WinStatusFrame)

        self.ButtonsFrame = QFrame(NodeDialog)
        self.ButtonsFrame.setObjectName(u"ButtonsFrame")
        self.ButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.ButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.ButtonsFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.previousMoveButton = QPushButton(self.ButtonsFrame)
        self.previousMoveButton.setObjectName(u"previousMoveButton")
        sizePolicy1.setHeightForWidth(self.previousMoveButton.sizePolicy().hasHeightForWidth())
        self.previousMoveButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.previousMoveButton)

        self.nextMoveButton = QPushButton(self.ButtonsFrame)
        self.nextMoveButton.setObjectName(u"nextMoveButton")
        sizePolicy1.setHeightForWidth(self.nextMoveButton.sizePolicy().hasHeightForWidth())
        self.nextMoveButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.nextMoveButton)


        self.verticalLayout.addWidget(self.ButtonsFrame)

        self.DialogButtons = QDialogButtonBox(NodeDialog)
        self.DialogButtons.setObjectName(u"DialogButtons")
        self.DialogButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.DialogButtons.setCenterButtons(True)

        self.verticalLayout.addWidget(self.DialogButtons)


        self.retranslateUi(NodeDialog)

        QMetaObject.connectSlotsByName(NodeDialog)
    # setupUi

    def retranslateUi(self, NodeDialog):
        NodeDialog.setWindowTitle(QCoreApplication.translate("NodeDialog", u"Node Information", None))
        self.NodeStateLabel.setText(QCoreApplication.translate("NodeDialog", u"Node State:", None))
        self.NodeLabelInfo.setText(QCoreApplication.translate("NodeDialog", u"Label Information:", None))
        self.nodeWinLabel.setText(QCoreApplication.translate("NodeDialog", u"Node Win Rate:", None))
        self.nodeWinValue.setText(QCoreApplication.translate("NodeDialog", u"TextLabel", None))
        self.previousMoveButton.setText(QCoreApplication.translate("NodeDialog", u"Previous State", None))
        self.nextMoveButton.setText(QCoreApplication.translate("NodeDialog", u"Next State", None))
    # retranslateUi

