# -*- coding: utf-8 -*-
import sys, os
from pathlib import Path
resource_file_path = Path(os.getcwd()).joinpath(Path("./UI/Resources"))
sys.path.append(str(resource_file_path))

################################################################################
## Form generated from reading UI file 'MainWindow - Copy.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1078, 749)
        self.actionNewGame = QAction(MainWindow)
        self.actionNewGame.setObjectName(u"actionNewGame")
        icon = QIcon()
        icon.addFile(u":/Icons/GameNew.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewGame.setIcon(icon)
        self.actionLoadGame = QAction(MainWindow)
        self.actionLoadGame.setObjectName(u"actionLoadGame")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/GameOpen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLoadGame.setIcon(icon1)
        self.actionSaveGame = QAction(MainWindow)
        self.actionSaveGame.setObjectName(u"actionSaveGame")
        self.actionSaveGame.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/GameSave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSaveGame.setIcon(icon2)
        self.actionCloseGame = QAction(MainWindow)
        self.actionCloseGame.setObjectName(u"actionCloseGame")
        self.actionCloseGame.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/GameClose.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCloseGame.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.GameRegion = QFrame(self.centralwidget)
        self.GameRegion.setObjectName(u"GameRegion")
        self.GameRegion.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GameRegion.sizePolicy().hasHeightForWidth())
        self.GameRegion.setSizePolicy(sizePolicy)
        self.GameRegion.setFrameShape(QFrame.NoFrame)
        self.GameRegion.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.GameRegion)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.GameDisplayFrame = QFrame(self.GameRegion)
        self.GameDisplayFrame.setObjectName(u"GameDisplayFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.GameDisplayFrame.sizePolicy().hasHeightForWidth())
        self.GameDisplayFrame.setSizePolicy(sizePolicy1)
        self.GameDisplayFrame.setFrameShape(QFrame.StyledPanel)
        self.GameDisplayFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.GameDisplayFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.GameDisplayLabel = QLabel(self.GameDisplayFrame)
        self.GameDisplayLabel.setObjectName(u"GameDisplayLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.GameDisplayLabel.sizePolicy().hasHeightForWidth())
        self.GameDisplayLabel.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(13)
        self.GameDisplayLabel.setFont(font)
        self.GameDisplayLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.GameDisplayLabel)

        self.GameInfoLabel = QLabel(self.GameDisplayFrame)
        self.GameInfoLabel.setObjectName(u"GameInfoLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.GameInfoLabel.sizePolicy().hasHeightForWidth())
        self.GameInfoLabel.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(10)
        self.GameInfoLabel.setFont(font1)
        self.GameInfoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.GameInfoLabel)


        self.verticalLayout.addWidget(self.GameDisplayFrame)

        self.ManualMoveFrame = QGroupBox(self.GameRegion)
        self.ManualMoveFrame.setObjectName(u"ManualMoveFrame")
        sizePolicy1.setHeightForWidth(self.ManualMoveFrame.sizePolicy().hasHeightForWidth())
        self.ManualMoveFrame.setSizePolicy(sizePolicy1)
        self.ManualMoveFrame.setCheckable(False)
        self.ManualMoveFrame.setChecked(False)
        self.verticalLayout_3 = QVBoxLayout(self.ManualMoveFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ManualOptionsFrame = QFrame(self.ManualMoveFrame)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ManualLineInput.sizePolicy().hasHeightForWidth())
        self.ManualLineInput.setSizePolicy(sizePolicy4)
        self.ManualLineInput.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.ManualLineInput)


        self.verticalLayout_3.addWidget(self.ManualOptionsFrame)

        self.ManualMoveButton = QPushButton(self.ManualMoveFrame)
        self.ManualMoveButton.setObjectName(u"ManualMoveButton")

        self.verticalLayout_3.addWidget(self.ManualMoveButton)


        self.verticalLayout.addWidget(self.ManualMoveFrame)

        self.RandomMoveFrame = QGroupBox(self.GameRegion)
        self.RandomMoveFrame.setObjectName(u"RandomMoveFrame")
        self.horizontalLayout_3 = QHBoxLayout(self.RandomMoveFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.RandomMoveButton = QPushButton(self.RandomMoveFrame)
        self.RandomMoveButton.setObjectName(u"RandomMoveButton")

        self.horizontalLayout_3.addWidget(self.RandomMoveButton)


        self.verticalLayout.addWidget(self.RandomMoveFrame)

        self.AIMoveFrame = QGroupBox(self.GameRegion)
        self.AIMoveFrame.setObjectName(u"AIMoveFrame")
        self.AIMoveFrame.setEnabled(False)
        self.verticalLayout_7 = QVBoxLayout(self.AIMoveFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.AITypeBox = QGroupBox(self.AIMoveFrame)
        self.AITypeBox.setObjectName(u"AITypeBox")
        self.AITypeBox.setEnabled(False)
        self.AITypeBox.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_4 = QHBoxLayout(self.AITypeBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.IterationsCheckBox = QCheckBox(self.AITypeBox)
        self.ThinkingTypeOptions = QButtonGroup(MainWindow)
        self.ThinkingTypeOptions.setObjectName(u"ThinkingTypeOptions")
        self.ThinkingTypeOptions.addButton(self.IterationsCheckBox)
        self.IterationsCheckBox.setObjectName(u"IterationsCheckBox")
        self.IterationsCheckBox.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.IterationsCheckBox.sizePolicy().hasHeightForWidth())
        self.IterationsCheckBox.setSizePolicy(sizePolicy5)
        self.IterationsCheckBox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.IterationsCheckBox)

        self.TimeCheckBox = QCheckBox(self.AITypeBox)
        self.ThinkingTypeOptions.addButton(self.TimeCheckBox)
        self.TimeCheckBox.setObjectName(u"TimeCheckBox")

        self.horizontalLayout_4.addWidget(self.TimeCheckBox)

        self.EnableReUseCheckBox = QCheckBox(self.AITypeBox)
        self.EnableReUseCheckBox.setObjectName(u"EnableReUseCheckBox")
        sizePolicy5.setHeightForWidth(self.EnableReUseCheckBox.sizePolicy().hasHeightForWidth())
        self.EnableReUseCheckBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.EnableReUseCheckBox)


        self.verticalLayout_7.addWidget(self.AITypeBox)

        self.LimitsFrame = QFrame(self.AIMoveFrame)
        self.LimitsFrame.setObjectName(u"LimitsFrame")
        self.LimitsFrame.setFrameShape(QFrame.StyledPanel)
        self.LimitsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.LimitsFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.L_LimitButton = QPushButton(self.LimitsFrame)
        self.L_LimitButton.setObjectName(u"L_LimitButton")

        self.horizontalLayout_5.addWidget(self.L_LimitButton)

        self.M_LimitButton = QPushButton(self.LimitsFrame)
        self.M_LimitButton.setObjectName(u"M_LimitButton")

        self.horizontalLayout_5.addWidget(self.M_LimitButton)

        self.H_LimitButton = QPushButton(self.LimitsFrame)
        self.H_LimitButton.setObjectName(u"H_LimitButton")

        self.horizontalLayout_5.addWidget(self.H_LimitButton)


        self.verticalLayout_7.addWidget(self.LimitsFrame)

        self.ManualEntryFrame = QFrame(self.AIMoveFrame)
        self.ManualEntryFrame.setObjectName(u"ManualEntryFrame")
        self.ManualEntryFrame.setFrameShape(QFrame.StyledPanel)
        self.ManualEntryFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.ManualEntryFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LimitsLabel = QLabel(self.ManualEntryFrame)
        self.LimitsLabel.setObjectName(u"LimitsLabel")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.LimitsLabel.sizePolicy().hasHeightForWidth())
        self.LimitsLabel.setSizePolicy(sizePolicy6)

        self.horizontalLayout_6.addWidget(self.LimitsLabel)

        self.AILimitsEdit = QLineEdit(self.ManualEntryFrame)
        self.AILimitsEdit.setObjectName(u"AILimitsEdit")
        sizePolicy4.setHeightForWidth(self.AILimitsEdit.sizePolicy().hasHeightForWidth())
        self.AILimitsEdit.setSizePolicy(sizePolicy4)

        self.horizontalLayout_6.addWidget(self.AILimitsEdit)


        self.verticalLayout_7.addWidget(self.ManualEntryFrame)

        self.AIBuildTreeButton = QPushButton(self.AIMoveFrame)
        self.AIBuildTreeButton.setObjectName(u"AIBuildTreeButton")

        self.verticalLayout_7.addWidget(self.AIBuildTreeButton)

        self.AIDisplayTreeButton = QPushButton(self.AIMoveFrame)
        self.AIDisplayTreeButton.setObjectName(u"AIDisplayTreeButton")

        self.verticalLayout_7.addWidget(self.AIDisplayTreeButton)

        self.AIMoveButton = QPushButton(self.AIMoveFrame)
        self.AIMoveButton.setObjectName(u"AIMoveButton")

        self.verticalLayout_7.addWidget(self.AIMoveButton)


        self.verticalLayout.addWidget(self.AIMoveFrame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.GameRegion)

        self.TreeVisualizer = QFrame(self.centralwidget)
        self.TreeVisualizer.setObjectName(u"TreeVisualizer")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.TreeVisualizer.sizePolicy().hasHeightForWidth())
        self.TreeVisualizer.setSizePolicy(sizePolicy7)
        self.TreeVisualizer.setFrameShape(QFrame.StyledPanel)
        self.TreeVisualizer.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.TreeVisualizer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1078, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionNewGame)
        self.toolBar.addAction(self.actionLoadGame)
        self.toolBar.addAction(self.actionSaveGame)
        self.toolBar.addAction(self.actionCloseGame)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNewGame.setText(QCoreApplication.translate("MainWindow", u"NewGame", None))
