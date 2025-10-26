from pathlib import Path
from PySide6.QtWidgets import (
    QWidget, QTableWidget, QTableView, QTableWidgetItem, QHeaderView, QAbstractItemView,
    QDialog, QFileDialog, QVBoxLayout, QLabel
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt
from ui.skin_myra_playlist import Ui_Form
from ui.dialgog_add_url import DialogAddUrl, Viewer


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
       self.sld_size_icons.sliderReleased.connect(self._set_row_height)

    def open_dialog_new_url(self):
        dialog = DialogAddUrl(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            print("agregada nueva url")
            name, url, image = dialog.get_data()
            if url:
                self.add_item(name, url, image)

    def add_item(self, name:str, url:str, image:str):
        index_row = self.tw_playlist.rowCount()
        self.tw_playlist.insertRow(index_row)
        item_name = QTableWidgetItem(name)
        item_url = QTableWidgetItem(url)
        self.tw_playlist.setItem(index_row, 1, item_name)
        self.tw_playlist.setItem(index_row, 2, item_url)
        value = self.sld_size_icons.value()

        viewer = Viewer()
        viewer.set_image(image)
        viewer.resize_image(size=value)
        self.tw_playlist.setRowHeight(index_row, value)
        self.tw_playlist.setCellWidget(index_row, 0, viewer)
        data = dict(name=name, url=url, image=image)
        item_name.setData(Qt.ItemDataRole.UserRole, data)

    def _set_row_height(self):
        value = self.sld_size_icons.value()
        for index in range(self.tw_playlist.rowCount()):
            self.tw_playlist.setRowHeight(index, value)

            viewer:Viewer = self.tw_playlist.cellWidget(index, 0)
            viewer.resize_image(size=value)

