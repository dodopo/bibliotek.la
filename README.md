# bibliotek.la

Este código Python implementa um sistema de gerenciamento de biblioteca com funcionalidades para adicionar, deletar, editar, pesquisar e exibir livros. Aqui está um resumo das principais partes do código:
1. Classe Book:
    * Representa um livro com título, autor, gênero e quantidade.
    * Métodos:
        * __str__: Retorna uma string representando o livro.
        * to_dict: Converte os atributos do livro para um dicionário.
        * from_dict: Cria um objeto Book a partir de um dicionário.
2. Classe Library:
    * Gerencia uma coleção de livros.
    * Métodos:
        * __init__: Inicializa a biblioteca e carrega os livros do arquivo books.json.
        * add_book: Adiciona um livro à coleção e salva as mudanças.
        * delete_book: Deleta um ou mais livros com base em um critério de busca (título, autor ou gênero).
        * edit_book: Edita os detalhes de um livro específico.
        * search_book: Pesquisa livros com base em um critério e valor.
        * print_books: Imprime uma lista de livros.
        * save_books: Salva a coleção de livros em um arquivo JSON.
        * load_books: Carrega a coleção de livros de um arquivo JSON.
3. Função main:
    * Exibe um menu interativo para o usuário escolher entre adicionar, deletar, editar, pesquisar, exibir livros, limpar a tela ou sair do programa.
    * Executa a ação escolhida pelo usuário, solicitando as informações necessárias e chamando os métodos apropriados da classe Library.
Este sistema permite que os usuários gerenciem uma biblioteca de forma eficiente, persistindo os dados em um arquivo JSON e proporcionando uma interface de linha de comando para interagir com a coleção de livros.
