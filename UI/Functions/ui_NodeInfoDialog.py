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
    QFormLayout, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_NodeDialog(object):
    def setupUi(self, NodeDialog):
        if not NodeDialog.objectName():
            NodeDialog.setObjectName(u"NodeDialog")
        NodeDialog.resize(486, 394)
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
        self.formLayout = QFormLayout(self.WinStatusFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.nodeTypeLabel = QLabel(self.WinStatusFrame)
        self.nodeTypeLabel.setObjectName(u"nodeTypeLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.nodeTypeLabel)

        self.nodeTypeValue = QLabel(self.WinStatusFrame)
        self.nodeTypeValue.setObjectName(u"nodeTypeValue")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.nodeTypeValue)

        self.nodeWinLabel = QLabel(self.WinStatusFrame)
        self.nodeWinLabel.setObjectName(u"nodeWinLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.nodeWinLabel.sizePolicy().hasHeightForWidth())
        self.nodeWinLabel.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.nodeWinLabel)

        self.nodeWinValue = QLabel(self.WinStatusFrame)
        self.nodeWinValue.setObjectName(u"nodeWinValue")
        sizePolicy1.setHeightForWidth(self.nodeWinValue.sizePolicy().hasHeightForWidth())
        self.nodeWinValue.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.nodeWinValue)

        self.nodeVisitLabel = QLabel(self.WinStatusFrame)
        self.nodeVisitLabel.setObjectName(u"nodeVisitLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.nodeVisitLabel)

        self.nodeVisitValue = QLabel(self.WinStatusFrame)
        self.nodeVisitValue.setObjectName(u"nodeVisitValue")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.nodeVisitValue)

        self.childNodeLabel = QLabel(self.WinStatusFrame)
        self.childNodeLabel.setObjectName(u"childNodeLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.childNodeLabel)

        self.childNodeValue = QLabel(self.WinStatusFrame)
        self.childNodeValue.setObjectName(u"childNodeValue")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.childNodeValue)

        self.createIterationLabel = QLabel(self.WinStatusFrame)
        self.createIterationLabel.setObjectName(u"createIterationLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.createIterationLabel)

        self.createIterationValue = QLabel(self.WinStatusFrame)
        self.createIterationValue.setObjectName(u"createIterationValue")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.createIterationValue)

        self.bestNodeLabel = QLabel(self.WinStatusFrame)
        self.bestNodeLabel.setObjectName(u"bestNodeLabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.bestNodeLabel)

        self.bestNodeValue = QLabel(self.WinStatusFrame)
        self.bestNodeValue.setObjectName(u"bestNodeValue")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.bestNodeValue)

        self.bestNodeIterationsLabel = QLabel(self.WinStatusFrame)
        self.bestNodeIterationsLabel.setObjectName(u"bestNodeIterationsLabel")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.bestNodeIterationsLabel)

        self.bestNodeIterationsValue = QLabel(self.WinStatusFrame)
        self.bestNodeIterationsValue.setObjectName(u"bestNodeIterationsValue")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.bestNodeIterationsValue)

        self.nodeDepthValue = QLabel(self.WinStatusFrame)
        self.nodeDepthValue.setObjectName(u"nodeDepthValue")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.nodeDepthValue)

        self.nodeDepthLabel = QLabel(self.WinStatusFrame)
        self.nodeDepthLabel.setObjectName(u"nodeDepthLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.nodeDepthLabel)


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
        self.nodeTypeLabel.setText(QCoreApplication.translate("NodeDialog", u"Node Type", None))
        self.nodeTypeValue.setText(QCoreApplication.translate("NodeDialog", u"TextLabel", None))
        self.nodeWinLabel.setText(QCoreApplication.translate("NodeDialog", u"Win Rate:", None))
        self.nodeWinValue.setText(QCoreApplication.translate("NodeDialog", u"TextLabel", None))
        self.nodeVisitLabel.setText(QCoreApplication.translate("NodeDialog", u"Visit Count", None))
        self.nodeVisitValue.setText(QCoreApplication.translate("NodeDialog", u"TextLabel", None))
        self.childNodeLabel.setText(QCoreApplication.translate("NodeDialog", u"Available Child Nodes", None))
        self.childNodeValue.setText(QCoreApplication.translate("NodeDialog", u"TextLabel", None))
        self.createIterationLabel.setText(QCoreApplication.translate("NodeDialog", u"Created at Iteration", None))
        self.createIterationValue.setText(QCoreApplication.translate("NodeDialog", u"TextLabel", None))
        self.bestNodeLabel.setText(QCoreApplication.translate("NodeDialog", u"Best Node", None))
        self.bestNodeValue.setText(QCoreApplication.translate("NodeDialog", u"TextLabel", None))
        self.bestNodeIterationsLabel.setText(QCoreApplication.translate("NodeDialog", u"Minium Iterations required for best Node", None))
        self.bestNodeIterationsValue.setText(QCoreApplication.translate("NodeDialog", u"TextLabel", None))
        self.nodeDepthValue.setText(QCoreApplication.translate("NodeDialog", u"TextLabel", None))
        self.nodeDepthLabel.setText(QCoreApplication.translate("NodeDialog", u"Node Depth", None))
        self.previousMoveButton.setText(QCoreApplication.translate("NodeDialog", u"Previous State", None))
        self.nextMoveButton.setText(QCoreApplication.translate("NodeDialog", u"Next State", None))
    # retranslateUi

