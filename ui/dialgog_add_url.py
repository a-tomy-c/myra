from PySide6.QtWidgets import QDialog, QWidget, QFileDialog, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize
from ui.skin_dialog_add_url import Ui_Dialog
from pathlib import Path


class Viewer(QLabel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._cnf_Viewer()

    def _cnf_Viewer(self):
        self.IMAGE = None
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def get_image(self) -> str:
        """retorna la ruta de la image"""
        return self.IMAGE

    def set_image(self, image:str):
        """asigna la ruta de la imagen"""
        self.IMAGE = Path(image).as_posix()

    def get_pixmap(self, size:int=150) -> QPixmap:
        """retorna QPixmap redimensionado"""
        if self.get_image():
            pixmap = QPixmap(self.get_image())
            if not pixmap.isNull():
                return pixmap.scaled(
                    QSize(size, size),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )

    def resize_image(self, size:int):
        """asigna un pixmap de tamaño (size) al viewer"""
        pixmap = self.get_pixmap(size)
        if pixmap:
            self.setPixmap(pixmap)


class DialogAddUrl(QDialog, Ui_Dialog):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self._cnf_DialogAddUrl()

    def _cnf_DialogAddUrl(self):
        self.setWindowTitle('Agrega una nueva Url')
        self.viewer = Viewer()
        self.btn_load_image.clicked.connect(self.select_image)

    def select_image(self):
        """dialogo para seleccionar una imagen"""
        self.image_path, _ = QFileDialog.getOpenFileName(
            self, "Seleciona una Imagen", "",
            "Imagenes (*.jpg *.png *.jpeg)"
        )
        if self.image_path:
            self.viewer.set_image(image=self.image_path)
            pix_scaled:QPixmap = self.viewer.get_pixmap()
            if not pix_scaled.isNull():
                self.lb_viewer.setPixmap(pix_scaled)
            else:
                self.lb_info.setText("ERROR al cargar la imagen")

    def get_image(self) -> str:
        """retorna la ruta de la imagen"""
        return self.viewer.get_image()
    
    def get_url(self) -> str:
        """retorna la url ingresada en la ventana modal"""
        return self.le_url.text()
    
    def get_name(self) -> str:
        """retorna el nombre ingresado en la ventana modal"""
        return self.le_name.text()
    
    def get_data(self) -> tuple[str]:
        """retorna una tupla: (nombre, url, imagen)"""
        return self.get_name(), self.get_url(), self.get_image()
    
    def get_viewer(self, size:int) -> Viewer:
        """retorna un objeto Viewer (QLabel con imagen)"""
        self.viewer.resize_image(size=size)
        return self.viewer

