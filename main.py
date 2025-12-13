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
        self.fr_left.setHidden(True)
        self.fr_right.setHidden(True)

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
        # self.setStyleSheet('QWidget#MyraPlayer {border-radius: 10px;border: 1px solid #804560;background:blue;}')


    def toggle_playlist(self):
        self.set_text_info_aux('toggle playlist', fg='azure')
        self.mv.SHOW_PLAYLIST = not self.mv.SHOW_PLAYLIST
        if self.mv.SHOW_PLAYLIST:
            self.mv.widget.show()
            self.resize(430, 550)
        else:
            self.mv.widget.hide()
            self.resize(430, 140)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    wg = MyraPlayer()
    wg.show()
    sys.exit(app.exec())


