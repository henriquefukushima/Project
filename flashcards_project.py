''' Esse programa tem como intuito criar flashcards personalizados para o estudo de diversas matérias vistas na faculdade'''

def recebe_arquivo(arq):
    documento = open("arq.txt", "r")
    for linha in documento:
        