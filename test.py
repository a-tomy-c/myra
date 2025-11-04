from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from ui.widget_playlist import WidgetPlaylist
from ui.widget_player import WidgetPlayer


class Ventana(QMainWindow):
    def __init__(self, *args, **kw):
        super().__init__()
        self._cnf_ventana()

    def _cnf_ventana(self):
        self.resize(320, 400)
        # self.setStyleSheet('background-color:#322630;')
        # PRUEBA PLAYLIST
        wplaylist = WidgetPlaylist()
        self.setCentralWidget(wplaylist)

        # PRUEBA PLAYER
        wplayer = WidgetPlayer()
        self.setCentralWidget(wplayer)
        ### tengo que heredar la clase, no agergarla como widget



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    vn = Ventana()
    vn.show()
    sys.exit(app.exec())