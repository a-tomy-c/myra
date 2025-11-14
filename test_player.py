from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFrame, QSizePolicy,
    QPushButton, QLineEdit, QLabel, QSlider, QMainWindow
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QShortcut, QKeySequence
from ui.widget_player import WidgetPlayer
from ui.widget_playlist import WidgetPlaylist


class MiVentana(WidgetPlayer):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._cnf_MiVentana()

    # def resizeEvent(self, event):
    #     gm = self.geometry()
    #     self.setWindowTitle(f'{gm.width()}x{gm.height()}')

    def _cnf_MiVentana(self):
        self.resize(430, 550)
        # vly = QVBoxLayout(self)
        # vly.addWidget()
        self.wplaylist = WidgetPlaylist()
        self.vly_widget.addWidget(self.wplaylist)
        # self.vly_widget.setContentsMargins(0, 6, 0, 0) # linea 203 wplayer
        self.wplaylist.tw_playlist.cellDoubleClicked.connect(self.select)
        self.btn_playlist.clicked.connect(self.toggle_playlist)
        pol = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        self.widget.setSizePolicy(pol)
        self.sld_volume.sliderMoved.connect(self.set_volume)
        self.btn_play.clicked.connect(self.toggle_playback)
        self.core.timer.timeout.connect(self.set_metadata)
        self.set_volme_initial(90)
        self.btn_next.clicked.connect(self.next)
        self.lb_title.setWordWrap(True)
        self.lb_name.setWordWrap(True)
        self.btn_previous.clicked.connect(self.previous)

        self._menu_actions()
        self._enable_shortcuts()
        fo = self.lb_title.font()
        fo.setPointSize(11)
        self.lb_title.setFont(fo)

        self.load_theme()
        self.wplaylist.open_m3u(filename_m3u='test_playlist.m3u')

    def select(self, row:int, col:int):
        data = self.wplaylist.element.select(row, col)
        self.set_url(data.get('url'))
        self.set_cover(data.get('image'))

    def toggle_playback(self):
        """intercambia la accion entre play y stop"""
        if self.core.IS_PLAYING:
            self.stop()
        else:
            if self.wplaylist.tw_playlist.rowCount() > 0:
                current_row = self.wplaylist.tw_playlist.currentRow()
                index_row = 0 if current_row==-1 else current_row
                self.wplaylist.tw_playlist.setCurrentCell(index_row, 1)
                # data:dict = self.wplaylist.tw_playlist.item(index_row, 1)
                data:dict = self.wplaylist.element.select(index_row, 1)
                url = data.get('url', '')
                if url:
                    self.set_url(url)
                    self.set_cover(data.get('image'))
                self.play()

    def toggle_playlist(self):
        self.SHOW_PLAYLIST = not self.SHOW_PLAYLIST
        if self.SHOW_PLAYLIST:
            self.widget.show()
            self.resize(430, 550)
        else:
            self.widget.hide()
            self.resize(430, 100)

    def next(self):
        count:int = self.wplaylist.tw_playlist.rowCount()
        current:int = self.wplaylist.tw_playlist.currentRow()
        if current < count-1:
            self.wplaylist.tw_playlist.setCurrentCell(current+1, 1)
            # data = self.wplaylist.element.select(current+1)
            self.select(current+1, 1)
            # self.btn_next.setEnabled(True)
            # self.btn_previous.setEnabled(True)
        else:
        #     self.btn_next.setEnabled(False)
        # if not self.btn_next.isEnabled():
            self.lb_info.setText('NO NEXT')

    def previous(self):
        current:int = self.wplaylist.tw_playlist.currentRow()
        if current > 0:
            self.wplaylist.tw_playlist.setCurrentCell(current-1, 1)
            self.select(current-1, 1)
        else:
            self.lb_info.setText('NO PREVIOUS')

    def _menu_actions(self):
        self.actionNew_Url.triggered.connect(self.wplaylist.dialog_add_url)
        self.actionQuit.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.wplaylist.playlist_open)
        self.actionAppend.triggered.connect(self.wplaylist.playlist_append)
        self.actionSave.triggered.connect(self.wplaylist.playlist_save)
        self.actionclear.triggered.connect(self.wplaylist.element.clear)
        self.actionReload_Title.triggered.connect(self.set_metadata)
        self.actiontoggle_playlist.triggered.connect(self.toggle_playlist)


    def _enable_shortcuts(self):
        d = {
            Qt.Key_Delete:self.wplaylist.element.delete
        }
        for k, v in d.items():
            QShortcut(QKeySequence(k), self, v, context=Qt.ApplicationShortcut)


    def load_theme(self):
        """carga los estilos del tema por default"""
        filepath = 'ui/theme.qss'
        with open(filepath, 'r', encoding='utf-8') as file:
            style = file.read()
            app = QApplication.instance()
            if app:
                app.setStyleSheet(style)

    def msg_initial(self):
        ...
    

if __name__ == '__main__':
    print("ejecucion")
    import sys
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mv = MiVentana()
    mv.show()
    sys.exit(app.exec())
