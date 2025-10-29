from pathlib import Path
from PySide6.QtWidgets import (
    QWidget, QTableWidget, QTableView, QTableWidgetItem, QHeaderView, QAbstractItemView,
    QDialog, QFileDialog, QVBoxLayout, QLabel, QMessageBox
)
from PySide6.QtGui import QPixmap, QImage, QIcon
from PySide6.QtCore import QSize, Qt
from ui.widget_playlist.skin_playlist import Ui_Playlist
from ui.widget_modal import WidgetModal, Viewer
from core_myra.file_m3u import FileM3u


class ItemWithIcon(QTableWidgetItem):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._cnf_itemwithicon()

    def _cnf_itemwithicon(self):
        self.IMAGE = None

    def set_image(self, file:str, h:int=30):
        self.IMAGE = file
        pixmap = self.get_pixmap(height=h)
        if pixmap:
            self.setIcon(QIcon(pixmap))
            self.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def get_image(self) -> str:
        return self.IMAGE

    def get_pixmap(self, height:int) -> QPixmap:
        pixmap = QPixmap(self.get_image())
        if not pixmap.isNull():
            return pixmap.scaled(
                    QSize(height, height),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )


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
    #    self.btn_open.clicked.connect(self._test_open_playlist)
    #    self.btn_edit.clicked.connect(self.save)
    #    self.btn_edit.clicked.connect(self.remove_items)
    #    self.btn_edit.clicked.connect(self.open_load_m3u)
       self.btn_up.clicked.connect(self.move_row_up)
       self.btn_down.clicked.connect(self.move_row_down)
       self.tw_playlist.cellDoubleClicked.connect(self.select_row)
       self.btn_edit.clicked.connect(self.save)
       self.btn_open.clicked.connect(self.open_load_m3u)
       self.init_row_height(40)
       self.FOLDER_PLAYLIST = '.'
       self.set_folder_playlists(path='adicional')

    def open_dialog_new_url(self):
        dialog = WidgetModal(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            name, url, image = dialog.get_data()
            if url:
                self.add_item(name, url, image)

    def add_item(self, title:str, url:str, image:str, **kw):
        index_row = self.tw_playlist.rowCount()
        self.tw_playlist.insertRow(index_row)

        item_name = QTableWidgetItem(title)
        item_name.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        item_url = QTableWidgetItem(url)
        self.tw_playlist.setItem(index_row, 1, item_name)
        self.tw_playlist.setItem(index_row, 2, item_url)
        value = self.sld_size_icons.value()
        max_value = self.sld_size_icons.maximum()
        item_icon = ItemWithIcon()
        item_icon.set_image(file=image, h=max_value)
        self.tw_playlist.setItem(index_row, 0, item_icon)

        self.tw_playlist.setRowHeight(index_row, value)
        data = dict(title=title, url=url, image=image)
        item_url.setData(Qt.ItemDataRole.UserRole, data)

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
        self.set_row_height(self.sld_size_icons.value())

    def set_row_height(self, value:int, mod:int=4):
        self.tw_playlist.setIconSize(QSize(value, value))
        rows = self.tw_playlist.rowCount()
        for row in range(rows):
            self.tw_playlist.setRowHeight(row, value+mod)

    def init_row_height(self, value:int):
        self.sld_size_icons.setValue(value)
        self.set_row_height(value)

    def save(self):
        def get_data_row(row:int) -> list:
            """retorna dict:{Viewer, title, url, seconds}"""
            viewer = self.tw_playlist.item(row, 0)
            title = self.tw_playlist.item(row, 1).text()
            url = self.tw_playlist.item(row, 2).text()
            return dict(image=viewer.get_image(), title=title, url=url, seconds=0)
        
        def get_data(rows:int) -> list[dict]:
            """retorna list:[{Viewer, title, url, seconds}, {...}]"""
            return [get_data_row(r) for r in range(rows)]

        rows = self.tw_playlist.rowCount()
        if rows > 0:
            data = get_data(rows)
            path = f'{self.FOLDER_PLAYLIST}/untitled.m3u'
            filename, _ = QFileDialog.getSaveFileName(
                self, 'Guardar archivo playlist .m3u', path,
                'playlist (*.m3u);;Todos (*.*)'
            )
            if filename:
                m3u = FileM3u(filename)
                m3u.write(data)

    def open_m3u(self, filename_m3u:str):
        m3u = FileM3u(file_name=filename_m3u)
        items:list[dict] = m3u.read()
        if len(items) > 0:
            for d in items:
                self.add_item(**d)
            self.tw_playlist.setCurrentCell(0, 2)

    def _test_open_playlist(self):
        self.tw_playlist.setRowCount(0)
        self.open_m3u(filename_m3u='playlist_myra.m3u')

    # def get_data_row(self, row:int) -> tuple[str, str, int]:
    #     """retorna dict:{image, title, url}"""
    #     viewer:Viewer = self.tw_playlist.cellWidget(row, 0)
    #     img = ""
    #     title = self.tw_playlist.item(row, 1).text()
    #     url = self.tw_playlist.item(row, 2).text()
    #     return dict(image=img, title=title, url=url)

    def _move_item(self, irow:int, new_irow:int):
        def take_data_row(row:int) -> dict:
            viewer = self.tw_playlist.takeItem(row, 0)
            title = self.tw_playlist.takeItem(row, 1)
            url = self.tw_playlist.takeItem(row, 2)
            return dict(viewer=viewer, title=title, url=url)
        
        def set_data_row(row:int, viewer, title, url):
            self.tw_playlist.setItem(row, 0, viewer)
            self.tw_playlist.setItem(row, 1, title)
            self.tw_playlist.setItem(row, 2, url)

        data = take_data_row(new_irow)
        set_data_row(new_irow, **take_data_row(irow))
        set_data_row(irow, **data)
        self.tw_playlist.setCurrentCell(new_irow, 0)        

    def move_row_up(self):
        index_row:int = self.tw_playlist.currentRow()
        if index_row > 0 and index_row != -1:
            self._move_item(index_row, index_row-1)

    def move_row_down(self):
        index_row:int = self.tw_playlist.currentRow()
        if index_row<self.tw_playlist.rowCount()-1 and index_row!=-1:
            self._move_item(index_row, index_row+1)

    def remove_items(self):
        if self.tw_playlist.rowCount() > 0:
            res = QMessageBox.question(
                self, "Playlist clear",
                "Se eliminaran todos los items de la playlist\n¿Deseas continuar?",
                QMessageBox.Yes | QMessageBox.No
            )
            if res == QMessageBox.Yes:
                self.tw_playlist.setRowCount(0)

    def select_row(self, row:int, col:int):
        item = self.tw_playlist.item(row, 2)
        return item.data(Qt.ItemDataRole.UserRole)
    
    def delete_row(self):
        row = self.tw_playlist.currentRow()
        if row >= 0:
            self.tw_playlist.removeRow(row)

    def open_load_m3u(self):
        """dialog: selecciona un archivo m3u, adjunta"""
        filename, _ = QFileDialog.getOpenFileName(
            self, 'selecciona un archivo', self.FOLDER_PLAYLIST,
            'playlist file (*.m3u);;todos los archivos (*.*)'
        )
        if filename:
            self.open_m3u(filename)

    def load_m3u(self):
        """dialog: selecciona un archivo m3u, limpia y carga"""
        self.tw_playlist.setRowCount(0)
        self.open_load_m3u()

    def set_folder_playlists(self, path:str):
        self.FOLDER_PLAYLIST = path