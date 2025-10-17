"""Janela principal da aplicação."""

from PyQt5.QtWidgets import QMainWindow, QLabel
from app.controllers.main_controller import MainController


class MainWindow(QMainWindow):
    """Classe da janela principal."""

    def __init__(self):
        """Inicializa a janela principal."""
        super().__init__()
        self.setWindowTitle("Template Desktop App")
        self.setGeometry(100, 100, 800, 600)
        self.controller = MainController()
        self._init_ui()

    def _init_ui(self):
        """Inicializa a interface do usuário."""
        label = QLabel(self.controller.get_message(), self)
        label.move(50, 50)
