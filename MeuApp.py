import requests
import os, sys
from kivy.app import App
from kivy.lang import Builder
from kivy.resources import resource_add_path, resource_find

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):

        self.root.ids["moeda1"].text = f"Dólar: R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro: R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"BTC: R${self.pegar_cotacao('BTC')}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    MeuAplicativo().run()
