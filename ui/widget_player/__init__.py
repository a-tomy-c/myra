from PySide6.QtWidgets import (
    QMainWindow, QWidget, QTableWidgetItem, QHeaderView, QTableWidget,
    QDialog, QFileDialog, QMessageBox, QLabel
)
from PySide6.QtGui import QPixmap, QImage, QIcon, QFont
from PySide6.QtCore import QSize, Qt
from ui.widget_player.skin_pp import Ui_MyraPlayer
from core_myra import CoreMyra, get_rounded_cover
from pathlib import Path


class WidgetPlayer(QMainWindow, Ui_MyraPlayer):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self._cnf_WidgetPlayer()

    def _cnf_WidgetPlayer(self):
        self.core = CoreMyra()
        self.SHOW_PLAYLIST = True
        self.lb_info = QLabel(parent=self, text="")
        self.lb_info.setMinimumWidth(150)
        self.lb_info.setMaximumHeight(24)
        # self.lb_info.setBaseSize(QSize(150,20))
        self.lb_info.setWordWrap(True)
        # self.lb_info.setMaximumWidth(80)
        self.lb_info.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont()
        font.setPointSize(8)
        self.lb_info.setFont(font)
        self.horizontalLayout_2.setContentsMargins(0,0,0,6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout.setSpacing(6) # espacio entre labels y imagen
        self.horizontalLayout_3.setContentsMargins(4,4,4,0)

    def set_cover(self, image:str, size:int=80):
        """asigna cover al player"""
        if not Path(image).exists():
            image = 'core_myra/default.jpg'
        if Path(image).exists():
            pix = QPixmap(QImage(image).scaledToWidth(size))
            self.lb_cover.setPixmap(get_rounded_cover(pix, 24))

    def set_url(self, url:str):
        """asigna una url"""
        if self.core.IS_PLAYING:
            self.stop()
        self.core.set_url(url)
        self.play()

    def play(self):
        req = self.core.play()
        self.lb_info.setText(req)
        self.btn_play.setIcon(QIcon(":/w/stop.svg"))

    def stop(self):
        req = self.core.stop()
        self.lb_info.setText(req)
        self.btn_play.setIcon(QIcon(":/w/play.svg"))

    def resizeEvent(self, event):
        width = self.geometry().width()
        wlb = self.lb_info.geometry().width()
        self.lb_info.move(width-(wlb+4), 0)

    def set_volume(self, volume:int):
        """asigna volumen 1-100"""
        self.core.set_volume(value=volume)
        self.sld_volume.setToolTip(str(volume))

    def set_volme_initial(self, volume:int):
        """asigna el volumen (valor de inicio)"""
        self.set_volume(volume)
        self.sld_volume.setValue(volume)

    def closeEvent(self, event):
        self.core.terminate()
        self.lb_info.setText('Bye!')

    def set_metadata(self):
        """asigna info al ui sobre el metadata"""
        metadata:dict = self.core.get_metadata()
        # self.lb_title.setText(metadata.get('mtitle', ''))
        self.lb_name.setText(metadata.get('iname', ''))
        codec = metadata.get('codec', '')
        self.lb_info.setText(f'<p style="line-height:80%;">{codec}</p>')
        title = metadata.get('mtitle', '')
        self.lb_title.setText(f'<p style="line-height:80%;">{title}</p>')
        self.lb_title.setToolTip(title)
