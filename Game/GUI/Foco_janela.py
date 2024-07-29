import os
from Log.infor import Log
from pywinauto import Application


class FocoJanela:
    def __init__(self, janela_titulo):
        self.janela_titulo = janela_titulo

    def foco_janela(self):
        try:
            app = Application().connect(title=self.janela_titulo)
            window = app.window(title=self.janela_titulo)
            window.set_focus()
        except Exception as e:
            Log(5).salvar()