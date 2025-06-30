# Autores: William Teleken e Brunno Rezende
import sqlite3

from logger import logger

class Database:
    def __init__(self, db_name='livros.db'):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.create_table()
        except sqlite3.Error as e:

            logger.error(f"Erro de conexão com o banco de dados: {e}")
            raise

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                codigo INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                autor TEXT,
                genero TEXT,
                editora TEXT,
                ano INTEGER
            )
        ''')
        self.conn.commit()

    def execute_query(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor
        except sqlite3.Error as e:

            logger.error(f"Falha ao executar a query: {query} com parâmetros {params}. Erro: {e}")
            return None

    def adicionar_livro_db(self, codigo, titulo, autor, genero, editora, ano):
        query = "INSERT INTO livros (codigo, titulo, autor, genero, editora, ano) VALUES (?, ?, ?, ?, ?, ?)"
        self.execute_query(query, (codigo, titulo, autor, genero, editora, ano))

    def pegar_todos_livros_db(self):
        query = "SELECT * FROM livros ORDER BY titulo"
        cursor = self.execute_query(query)
        return cursor.fetchall() if cursor else []
    
    def excluir_livro_db(self, codigo):
        query = "DELETE FROM livros WHERE codigo = ?"
        self.execute_query(query, (codigo,))

    def atualizar_livro_db(self, codigo, titulo, autor, genero, editora, ano):
        query = "UPDATE livros SET titulo = ?, autor = ?, genero = ?, editora = ?, ano = ? WHERE codigo = ?"
        self.execute_query(query, (titulo, autor, genero, editora, ano, codigo))

    def buscar_livro_por_titulo_db(self, titulo):
        query = "SELECT * FROM livros WHERE titulo LIKE ?"
        termo_busca = f'%{titulo}%'
        cursor = self.execute_query(query, (termo_busca,))
        return cursor.fetchall() if cursor else []

    def __del__(self):
        if self.conn:
            self.conn.close()