#if QT_CONFIG(tooltip)
        self.actionNewGame.setToolTip(QCoreApplication.translate("MainWindow", u"Start a new game", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionNewGame.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionLoadGame.setText(QCoreApplication.translate("MainWindow", u"LoadGame", None))
#if QT_CONFIG(tooltip)
        self.actionLoadGame.setToolTip(QCoreApplication.translate("MainWindow", u"Load a saved game", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionLoadGame.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSaveGame.setText(QCoreApplication.translate("MainWindow", u"SaveGame", None))
#if QT_CONFIG(tooltip)
        self.actionSaveGame.setToolTip(QCoreApplication.translate("MainWindow", u"Save current game", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSaveGame.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionCloseGame.setText(QCoreApplication.translate("MainWindow", u"CloseGame", None))
#if QT_CONFIG(tooltip)
        self.actionCloseGame.setToolTip(QCoreApplication.translate("MainWindow", u"Close current game", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionCloseGame.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.GameDisplayLabel.setText(QCoreApplication.translate("MainWindow", u"Game Display", None))
        self.GameInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Create a New Game / Load Existing Game", None))
        self.ManualMoveFrame.setTitle(QCoreApplication.translate("MainWindow", u"Manual Move Options", None))
        self.ManualMoveLabel.setText(QCoreApplication.translate("MainWindow", u"Enter your move:", None))
        self.ManualLineInput.setText("")
        self.ManualLineInput.setPlaceholderText("")
        self.ManualMoveButton.setText(QCoreApplication.translate("MainWindow", u"Make Manual Move", None))
        self.RandomMoveFrame.setTitle(QCoreApplication.translate("MainWindow", u"Random Move Options", None))
        self.RandomMoveButton.setText(QCoreApplication.translate("MainWindow", u"Make a Random Move", None))
        self.AIMoveFrame.setTitle(QCoreApplication.translate("MainWindow", u"AI Move Options", None))
        self.AITypeBox.setTitle(QCoreApplication.translate("MainWindow", u"Thinking Type", None))
        self.IterationsCheckBox.setText(QCoreApplication.translate("MainWindow", u"Iterations", None))
        self.TimeCheckBox.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.EnableReUseCheckBox.setText(QCoreApplication.translate("MainWindow", u"Re-Use MCTS Tree", None))
        self.L_LimitButton.setText(QCoreApplication.translate("MainWindow", u"1 Iteration", None))
        self.M_LimitButton.setText(QCoreApplication.translate("MainWindow", u"10 Iterations", None))
        self.H_LimitButton.setText(QCoreApplication.translate("MainWindow", u"100 Iterations", None))
        self.LimitsLabel.setText(QCoreApplication.translate("MainWindow", u"Enter the required limits: ", None))
        self.AILimitsEdit.setText("")
        self.AIBuildTreeButton.setText(QCoreApplication.translate("MainWindow", u"Build MCTS Tree", None))
        self.AIDisplayTreeButton.setText(QCoreApplication.translate("MainWindow", u"Display MCTS Tree", None))
        self.AIMoveButton.setText(QCoreApplication.translate("MainWindow", u"Make AI based Move", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

