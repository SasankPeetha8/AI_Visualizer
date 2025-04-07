# -*- coding: utf-8 -*-
import sys, os
from pathlib import Path
resource_file_path = Path(os.getcwd()).joinpath(Path("./UI/Resources"))
sys.path.append(str(resource_file_path))

################################################################################
## Form generated from reading UI file 'NewGameMessageBox.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QButtonGroup, QCheckBox,
    QComboBox, QDialog, QDialogButtonBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_NewGameDialog(object):
    def setupUi(self, NewGameDialog):
        if not NewGameDialog.objectName():
            NewGameDialog.setObjectName(u"NewGameDialog")
        NewGameDialog.resize(453, 268)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewGameDialog.sizePolicy().hasHeightForWidth())
        NewGameDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(NewGameDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.WelcomeLabel = QLabel(NewGameDialog)
        self.WelcomeLabel.setObjectName(u"WelcomeLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.WelcomeLabel.sizePolicy().hasHeightForWidth())
        self.WelcomeLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(13)
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setScaledContents(False)
        self.WelcomeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.WelcomeLabel)

        self.ChoiceFrame = QFrame(NewGameDialog)
        self.ChoiceFrame.setObjectName(u"ChoiceFrame")
        sizePolicy.setHeightForWidth(self.ChoiceFrame.sizePolicy().hasHeightForWidth())
        self.ChoiceFrame.setSizePolicy(sizePolicy)
        self.ChoiceFrame.setFrameShape(QFrame.StyledPanel)
        self.ChoiceFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ChoiceFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ChoiceText = QLabel(self.ChoiceFrame)
        self.ChoiceText.setObjectName(u"ChoiceText")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ChoiceText.sizePolicy().hasHeightForWidth())
        self.ChoiceText.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.ChoiceText)

        self.ChoiceMenu = QComboBox(self.ChoiceFrame)
        self.ChoiceMenu.addItem("")
        self.ChoiceMenu.addItem("")
        self.ChoiceMenu.addItem("")
        self.ChoiceMenu.addItem("")
        self.ChoiceMenu.addItem("")
        self.ChoiceMenu.addItem("")
        self.ChoiceMenu.setObjectName(u"ChoiceMenu")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ChoiceMenu.sizePolicy().hasHeightForWidth())
        self.ChoiceMenu.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.ChoiceMenu)


        self.verticalLayout.addWidget(self.ChoiceFrame)

        self.PlayerOptions = QGroupBox(NewGameDialog)
        self.PlayerOptions.setObjectName(u"PlayerOptions")
        sizePolicy.setHeightForWidth(self.PlayerOptions.sizePolicy().hasHeightForWidth())
        self.PlayerOptions.setSizePolicy(sizePolicy)
        self.PlayerOptions.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.PlayerOptions.setFlat(False)
        self.verticalLayout_3 = QVBoxLayout(self.PlayerOptions)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.PlayerXFrame = QFrame(self.PlayerOptions)
        self.PlayerXFrame.setObjectName(u"PlayerXFrame")
        sizePolicy.setHeightForWidth(self.PlayerXFrame.sizePolicy().hasHeightForWidth())
        self.PlayerXFrame.setSizePolicy(sizePolicy)
        self.PlayerXFrame.setFrameShape(QFrame.StyledPanel)
        self.PlayerXFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.PlayerXFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PlayerXLabel = QLabel(self.PlayerXFrame)
        self.PlayerXLabel.setObjectName(u"PlayerXLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.PlayerXLabel.sizePolicy().hasHeightForWidth())
        self.PlayerXLabel.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.PlayerXLabel)

        self.PlayerXManualBox = QCheckBox(self.PlayerXFrame)
        self.PlayerXGroup = QButtonGroup(NewGameDialog)
        self.PlayerXGroup.setObjectName(u"PlayerXGroup")
        self.PlayerXGroup.addButton(self.PlayerXManualBox)
        self.PlayerXManualBox.setObjectName(u"PlayerXManualBox")

        self.horizontalLayout_2.addWidget(self.PlayerXManualBox)

        self.PlayerXRandomBox = QCheckBox(self.PlayerXFrame)
        self.PlayerXGroup.addButton(self.PlayerXRandomBox)
        self.PlayerXRandomBox.setObjectName(u"PlayerXRandomBox")

        self.horizontalLayout_2.addWidget(self.PlayerXRandomBox)

        self.PlayerXAIBox = QCheckBox(self.PlayerXFrame)
        self.PlayerXGroup.addButton(self.PlayerXAIBox)
        self.PlayerXAIBox.setObjectName(u"PlayerXAIBox")

        self.horizontalLayout_2.addWidget(self.PlayerXAIBox)


        self.verticalLayout_3.addWidget(self.PlayerXFrame)

        self.PlayerOFrame = QFrame(self.PlayerOptions)
        self.PlayerOFrame.setObjectName(u"PlayerOFrame")
        sizePolicy.setHeightForWidth(self.PlayerOFrame.sizePolicy().hasHeightForWidth())
        self.PlayerOFrame.setSizePolicy(sizePolicy)
        self.PlayerOFrame.setFrameShape(QFrame.StyledPanel)
        self.PlayerOFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.PlayerOFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PlayerOLabel = QLabel(self.PlayerOFrame)
        self.PlayerOLabel.setObjectName(u"PlayerOLabel")
        sizePolicy4.setHeightForWidth(self.PlayerOLabel.sizePolicy().hasHeightForWidth())
        self.PlayerOLabel.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.PlayerOLabel)

        self.PlayerOManualBox = QCheckBox(self.PlayerOFrame)
        self.PlayerOGroup = QButtonGroup(NewGameDialog)
        self.PlayerOGroup.setObjectName(u"PlayerOGroup")
        self.PlayerOGroup.addButton(self.PlayerOManualBox)
        self.PlayerOManualBox.setObjectName(u"PlayerOManualBox")

        self.horizontalLayout.addWidget(self.PlayerOManualBox)

        self.PlayerORandomBox = QCheckBox(self.PlayerOFrame)
        self.PlayerOGroup.addButton(self.PlayerORandomBox)
        self.PlayerORandomBox.setObjectName(u"PlayerORandomBox")

        self.horizontalLayout.addWidget(self.PlayerORandomBox)

        self.PlayerOAIBox = QCheckBox(self.PlayerOFrame)
        self.PlayerOGroup.addButton(self.PlayerOAIBox)
        self.PlayerOAIBox.setObjectName(u"PlayerOAIBox")

        self.horizontalLayout.addWidget(self.PlayerOAIBox)


        self.verticalLayout_3.addWidget(self.PlayerOFrame)


        self.verticalLayout.addWidget(self.PlayerOptions)

        self.DialogButtons = QDialogButtonBox(NewGameDialog)
        self.DialogButtons.setObjectName(u"DialogButtons")
        self.DialogButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.DialogButtons.setCenterButtons(True)

        self.verticalLayout.addWidget(self.DialogButtons)


        self.retranslateUi(NewGameDialog)

        QMetaObject.connectSlotsByName(NewGameDialog)
    # setupUi

    def retranslateUi(self, NewGameDialog):
        NewGameDialog.setWindowTitle(QCoreApplication.translate("NewGameDialog", u"New Game Options", None))
        self.WelcomeLabel.setText(QCoreApplication.translate("NewGameDialog", u"Welcome to Tic-Tac-Toe Game", None))
        self.ChoiceText.setText(QCoreApplication.translate("NewGameDialog", u"Select your Board Choice:", None))
        self.ChoiceMenu.setItemText(0, QCoreApplication.translate("NewGameDialog", u"3 x 3", None))
        self.ChoiceMenu.setItemText(1, QCoreApplication.translate("NewGameDialog", u"4 x 4", None))
        self.ChoiceMenu.setItemText(2, QCoreApplication.translate("NewGameDialog", u"5 x 5", None))
        self.ChoiceMenu.setItemText(3, QCoreApplication.translate("NewGameDialog", u"6 x 6", None))
        self.ChoiceMenu.setItemText(4, QCoreApplication.translate("NewGameDialog", u"7 x 7", None))
        self.ChoiceMenu.setItemText(5, QCoreApplication.translate("NewGameDialog", u"8 x 8", None))

        self.PlayerOptions.setTitle(QCoreApplication.translate("NewGameDialog", u"Player Options", None))
        self.PlayerXLabel.setText(QCoreApplication.translate("NewGameDialog", u"Player X :", None))
        self.PlayerXManualBox.setText(QCoreApplication.translate("NewGameDialog", u"Manual", None))
        self.PlayerXRandomBox.setText(QCoreApplication.translate("NewGameDialog", u"Random", None))
        self.PlayerXAIBox.setText(QCoreApplication.translate("NewGameDialog", u"AI (MCTS)", None))
        self.PlayerOLabel.setText(QCoreApplication.translate("NewGameDialog", u"Player O :", None))
        self.PlayerOManualBox.setText(QCoreApplication.translate("NewGameDialog", u"Manual", None))
        self.PlayerORandomBox.setText(QCoreApplication.translate("NewGameDialog", u"Random", None))
        self.PlayerOAIBox.setText(QCoreApplication.translate("NewGameDialog", u"AI (MCTS)", None))
    # retranslateUi

