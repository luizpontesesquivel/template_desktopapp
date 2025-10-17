# 🖥️ Template de Aplicativo Desktop em Python (PyQt5)

Este projeto é um **template reutilizável e escalável** para criação de aplicativos desktop em Python utilizando **PyQt5**. Foi projetado para servir como ponto de partida para aplicações de qualquer porte, com uma estrutura modular e de fácil manutenção.

---

## 📁 Estrutura do Projeto

```

my_desktop_app_template/
├── main.py                  # Ponto de entrada do aplicativo
├── app/
│   ├── **init**.py
│   ├── core.py              # Inicialização principal da aplicação
│   ├── ui_main.py           # (Opcional) Interface gerada por Qt Designer
│   ├── controllers/
│   │   └── main_controller.py
│   └── views/
│       └── main_window.py   # Janela principal (QMainWindow)
├── resources/               # Ícones, imagens, arquivos .qrc
├── config/
│   └── settings.json        # Configurações externas
└── README.md

````

---

## 🚀 Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/my_desktop_app_template.git
cd my_desktop_app_template
````

2. **Crie e ative um ambiente virtual:**

```bash
python -m venv venv
# Ative:
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

> Se não houver `requirements.txt`, instale manualmente:

```bash
pip install PyQt5
```

4. **Execute o app:**

```bash
python main.py
```

---

## 🧱 Tecnologias Utilizadas

* [Python 3.8+](https://www.python.org/)
* [PyQt5](https://pypi.org/project/PyQt5/)
* Estrutura modular com `controllers`, `views`, `config` e `resources`

---

## ⚙️ Customização

Você pode expandir este template facilmente adicionando:

* **Novas telas/views** dentro da pasta `views/`
* **Lógica de negócio** em `controllers/`
* **Configurações dinâmicas** via JSON/YAML
* **Recursos gráficos** na pasta `resources/`
* **Integração com banco de dados ou APIs**

---

## 🧪 Testes

Você pode adicionar testes unitários com `pytest`:

```bash
pip install pytest
pytest
```

---

## 📌 Roadmap Futuro (sugestões)

* [ ] Suporte a múltiplas janelas (multi-view)
* [ ] Logging global (arquivo de log)
* [ ] Integração com SQLite
* [ ] Suporte a plugins ou módulos dinâmicos
* [ ] Suporte a `.ui` files (Qt Designer)
* [ ] Internacionalização (i18n)

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 🙋‍♂️ Autor

Desenvolvido por Luiz Eduardo Pontes Esquivel — sinta-se livre para usar, modificar e contribuir!

---
