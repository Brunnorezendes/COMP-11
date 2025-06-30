# Autores: William Teleken e Brunno Rezende
from database import Database
from interface import Interface
from logger import logger

class App:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.interface = Interface(self.root, self)
        
        self.atualizar_lista_livros()

    def adicionar_livro(self, data):
        if data:
            logger.info(f"Tentando adicionar o livro: {data['titulo']}")
            self.db.adicionar_livro_db(data['codigo'], data['titulo'], data['autor'], 
                                       data['genero'], data['editora'], data['ano'])
            logger.info(f"Livro '{data['titulo']}' adicionado com sucesso!")
            self.interface.limpar_campos()
            self.atualizar_lista_livros()

    def excluir_livro(self, codigo):
        logger.info(f"Tentando excluir o livro com código: {codigo}")
        self.db.excluir_livro_db(codigo)
        logger.info(f"Livro com código {codigo} excluído com sucesso!")
        self.atualizar_lista_livros()

    def atualizar_lista_livros(self):
        livros = self.db.pegar_todos_livros_db()
        self.interface.popular_lista(livros)

    def atualizar_livro(self, data):
        if data:
            logger.info(f"Recebido pedido para atualizar livro de código: {data['codigo']}")
            self.db.atualizar_livro_db(data['codigo'], data['titulo'], data['autor'],
                                       data['genero'], data['editora'], data['ano'])
            logger.info(f"Livro '{data['titulo']}' atualizado com sucesso.")
            self.interface.limpar_campos()
            self.atualizar_lista_livros()

    def buscar_livro(self):
        termo = self.interface.get_search_term()
        if termo is not None:
            logger.info(f"Buscando por livros com o título contendo: '{termo}'")
            livros_encontrados = self.db.buscar_livro_por_titulo_db(termo)
            self.interface.popular_lista(livros_encontrados)
