"""Ponto de entrada da aplicação."""

import sys
from PyQt5.QtWidgets import QApplication
from app.core import AppCore


def main():
    """Função principal que inicia o aplicativo."""
    app = QApplication(sys.argv)
    core = AppCore()
    core.run()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
