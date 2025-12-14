from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from widget_frameless import WidgetFrameless
from test_player import MiVentana


class MyraPlayer(WidgetFrameless):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        # self.setupUi(self)
        self.__cnf_MyraPlayer()

    def __cnf_MyraPlayer(self):
        self.resize(430, 550)
        # self.fr_left.setHidden(True)
        # self.fr_right.setHidden(True)

        self.mv = MiVentana(self)
        self.vly_body.addWidget(self.mv)
        self.fr_status_bar.setHidden(True)
        self.set_title('MYRA PLAYER', fg='orange', bg='black')
        self.set_icon(icon=u":/w/orange.svg")
        self.setMinimumWidth(300)
        self.mv.wplaylist.btn_save.setIconSize(QSize(20,20))
        self.mv.wplaylist.btn_up.setIconSize(QSize(20,20))
        self.mv.wplaylist.btn_down.setIconSize(QSize(20,20))
        self.mv.btn_playlist.clicked.connect(self.toggle_playlist)
        self.mv.actionQuit.triggered.connect(self.close)
        self.mv.actionInfo.triggered.connect(self.show_about)
        self.mv.actiontoggle_playlist.triggered.connect(self.toggle_playlist)

        self.about.set_image(":/w/orange.svg")
        self.about.set_text_title('MYRA')
        self.about.set_text_aux('RADIO PLAYER')
        self.about.set_text('realizado por: ')
        self.about.set_text('Tomy', fg='yellowgreen', br=True)
        self.about.set_text('version: ')
        self.about.set_text('1.0', fg='salmon', br=True)
        self.about.set_text('https://github.com/a-tomy-c/myra', fg='lightblue')
        
        # self.about.test()
        # self.mv.fm_top.setStyleSheet('background:green;')
        self.mv.fm_top.setMinimumHeight(84)
        self.mv.fm_top.setMaximumHeight(84)
        

    def toggle_playlist(self):
        self.set_text_info_aux('toggle playlist', fg='azure')
        self.mv.SHOW_PLAYLIST = not self.mv.SHOW_PLAYLIST
        if self.mv.SHOW_PLAYLIST:
            self.mv.widget.show()
            self.resize(430, 550)
        else:
            self.mv.widget.hide()
            self.resize(430, 142)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    wg = MyraPlayer()
    wg.show()
    sys.exit(app.exec())


