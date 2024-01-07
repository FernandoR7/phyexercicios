filmes = [
    {'nome': 'Os Condenados de Shawshank', 'ano': 1994, 'sinopse': 'Um homem é condenado à prisão por um crime que não cometeu e busca a redenção ao longo dos anos.'},
    {'nome': 'O Padrinho', 'ano': 1972, 'sinopse': 'A história da família Corleone, liderada pelo patriarca Vito Corleone, em meio ao mundo do crime organizado.'},
    {'nome': 'O Cavaleiro das Trevas', 'ano': 2008, 'sinopse': 'Batman enfrenta o Coringa, um criminoso psicótico que busca mergulhar Gotham City no caos.'},
    {'nome': 'O Padrinho: Parte II', 'ano': 1974, 'sinopse': 'A continuação da saga da família Corleone, explorando também o passado de Vito Corleone.'},
    {'nome': 'Doze Homens em Fúria', 'ano': 1957, 'sinopse': 'Doze jurados tentam chegar a um veredicto unânime no julgamento de um jovem acusado de assassinato.'},
    {'nome': 'A Lista de Schindler', 'ano': 1993, 'sinopse': 'A história verídica de Oskar Schindler, um empresário que salva a vida de mais de mil judeus durante o Holocausto.'},
    {'nome': 'O Senhor dos Anéis - O Regresso do Rei', 'ano': 2003, 'sinopse': 'A conclusão da trilogia, onde a Sociedade do Anel luta para destruir o Um Anel e derrotar Sauron.'},
    {'nome': 'Pulp Fiction', 'ano': 1994, 'sinopse': 'Histórias interligadas de gangsters, boxeadores, e outros personagens em Los Angeles.'},
    {'nome': 'O Senhor dos Anéis - A Irmandade do Anel', 'ano': 2001, 'sinopse': 'A formação da Sociedade do Anel e a jornada para destruir o Um Anel.'},
    {'nome': 'O Bom, o Mau e o Vilão', 'ano': 1966, 'sinopse': 'Três pistoleiros rivais buscam um tesouro enterrado durante a Guerra Civil Americana.'}
]

# Simulando a duplicação dos três últimos filmes
filmes += [
    {'nome': 'O Senhor dos Anéis - O Regresso do Rei', 'ano': 2003, 'sinopse': 'A conclusão da trilogia, onde a Sociedade do Anel luta para destruir o Um Anel e derrotar Sauron.'},
    {'nome': 'Pulp Fiction', 'ano': 1994, 'sinopse': 'Histórias interligadas de gangsters, boxeadores, e outros personagens em Los Angeles.'},
    {'nome': 'O Senhor dos Anéis - A Irmandade do Anel', 'ano': 2001, 'sinopse': 'A formação da Sociedade do Anel e a jornada para destruir o Um Anel.'}
]

# Removendo duplicatas usando conjunto
filmes_sem_duplicatas = list({frozenset(filme.items()) for filme in filmes})

# Imprimindo a lista de filmes após a duplicação e remoção de duplicatas
for filme in filmes_sem_duplicatas:
    print(filme)