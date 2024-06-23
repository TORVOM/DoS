import multiprocessing
import os
from time import sleep
import requests

# dados para requisição
site = str(input("\nURL: "))
with open(str(input("\nnome do arquivo que sera enviado os dados: ")), "r") as arquivo:
    dados_txt = arquivo.read()
tempo_envio = float(input("\ntempo entre requisições: "))
input("\n[ENTER] para iniciar\n[CTRL, c] para sair")

# requisções
def request():
    global site
    global dados_txt
    global tempo_envio

    while True:
        sleep(tempo_envio)
        resposta = requests.get(site, data=dados_txt)
        print(resposta)
        if resposta == "<Response [200]>":
            print("[POST]_[ ✓ ]")

# repetis fumção request()
cod1 = multiprocessing.Process(target=request)
cod2 = multiprocessing.Process(target=request)
cod3 = multiprocessing.Process(target=request)
cod4 = multiprocessing.Process(target=request)
cod5 = multiprocessing.Process(target=request)
cod6 = multiprocessing.Process(target=request)
cod7 = multiprocessing.Process(target=request)
cod8 = multiprocessing.Process(target=request)
cod9 = multiprocessing.Process(target=request)
cod10 = multiprocessing.Process(target=request)
# executar aobmesmo tempo
cod1.start()
cod2.start()
cod3.start()
cod4.start()
cod5.start()
cod6.start()
cod7.start()
cod8.start()
cod9.start()
cod10.start()
