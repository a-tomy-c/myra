from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from ui.widget_playlist import WidgetPlaylist


class Ventana(QMainWindow):
    def __init__(self, *args, **kw):
        super().__init__()
        self._cnf_ventana()

    def _cnf_ventana(self):
        self.resize(320, 400)
        wplaylist = WidgetPlaylist()
        self.setCentralWidget(wplaylist)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    vn = Ventana()
    vn.show()
    sys.exit(app.exec())