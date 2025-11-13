import os
import locale
os.environ['LC_NUMERIC'] = 'C'
import core_myra.mpv as mpv
from PySide6.QtGui import QPixmap, QPainter, QPainterPath, Qt
from PySide6.QtCore import QTimer
try:
    locale.setlocale(locale.LC_NUMERIC, "C")
except locale.Error as e:
    print(f"Advertencia: No se pudo establecer el locale LC_NUMERIC a 'C': {e}")


def get_rounded_cover(pixmap:QPixmap, radius:int) -> QPixmap:
    """retorna un pixmap con bordes redondeados"""
    new_pixmap = QPixmap(pixmap.size())
    new_pixmap.fill(Qt.GlobalColor.transparent)

    painter = QPainter(new_pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
    path = QPainterPath()
    rect = new_pixmap.rect()
    path.addRoundedRect(rect, radius, radius)
    painter.setClipPath(path)
    painter.drawPixmap(0,0,pixmap)
    painter.end()
    return new_pixmap


class CoreMyra():
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._cnf_CoreMyra()

    def _cnf_CoreMyra(self):
        self.player = mpv.MPV(video=False, ytdl=False, volume_max=200)
        self.IS_PLAYING = False
        self.url = None
        self.timer = QTimer()
        self.timer.setInterval(5000)
        # self.timer.timeout.connect()

    def set_volume(self, value:int=50):
        self.player.volume = value

    def terminate(self):
        self.stop()
        self.player.terminate()
    
    def stop(self) -> str:
        self.player.stop()
        self.IS_PLAYING = False
        self.timer.stop()
        return "STOPPED"

    def play(self) -> str:
        if not self.url:
            return "error: url"
        else:
            try:
                self.player.play(self.url)
                self.IS_PLAYING = True
                self.timer.start()
                return "PLAYING"
            except Exception as err:
                return f'error: {err}'

    def set_url(self, url:str):
        self.url = url

    def toggle_playback(self):
        self.stop() if self.IS_PLAYING else self.play()

    def get_metadata(self) -> dict:
        if not self.IS_PLAYING:
            return dict()
        
        properties = dict(
            mtitle = 'media-title',
            ititle = 'metadata/icy-title',
            iname = 'metadata/icy-name',
            codec = 'audio-codec',
            sr = 'audio-params/samplerate',
        )
        metadata = dict()
        for k, prop in properties.items():
            try:
                value = self.player._get_property(prop)
                if value:
                    metadata[k] = value
            except Exception as err:
                ...
                # print(f'METADATA:: {err}')
        return metadata

