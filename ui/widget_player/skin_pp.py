# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'skin_pp.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)
import ui.icons

class Ui_MyraPlayer(object):
    def setupUi(self, MyraPlayer):
        if not MyraPlayer.objectName():
            MyraPlayer.setObjectName(u"MyraPlayer")
        MyraPlayer.resize(433, 423)
        self.actionQuit = QAction(MyraPlayer)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionOpen = QAction(MyraPlayer)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MyraPlayer)
        self.actionSave.setObjectName(u"actionSave")
        self.actionAppend = QAction(MyraPlayer)
        self.actionAppend.setObjectName(u"actionAppend")
        self.actionclear = QAction(MyraPlayer)
        self.actionclear.setObjectName(u"actionclear")
        self.actionInfo = QAction(MyraPlayer)
        self.actionInfo.setObjectName(u"actionInfo")
        self.actionNew_Url = QAction(MyraPlayer)
        self.actionNew_Url.setObjectName(u"actionNew_Url")
        self.actionReload_Title = QAction(MyraPlayer)
        self.actionReload_Title.setObjectName(u"actionReload_Title")
        self.actiontoggle_playlist = QAction(MyraPlayer)
        self.actiontoggle_playlist.setObjectName(u"actiontoggle_playlist")
        self.actionOpen_Config = QAction(MyraPlayer)
        self.actionOpen_Config.setObjectName(u"actionOpen_Config")
        self.actionReload_Ui = QAction(MyraPlayer)
        self.actionReload_Ui.setObjectName(u"actionReload_Ui")
        self.centralwidget = QWidget(MyraPlayer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fm_top = QFrame(self.centralwidget)
        self.fm_top.setObjectName(u"fm_top")
        self.fm_top.setMinimumSize(QSize(0, 84))
        self.fm_top.setMaximumSize(QSize(16777215, 84))
        self.fm_top.setFrameShape(QFrame.Shape.NoFrame)
        self.fm_top.setFrameShadow(QFrame.Shadow.Plain)
        self.fm_top.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.fm_top)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fm_cover = QFrame(self.fm_top)
        self.fm_cover.setObjectName(u"fm_cover")
        self.fm_cover.setMinimumSize(QSize(80, 80))
        self.fm_cover.setMaximumSize(QSize(84, 84))
        self.fm_cover.setFrameShape(QFrame.Shape.NoFrame)
        self.fm_cover.setFrameShadow(QFrame.Shadow.Plain)
        self.fm_cover.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.fm_cover)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_cover = QLabel(self.fm_cover)
        self.lb_cover.setObjectName(u"lb_cover")
        self.lb_cover.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lb_cover)


        self.horizontalLayout.addWidget(self.fm_cover)

        self.fm_control = QFrame(self.fm_top)
        self.fm_control.setObjectName(u"fm_control")
        self.fm_control.setFrameShape(QFrame.Shape.NoFrame)
        self.fm_control.setFrameShadow(QFrame.Shadow.Plain)
        self.fm_control.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.fm_control)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_name = QLabel(self.fm_control)
        self.lb_name.setObjectName(u"lb_name")
        font = QFont()
        font.setPointSize(9)
        self.lb_name.setFont(font)

        self.horizontalLayout_4.addWidget(self.lb_name)

        self.btn_playlist = QPushButton(self.fm_control)
        self.btn_playlist.setObjectName(u"btn_playlist")
        self.btn_playlist.setMaximumSize(QSize(46, 24))
        icon = QIcon()
        icon.addFile(u":/w/playlist.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_playlist.setIcon(icon)
        self.btn_playlist.setIconSize(QSize(24, 24))
        self.btn_playlist.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btn_playlist)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.lb_title = QLabel(self.fm_control)
        self.lb_title.setObjectName(u"lb_title")

        self.verticalLayout_4.addWidget(self.lb_title)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_play = QPushButton(self.fm_control)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMinimumSize(QSize(46, 24))
        self.btn_play.setMaximumSize(QSize(46, 24))
        icon1 = QIcon()
        icon1.addFile(u":/w/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_play.setIcon(icon1)
        self.btn_play.setIconSize(QSize(22, 22))
        self.btn_play.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_play)

        self.btn_previous = QPushButton(self.fm_control)
        self.btn_previous.setObjectName(u"btn_previous")
        self.btn_previous.setMaximumSize(QSize(46, 24))
        icon2 = QIcon()
        icon2.addFile(u":/w/previous.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_previous.setIcon(icon2)
        self.btn_previous.setIconSize(QSize(20, 20))
        self.btn_previous.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_previous)

        self.btn_next = QPushButton(self.fm_control)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setMaximumSize(QSize(46, 24))
        icon3 = QIcon()
        icon3.addFile(u":/w/next.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_next.setIcon(icon3)
        self.btn_next.setIconSize(QSize(20, 20))
        self.btn_next.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_next)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.sld_volume = QSlider(self.fm_control)
        self.sld_volume.setObjectName(u"sld_volume")
        self.sld_volume.setMinimumSize(QSize(80, 0))
        self.sld_volume.setMaximumSize(QSize(120, 16777215))
        self.sld_volume.setMaximum(200)
        self.sld_volume.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.sld_volume)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addWidget(self.fm_control)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.fm_top)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.vly_widget = QVBoxLayout(self.widget)
        self.vly_widget.setSpacing(0)
        self.vly_widget.setObjectName(u"vly_widget")
        self.vly_widget.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.vly_widget.addLayout(self.verticalLayout_7)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MyraPlayer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MyraPlayer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 433, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuPlaylist = QMenu(self.menubar)
        self.menuPlaylist.setObjectName(u"menuPlaylist")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MyraPlayer.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPlaylist.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionNew_Url)
        self.menuFile.addAction(self.actionQuit)
        self.menuPlaylist.addAction(self.actionOpen)
        self.menuPlaylist.addAction(self.actionSave)
        self.menuPlaylist.addAction(self.actionAppend)
        self.menuPlaylist.addSeparator()
        self.menuPlaylist.addAction(self.actionclear)
        self.menuAbout.addAction(self.actionInfo)
        self.menuTools.addAction(self.actionReload_Title)
        self.menuTools.addAction(self.actiontoggle_playlist)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionOpen_Config)
        self.menuTools.addAction(self.actionReload_Ui)

        self.retranslateUi(MyraPlayer)

        QMetaObject.connectSlotsByName(MyraPlayer)
    # setupUi

    def retranslateUi(self, MyraPlayer):
        MyraPlayer.setWindowTitle(QCoreApplication.translate("MyraPlayer", u"MYRA", None))
        self.actionQuit.setText(QCoreApplication.translate("MyraPlayer", u"Quit", None))
        self.actionOpen.setText(QCoreApplication.translate("MyraPlayer", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MyraPlayer", u"Save", None))
        self.actionAppend.setText(QCoreApplication.translate("MyraPlayer", u"Append", None))
        self.actionclear.setText(QCoreApplication.translate("MyraPlayer", u"clear", None))
        self.actionInfo.setText(QCoreApplication.translate("MyraPlayer", u"Info", None))
        self.actionNew_Url.setText(QCoreApplication.translate("MyraPlayer", u"New Url", None))
        self.actionReload_Title.setText(QCoreApplication.translate("MyraPlayer", u"Reload Title", None))
        self.actiontoggle_playlist.setText(QCoreApplication.translate("MyraPlayer", u"Toggle Playlist", None))
        self.actionOpen_Config.setText(QCoreApplication.translate("MyraPlayer", u"Open Config", None))
        self.actionReload_Ui.setText(QCoreApplication.translate("MyraPlayer", u"Reload Ui", None))
        self.lb_cover.setText("")
        self.lb_name.setText("")
        self.btn_playlist.setText("")
        self.lb_title.setText("")
        self.btn_play.setText("")
        self.btn_previous.setText("")
        self.btn_next.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MyraPlayer", u"File", None))
        self.menuPlaylist.setTitle(QCoreApplication.translate("MyraPlayer", u"Playlist", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MyraPlayer", u"About", None))
        self.menuTools.setTitle(QCoreApplication.translate("MyraPlayer", u"Tools", None))
    # retranslateUi

