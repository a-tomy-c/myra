from PySide6.QtWidgets import QDialog, QWidget
from ui.skin_dialog_add_url import Ui_Dialog


class DialogAddUrl(QDialog, Ui_Dialog):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self._cnf_DialogAddUrl()

    def _cnf_DialogAddUrl(self):
        self.setWindowTitle('Agrega una nueva Url')