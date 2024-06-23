import os

on_off = False
n = 0
name_file = str(input("\nNOME DO ARQUIVO: "))
valor = int(input("\nAPEBAS NÚMEROS. melhor em quantas vezes?\nx "))
while not on_off:
    # salvar texto do arquivo
    with open(name_file, "r") as conteudo:
        texto = conteudo.read()
    texto_OP = texto + texto
    # duplicar texto e modificar 2x
    with open("off.txt", "w") as TEXT:
        TEXT.write(texto_OP)
    # limpar tela e mostrar tamanho do arquivo
    os.system("clear")
    os.system("du -h off.txt")
    #contador
    n = n + 1
    if n == valor:
        on_off = True
    else: pass
