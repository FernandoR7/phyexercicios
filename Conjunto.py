filmes = {
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
}

# Imprimindo o conjunto de filmes antes da duplicação
#print("Conjunto de Filmes (Antes):", filmes)

# Duplicando os três últimos filmes
ultimos_filmes = {'O Senhor dos Anéis - O Regresso do Rei', 'Pulp Fiction', 'O Senhor dos Anéis - A Irmandade do Anel'}
filmes.update(ultimos_filmes)  # Adiciona os últimos três filmes ao conjunto

# Imprimindo o conjunto de filmes após a duplicação
print("Conjunto de Filmes (Depois):", filmes)