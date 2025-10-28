from pathlib import Path
from PySide6.QtWidgets import (
    QWidget, QTableWidget, QTableView, QTableWidgetItem, QHeaderView, QAbstractItemView,
    QDialog, QFileDialog, QVBoxLayout, QLabel
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt
from ui.widget_playlist.skin_playlist import Ui_Playlist
from ui.widget_modal import WidgetModal, Viewer
from core_myra.file_m3u import FileM3u


class WidgetPlaylist(QWidget, Ui_Playlist):
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
       self.btn_open.clicked.connect(self._test_open_playlist)
       self.btn_edit.clicked.connect(self.save)

    def open_dialog_new_url(self):
        dialog = WidgetModal(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            print("agregada nueva url")
            name, url, image = dialog.get_data()
            if url:
                self.add_item(name, url, image)

    def add_item(self, title:str, url:str, image:str, **kw):
        index_row = self.tw_playlist.rowCount()
        self.tw_playlist.insertRow(index_row)
        item_name = QTableWidgetItem(title)
        item_url = QTableWidgetItem(url)
        self.tw_playlist.setItem(index_row, 1, item_name)
        self.tw_playlist.setItem(index_row, 2, item_url)
        value = self.sld_size_icons.value()

        viewer = Viewer()
        viewer.set_image(image)
        viewer.resize_image(size=value)
        self.tw_playlist.setRowHeight(index_row, value)
        self.tw_playlist.setCellWidget(index_row, 0, viewer)
        data = dict(title=title, url=url, image=image)
        item_name.setData(Qt.ItemDataRole.UserRole, data)

    def _set_row_height(self):
        value = self.sld_size_icons.value()
        for index in range(self.tw_playlist.rowCount()):
            self.tw_playlist.setRowHeight(index, value)

            viewer:Viewer = self.tw_playlist.cellWidget(index, 0)
            viewer.resize_image(size=value)

    def save(self):
        def get_data_row(row:int) -> list:
            """retorna dict:{Viewer, title, url, seconds}"""
            viewer:Viewer = self.tw_playlist.cellWidget(row, 0)
            title = self.tw_playlist.item(row, 1).text()
            url = self.tw_playlist.item(row, 2).text()
            return dict(image=viewer.get_image(), title=title, url=url, seconds=0)
        
        def get_data(rows:int) -> list[dict]:
            """retorna list:[{Viewer, title, url, seconds}, {...}]"""
            return [get_data_row(r) for r in range(rows)]

        rows = self.tw_playlist.rowCount()
        if rows > 0:
            data = get_data(rows)
            m3u = FileM3u('playlist_myra.m3u')
            m3u.write(data)

    def open_m3u(self, filename_m3u:str):
        m3u = FileM3u(file_name=filename_m3u)
        items:list[dict] = m3u.read()
        self.tw_playlist.clearContents()
        for d in items:
            self.add_item(**d)

    def _test_open_playlist(self):
        self.open_m3u(filename_m3u='playlist_myra.m3u')