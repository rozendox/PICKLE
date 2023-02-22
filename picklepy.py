# @Rozendox_

import pickle

# Criando um Objeto Python

lista_de_compras = ["arroz", "feijão", "macarrão", "leite"]

# Serializando o objeto em uma arquivo

with open('lista.pickle','wb') as f:
    pickle.dump(lista_de_compras, f)

# Desserializando o objeto de volta para a memoria
with open('lista.pickle', 'rb') as f:
    lista_desserializada = pickle.load(f)

# Imprimindo a lista original e desserializada

print("lista original", lista_de_compras)
print("Lista desserializada", lista_desserializada)
