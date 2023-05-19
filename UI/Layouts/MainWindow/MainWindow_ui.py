# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QToolBar, QVBoxLayout, QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1107, 839)
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
        icon2 = QIcon()
        icon2.addFile(u":/Icons/GameSave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSaveGame.setIcon(icon2)
        self.actionCloseGame = QAction(MainWindow)
        self.actionCloseGame.setObjectName(u"actionCloseGame")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/GameClose.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCloseGame.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(False)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.GameRegion = QFrame(self.centralwidget)
        self.GameRegion.setObjectName(u"GameRegion")
        self.GameRegion.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
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
        self.GameDisplayFrame.setEnabled(False)
        self.GameDisplayFrame.setFrameShape(QFrame.StyledPanel)
        self.GameDisplayFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.GameDisplayFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.GameDisplayLabel = QLabel(self.GameDisplayFrame)
        self.GameDisplayLabel.setObjectName(u"GameDisplayLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.GameDisplayLabel.sizePolicy().hasHeightForWidth())
        self.GameDisplayLabel.setSizePolicy(sizePolicy1)
        self.GameDisplayLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.GameDisplayLabel)

        self.pushButton = QPushButton(self.GameDisplayFrame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.GameInfoLabel = QLabel(self.GameDisplayFrame)
        self.GameInfoLabel.setObjectName(u"GameInfoLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.GameInfoLabel.sizePolicy().hasHeightForWidth())
        self.GameInfoLabel.setSizePolicy(sizePolicy2)
        self.GameInfoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.GameInfoLabel)


        self.verticalLayout.addWidget(self.GameDisplayFrame)


        self.horizontalLayout.addWidget(self.GameRegion)

        self.TreeVisualizer = QFrame(self.centralwidget)
        self.TreeVisualizer.setObjectName(u"TreeVisualizer")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.TreeVisualizer.sizePolicy().hasHeightForWidth())
        self.TreeVisualizer.setSizePolicy(sizePolicy3)
        self.TreeVisualizer.setFrameShape(QFrame.StyledPanel)
        self.TreeVisualizer.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.TreeVisualizer)

        self.MCTS_Frame = QFrame(self.centralwidget)
        self.MCTS_Frame.setObjectName(u"MCTS_Frame")
        self.MCTS_Frame.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.MCTS_Frame.sizePolicy().hasHeightForWidth())
        self.MCTS_Frame.setSizePolicy(sizePolicy4)
        self.MCTS_Frame.setFrameShape(QFrame.StyledPanel)
        self.MCTS_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.MCTS_Frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Selection = QFrame(self.MCTS_Frame)
        self.Selection.setObjectName(u"Selection")
        sizePolicy3.setHeightForWidth(self.Selection.sizePolicy().hasHeightForWidth())
        self.Selection.setSizePolicy(sizePolicy3)
        self.Selection.setFrameShape(QFrame.StyledPanel)
        self.Selection.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.Selection)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 121, 41))

        self.verticalLayout_6.addWidget(self.Selection)

        self.frame = QFrame(self.MCTS_Frame)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 40, 91, 41))

        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.MCTS_Frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 30, 111, 31))

        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.MCTS_Frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 10, 141, 51))

        self.verticalLayout_6.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.MCTS_Frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1107, 22))
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.GameInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Create a New Game / Load Existing Game", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Selection Phase", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Expansion Phase", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Simulation Phase", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Backpropagation Phase", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

