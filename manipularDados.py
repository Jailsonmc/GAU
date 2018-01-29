import pickle
from pathlib import Path

def salvar(lista, nomeFicheiro):
    pickle.dump(lista, open(nomeFicheiro, 'wb'))

def abrir(nomeFicheiro):
    ficheiro = Path(nomeFicheiro)
    if ficheiro.is_file():
        return pickle.load(open(nomeFicheiro, 'rb'))

