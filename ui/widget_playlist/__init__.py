from pathlib import Path
from PySide6.QtWidgets import (
    QWidget, QTableWidget, QTableView, QTableWidgetItem, QHeaderView, QAbstractItemView,
    QDialog, QFileDialog, QVBoxLayout, QLabel
)
from PySide6.QtGui import QPixmap, QImage, QIcon
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
       self.sld_size_icons.setRange(20, 60)

       # agregando dialogo
       self.btn_add.clicked.connect(self.open_dialog_new_url)
       self.sld_size_icons.sliderReleased.connect(self._set_row_height)
       self.btn_open.clicked.connect(self._test_open_playlist)
       self.btn_edit.clicked.connect(self.save)
       self.btn_up.clicked.connect(self.move_row_up)
       self.btn_down.clicked.connect(self.mover_row_down)

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
        viewer:QPixmap = self.get_pixmap(image)
        item_icon = QTableWidgetItem()
        item_icon.setIcon(QIcon(viewer))
        item_icon.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tw_playlist.setItem(index_row, 0, item_icon)

        self.tw_playlist.setRowHeight(index_row, value)
        # self.tw_playlist.setCellWidget(index_row, 0, viewer)
        # data = dict(title=title, url=url, image=image)
        # item_name.setData(Qt.ItemDataRole.UserRole, data)

    def get_pixmap(self, path:str) -> QPixmap:
        value = self.sld_size_icons.maximum()
        pixmap = QPixmap(path)
        if not pixmap.isNull():
            return pixmap.scaled(
                    QSize(value, value),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )

    def _set_row_height(self):
        value = self.sld_size_icons.value()
        self.tw_playlist.setIconSize(QSize(value, value))
        rows = self.tw_playlist.rowCount()
        for row in range(rows):
            self.tw_playlist.setRowHeight(row, value+4)


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
        self.tw_playlist.setRowCount(0)
        self.open_m3u(filename_m3u='playlist_myra.m3u')

    # def get_data_row(self, row:int) -> tuple[Viewer, str, str, int]:
    #     """retorna dict:{Viewer, title, url, seconds}"""
    #     viewer:Viewer = self.tw_playlist.cellWidget(row, 0)
    #     title = self.tw_playlist.item(row, 1).text()
    #     url = self.tw_playlist.item(row, 2).text()
    #     # return viewer, title, url, 0
    #     return dict(viewer=viewer, title=title, url=url, seconds=0)


    def _move_item(self, irow:int, new_irow:int):
        def take_data_row(row:int) -> dict:
            # viewer:Viewer = self.tw_playlist.cellWidget(row, 0)
            # # if viewer:
            # #     self.tw_playlist.removeCellWidget(row, 0)
            viewer = self.tw_playlist.takeItem(row, 0)
            title = self.tw_playlist.takeItem(row, 1)
            url = self.tw_playlist.takeItem(row, 2)
            return dict(viewer=viewer, title=title, url=url)
        
        def set_data_row(row:int, viewer, title, url):
            # if viewer:
            #     self.tw_playlist.setCellWidget(row, 0, viewer)
            self.tw_playlist.setItem(row, 0, viewer)
            self.tw_playlist.setItem(row, 1, title)
            self.tw_playlist.setItem(row, 2, url)

        data = take_data_row(new_irow)
        set_data_row(new_irow, **take_data_row(irow))
        # print("hasta aqui reemplazo la linea objetivo")
        set_data_row(irow, **data)
        # print("hasta aqui reemplazo la linea actual")
        self.tw_playlist.setCurrentCell(new_irow, 0)        

    def move_row_up(self):
        index_row:int = self.tw_playlist.currentRow()
        if index_row > 0 and index_row != -1:
            self._move_item(index_row, index_row-1)

    def mover_row_down(self):
        index_row:int = self.tw_playlist.currentRow()
        if index_row<self.tw_playlist.rowCount()-1 and index_row!=-1:
            self._move_item(index_row, index_row+1)

