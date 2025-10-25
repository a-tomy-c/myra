from PySide6.QtWidgets import QWidget, QTableWidget, QTableView, QTableWidgetItem, QHeaderView, QAbstractItemView
from ui.skin_myra_playlist import Ui_Form


class WidgetPlaylist(QWidget, Ui_Form):
    def __init__(self, *args, **kw):
        super().__init__()
        self.setupUi(self)
        self._cnf_WidgetPlaylist()
    
    def _cnf_WidgetPlaylist(self):
       hh:QHeaderView = self.tw_playlist.horizontalHeader()
       hh.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
       hh.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
       self.sld_size_icons.setRange(24, 60)

