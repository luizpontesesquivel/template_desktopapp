"""Inicializador principal da aplicação."""

from app.views.main_window import MainWindow


class AppCore:
    """Classe central da aplicação."""

    def __init__(self):
        """Inicializa os componentes principais."""
        self.main_window = MainWindow()

    def run(self):
        """Executa a janela principal."""
        self.main_window.show()
