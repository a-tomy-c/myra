from PySide6.QtWidgets import (
    QWidget, QTableWidgetItem, QHeaderView, QTableWidget,
    QDialog, QFileDialog, QMessageBox
)
from PySide6.QtGui import QPixmap, QImage, QIcon
from PySide6.QtCore import QSize, Qt
from ui.widget_playlist.skin_playlist import Ui_Playlist
from ui.widget_modal import WidgetModal
from core_myra.file_m3u import FileM3u


class MyItem(QTableWidgetItem):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._cnf_MyItem()

    def _cnf_MyItem(self):
        self.file = None

    def get_pixmap(self, height:int) -> QPixmap:
        pixmap = QPixmap(self.get_image())
        if not pixmap.isNull():
            return pixmap.scaled(
                    QSize(height, height),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )

    def set_image(self, file:str, h:int=30):
        self.file = file
        pixmap = self.get_pixmap(height=h)
        if pixmap:
            self.setIcon(QIcon(pixmap))

    def get_image(self) -> str:
        return self.file


class WidgetPlaylist(QWidget, Ui_Playlist):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self._cnf_WidgetPlaylist()

    def _cnf_WidgetPlaylist(self):
        hh:QHeaderView = self.tw_playlist.horizontalHeader()
        hh.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.set_save_dir()
        self.sld_size_icons.setRange(20, 60)
        self.element = Element(self)
        self.element.set_height_init(40)

        self.btn_add.clicked.connect(self.dialog_add_url)
        self.btn_open.clicked.connect(self.playlist_open)
        self.btn_save.clicked.connect(self.playlist_save)
        self.btn_up.clicked.connect(self.element.move_up)
        self.btn_down.clicked.connect(self.element.move_down)
        self.tw_playlist.cellDoubleClicked.connect(self.element._test_select)
        self.sld_size_icons.sliderReleased.connect(self.element._set_height)
        # self.btn_save.clicked.connect(self.element.delete)
        # self.btn_down.clicked.connect(self.element.clear)

    def set_save_dir(self, path:str='.'):
        """asigna la ruta donde se guardan las playlist por defecto"""
        self.SAVE_DIR = path

    def dialog_add_url(self):
        """agrega una nueva url"""
        dialog = WidgetModal(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            title, url, image = dialog.get_data()
            if url:
                self.element.append(url, title, image)

    def playlist_save(self):
        """guarda la playlist como un archivo .m3u"""
        def get_data(index:int) -> dict:
            """retorna un dict:{url, title, image, seconds=0}"""
            return dict(**self.element.select(index), seconds=0)
        
        count = self.tw_playlist.rowCount()
        if count > 0:
            data = [get_data(i) for i in range(count)]
            path = f'{self.SAVE_DIR}/untitled.m3u'
            filename, _ = QFileDialog.getSaveFileName(
                self, 'Guardar archivo playlist .m3u', path,
                'playlist (*.m3u);;Todos (*.*)'
            )
            if filename:
                m3u = FileM3u(filename)
                m3u.write(data)

    def open_m3u(self, filename_m3u:str):
        """abre y carga un archivo .m3u"""
        m3u = FileM3u(file_name=filename_m3u)
        items:list[dict] = m3u.read()
        if len(items) > 0:
            for d in items:
                self.element.append(**d)
            self.tw_playlist.setCurrentCell(0, 1)

    def playlist_append(self):
        """selecciona un archivo .m3u y agrega"""
        filename, _ = QFileDialog.getOpenFileName(
            self, 'selecciona un archivo', self.SAVE_DIR,
            'playlist file (*.m3u);;todos los archivos (*.*)'
        )
        if filename:
            self.open_m3u(filename)

    def playlist_open(self):
        """selecciona un archivo .m3u y carga"""
        self.tw_playlist.setRowCount(0)
        self.playlist_append()


class Element():
    """un elemento es toda la fila"""
    def __init__(self, widget:WidgetPlaylist, *args, **kw):
        super().__init__(*args, **kw)
        self._cnf_Element(widget)

    def _cnf_Element(self, widget:WidgetPlaylist):
        self.wg = widget
        self.playlist:QTableWidget = self.wg.tw_playlist

    def append(self, url:str, title:str, image:str, **kw):
        """agrega un elemento a la playlist"""
        index = self.playlist.rowCount()
        self.playlist.insertRow(index)

        item_title = MyItem(title)
        item_url = QTableWidgetItem(url)
        self.playlist.setItem(index, 0, item_title)
        self.playlist.setItem(index, 1, item_url)
        value = self.wg.sld_size_icons.value()
        self.playlist.setRowHeight(index, value)
        item_title.set_image(file=image, h=self.wg.sld_size_icons.maximum())
        data = dict(title=title, url=url, image=image)
        item_url.setData(Qt.ItemDataRole.UserRole, data)

    def set_height(self, value:int):
        """asigna la altura de los elementos"""
        self.playlist.setIconSize(QSize(value, value))
        for index in range(self.playlist.rowCount()):
            self.playlist.setRowHeight(index, value)

    def set_height_init(self, value:int):
        """asigna una altura inicial de la fila"""
        self.wg.sld_size_icons.setValue(value)
        self.set_height(value)

    def _move(self, index:int, new_index:int):
        """mueve un fila desde index a new_index"""
        def take_items(index:int):
            return dict(title=self.playlist.takeItem(index, 0), \
                        url=self.playlist.takeItem(index, 1))
        
        def set_items(index:int, title, url):
            self.playlist.setItem(index, 0, title)
            self.playlist.setItem(index, 1, url)

        items = take_items(new_index)
        set_items(new_index, **take_items(index))
        set_items(index, **items)
        self.playlist.setCurrentCell(new_index, 1)

    def move_up(self):
        """mueve un elemento hacia arriba"""
        current_index = self.playlist.currentRow()
        if current_index>0 and current_index!=-1:
            self._move(current_index, current_index-1)

    def move_down(self):
        """mueve un elemento hacia abajo"""
        current_index = self.playlist.currentRow()
        if current_index<self.playlist.rowCount()-1 and current_index!=-1:
            self._move(current_index, current_index+1)

    def delete(self):
        """borra un elemento"""
        if self.playlist.rowCount() > 0:
            self.playlist.removeRow(self.playlist.currentRow())

    def clear(self):
        """borra todos los elementos"""
        if self.playlist.rowCount() > 0:
            request = QMessageBox.question(
                self.wg, "Playlist clear",
                "Se eliminaran todos los items de la playlist\n¿Deseas continuar?",
                QMessageBox.Yes | QMessageBox.No
            )
            if request == QMessageBox.Yes:
                self.playlist.setRowCount(0)

    def select(self, index:int, col:int=None) -> dict[str]:
        """retorna un diccionario con url, title, image"""
        return self.playlist.item(index, 1).data(Qt.ItemDataRole.UserRole)
    
    def _set_height(self):
        self.set_height(value=self.wg.sld_size_icons.value())
    
    def _test_select(self, index:int, col:int=None):
        print(self.select(index, col))