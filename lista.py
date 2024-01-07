filmes = [
    'Os Condenados de Shawshank',
    'O Padrinho',
    'O Cavaleiro das Trevas',
    'O Padrinho: Parte II',
    'Doze Homens em Fúria',
    'A Lista de Schindler',
    'O Senhor dos Anéis - O Regresso do Rei',
    'Pulp Fiction',
    'O Senhor dos Anéis - A Irmandade do Anel',
    'O Bom, o Mau e o Vilão'
]

# Imprimindo a lista de filmes antes da movimentação
print("Lista de Filmes (Antes):", filmes)

# Trocando a posição do primeiro e segundo filme na lista
primeiro_filme = filmes.pop(0)  # Removendo o primeiro filme
print (filmes)
segundo_filme = filmes.pop(0)   # Removendo o segundo filme
print(filmes)
filmes.insert(1, primeiro_filme)  # Inserindo o primeiro filme na segunda posição
filmes.insert(0, segundo_filme)   # Inserindo o segundo filme na primeira posição


print(filmes)