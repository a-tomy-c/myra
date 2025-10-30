# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'skin_playlist.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSlider, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import ui.icons

class Ui_Playlist(object):
    def setupUi(self, Playlist):
        if not Playlist.objectName():
            Playlist.setObjectName(u"Playlist")
        Playlist.resize(399, 380)
        self.verticalLayout_2 = QVBoxLayout(Playlist)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tw_playlist = QTableWidget(Playlist)
        if (self.tw_playlist.columnCount() < 3):
            self.tw_playlist.setColumnCount(3)
        brush = QBrush(QColor(128, 128, 128, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        font = QFont()
        font.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(0, 0, 0, 200));
        __qtablewidgetitem.setForeground(brush);
        self.tw_playlist.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        __qtablewidgetitem1.setBackground(QColor(0, 0, 0, 200));
        __qtablewidgetitem1.setForeground(brush);
        self.tw_playlist.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        __qtablewidgetitem2.setBackground(QColor(0, 0, 0, 200));
        __qtablewidgetitem2.setForeground(brush);
        self.tw_playlist.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tw_playlist.setObjectName(u"tw_playlist")
        self.tw_playlist.setFrameShape(QFrame.Shape.NoFrame)
        self.tw_playlist.setFrameShadow(QFrame.Shadow.Plain)
        self.tw_playlist.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tw_playlist.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tw_playlist.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tw_playlist.setIconSize(QSize(20, 20))
        self.tw_playlist.setGridStyle(Qt.PenStyle.NoPen)
        self.tw_playlist.setSortingEnabled(True)
        self.tw_playlist.setCornerButtonEnabled(False)
        self.tw_playlist.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tw_playlist)

        self.fm_bot = QFrame(Playlist)
        self.fm_bot.setObjectName(u"fm_bot")
        self.fm_bot.setFrameShape(QFrame.Shape.StyledPanel)
        self.fm_bot.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fm_bot)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 4, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(self.fm_bot)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(35, 35))
        self.btn_add.setMaximumSize(QSize(40, 35))
        icon = QIcon()
        icon.addFile(u":/w/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_add.setIcon(icon)
        self.btn_add.setIconSize(QSize(30, 30))
        self.btn_add.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_add)

        self.lb_extra = QLabel(self.fm_bot)
        self.lb_extra.setObjectName(u"lb_extra")

        self.horizontalLayout.addWidget(self.lb_extra)

        self.sld_size_icons = QSlider(self.fm_bot)
        self.sld_size_icons.setObjectName(u"sld_size_icons")
        self.sld_size_icons.setMinimumSize(QSize(60, 0))
        self.sld_size_icons.setMaximumSize(QSize(60, 16777215))
        self.sld_size_icons.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.sld_size_icons)

        self.btn_open = QPushButton(self.fm_bot)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(35, 35))
        self.btn_open.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/w/open-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_open.setIcon(icon1)
        self.btn_open.setIconSize(QSize(30, 30))
        self.btn_open.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_open)

        self.btn_save = QPushButton(self.fm_bot)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(35, 35))
        self.btn_save.setMaximumSize(QSize(35, 35))
        icon2 = QIcon()
        icon2.addFile(u":/w/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save.setIcon(icon2)
        self.btn_save.setIconSize(QSize(24, 24))
        self.btn_save.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_save)

        self.btn_up = QPushButton(self.fm_bot)
        self.btn_up.setObjectName(u"btn_up")
        self.btn_up.setMinimumSize(QSize(35, 35))
        self.btn_up.setMaximumSize(QSize(35, 35))
        icon3 = QIcon()
        icon3.addFile(u":/w/up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_up.setIcon(icon3)
        self.btn_up.setIconSize(QSize(26, 26))
        self.btn_up.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_up)

        self.btn_down = QPushButton(self.fm_bot)
        self.btn_down.setObjectName(u"btn_down")
        self.btn_down.setMinimumSize(QSize(35, 35))
        self.btn_down.setMaximumSize(QSize(35, 35))
        icon4 = QIcon()
        icon4.addFile(u":/w/down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_down.setIcon(icon4)
        self.btn_down.setIconSize(QSize(26, 26))
        self.btn_down.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_down)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.fm_bot)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Playlist)

        QMetaObject.connectSlotsByName(Playlist)
    # setupUi

    def retranslateUi(self, Playlist):
        Playlist.setWindowTitle(QCoreApplication.translate("Playlist", u"Form", None))
        ___qtablewidgetitem = self.tw_playlist.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Playlist", u"ICON", None));
        ___qtablewidgetitem1 = self.tw_playlist.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Playlist", u"NAME", None));
        ___qtablewidgetitem2 = self.tw_playlist.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Playlist", u"URL", None));
        self.btn_add.setText("")
        self.lb_extra.setText("")
        self.btn_open.setText("")
        self.btn_save.setText("")
        self.btn_up.setText("")
        self.btn_down.setText("")
    # retranslateUi

