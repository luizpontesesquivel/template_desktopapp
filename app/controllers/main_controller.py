"""Controlador principal da aplicação."""


class MainController:
    """Classe responsável pela lógica da janela principal."""

    def __init__(self):
        """Inicializa o controlador."""
        self.message = "Olá, mundo do controller!"

    def get_message(self):
        """Retorna a mensagem do controlador."""
        return self.message
