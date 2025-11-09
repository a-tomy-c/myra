# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'skin_dialog_add_url.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(596, 206)
        Dialog.setMinimumSize(QSize(0, 206))
        Dialog.setMaximumSize(QSize(16777215, 206))
        Dialog.setModal(False)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_viewer = QLabel(Dialog)
        self.lb_viewer.setObjectName(u"lb_viewer")
        self.lb_viewer.setMinimumSize(QSize(150, 150))
        self.lb_viewer.setMaximumSize(QSize(120, 120))
        self.lb_viewer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_viewer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.btn_load_image = QPushButton(Dialog)
        self.btn_load_image.setObjectName(u"btn_load_image")

        self.verticalLayout_3.addWidget(self.btn_load_image)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_name = QLabel(self.frame)
        self.lb_name.setObjectName(u"lb_name")

        self.horizontalLayout.addWidget(self.lb_name)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.le_name = QLineEdit(self.frame)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.le_name)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_paste = QPushButton(self.frame)
        self.btn_paste.setObjectName(u"btn_paste")
        self.btn_paste.setMinimumSize(QSize(50, 0))
        self.btn_paste.setMaximumSize(QSize(50, 16777215))
        self.btn_paste.setIconSize(QSize(22, 22))
        self.btn_paste.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_paste)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.le_url = QLineEdit(self.frame)
        self.le_url.setObjectName(u"le_url")
        self.le_url.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.le_url.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.le_url)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_info = QLabel(self.frame)
        self.lb_info.setObjectName(u"lb_info")

        self.horizontalLayout_4.addWidget(self.lb_info)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMaximumSize(QSize(200, 16777215))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.horizontalLayout_4.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addWidget(self.frame)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lb_viewer.setText("")
#if QT_CONFIG(tooltip)
        self.btn_load_image.setToolTip(QCoreApplication.translate("Dialog", u"elIge o arrastra una imagen", None))
#endif // QT_CONFIG(tooltip)
        self.btn_load_image.setText(QCoreApplication.translate("Dialog", u"LOAD IMAGE", None))
        self.lb_name.setText(QCoreApplication.translate("Dialog", u"NAME", None))
        self.le_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"Optional", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"URL", None))
#if QT_CONFIG(tooltip)
        self.btn_paste.setToolTip(QCoreApplication.translate("Dialog", u"pegar del portapapeles", None))
#endif // QT_CONFIG(tooltip)
        self.btn_paste.setText("")
        self.lb_info.setText(QCoreApplication.translate("Dialog", u"SELECT OR DROP IMAGE", None))
    # retranslateUi

