# -*- coding: utf-8 -*-
import sys, os
from pathlib import Path
resource_file_path = Path(os.getcwd()).joinpath(Path("./UI/Resources"))
sys.path.append(str(resource_file_path))

################################################################################
## Form generated from reading UI file 'CloseGameMessageBox.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_CloseGameDialog(object):
    def setupUi(self, CloseGameDialog):
        if not CloseGameDialog.objectName():
            CloseGameDialog.setObjectName(u"CloseGameDialog")
        CloseGameDialog.resize(326, 120)
        self.verticalLayout = QVBoxLayout(CloseGameDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.WelcomeLabel = QLabel(CloseGameDialog)
        self.WelcomeLabel.setObjectName(u"WelcomeLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WelcomeLabel.sizePolicy().hasHeightForWidth())
        self.WelcomeLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(13)
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setScaledContents(False)
        self.WelcomeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.WelcomeLabel)

        self.ChoiceFrame = QFrame(CloseGameDialog)
        self.ChoiceFrame.setObjectName(u"ChoiceFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ChoiceFrame.sizePolicy().hasHeightForWidth())
        self.ChoiceFrame.setSizePolicy(sizePolicy1)
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
        self.ChoiceText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.ChoiceText)


        self.verticalLayout.addWidget(self.ChoiceFrame)

        self.DialogButtons = QDialogButtonBox(CloseGameDialog)
        self.DialogButtons.setObjectName(u"DialogButtons")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.DialogButtons.sizePolicy().hasHeightForWidth())
        self.DialogButtons.setSizePolicy(sizePolicy3)
        self.DialogButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.DialogButtons.setCenterButtons(True)

        self.verticalLayout.addWidget(self.DialogButtons)


        self.retranslateUi(CloseGameDialog)

        QMetaObject.connectSlotsByName(CloseGameDialog)
    # setupUi

    def retranslateUi(self, CloseGameDialog):
        CloseGameDialog.setWindowTitle(QCoreApplication.translate("CloseGameDialog", u"Close Game", None))
        self.WelcomeLabel.setText(QCoreApplication.translate("CloseGameDialog", u"Close Game", None))
        self.ChoiceText.setText(QCoreApplication.translate("CloseGameDialog", u"Are you sure that you want to close the current game ?", None))
    # retranslateUi

