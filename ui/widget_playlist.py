from PySide6.QtWidgets import (
    QWidget, QTableWidget, QTableView, QTableWidgetItem, QHeaderView, QAbstractItemView,
    QDialog, QFileDialog
)
from ui.skin_myra_playlist import Ui_Form
from ui.dialgog_add_url import DialogAddUrl


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


       # agregando dialogo
       self.btn_add.clicked.connect(self.open_dialog_new_url)


    def open_dialog_new_url(self):
        dialog = DialogAddUrl(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            print("agregada nueva url")

