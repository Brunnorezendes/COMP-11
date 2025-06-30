# Autores: William Teleken e Brunno Rezende
import tkinter as tk
from tkinter import ttk
from logger import logger

class Interface:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Catálogo de Livros")
        self.root.geometry("850x600")
        self.root.configure(bg="#f0f0f0")
        self.entries = {}
        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=20, padx=20, fill="x")

        labels = ["Código:", "Título:", "Autor:", "Gênero:", "Editora:", "Ano de Pub.:"]
        for i, label_text in enumerate(labels):
            label = tk.Label(input_frame, text=label_text, font=("Arial", 11), bg="#f0f0f0")
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            entry = tk.Entry(input_frame, font=("Arial", 11), width=40)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            self.entries[label_text.split(':')[0].lower().replace('.', '')] = entry

        search_frame = tk.Frame(self.root, bg="#f0f0f0")
        search_frame.pack(pady=5, padx=20, fill="x")

        search_label = tk.Label(search_frame, text="Buscar por Título:", font=("Arial", 11), bg="#f0f0f0")
        search_label.pack(side=tk.LEFT, padx=(0, 10))

        self.search_entry = tk.Entry(search_frame, font=("Arial", 11), width=30)
        self.search_entry.pack(side=tk.LEFT, expand=True, fill="x")

        self.search_btn = tk.Button(search_frame, text="Buscar", command=lambda: self.controller.buscar_livro())
        self.search_btn.pack(side=tk.LEFT, padx=(10, 0))

        self.show_all_btn = tk.Button(search_frame, text="Mostrar Todos", command=self.controller.atualizar_lista_livros)
        self.show_all_btn.pack(side=tk.LEFT, padx=(10, 0))


        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        self.add_btn = tk.Button(button_frame, text="Adicionar", width=12,
                                 command=lambda: self.controller.adicionar_livro(self.get_entry_data()))
        self.add_btn.grid(row=0, column=0, padx=10)
        self.update_btn = tk.Button(button_frame, text="Atualizar", width=12, command=lambda: self.controller.atualizar_livro(self.get_entry_data()))
        self.update_btn.grid(row=0, column=1, padx=10)
        self.delete_btn = tk.Button(button_frame, text="Excluir", width=12, command=lambda: self.on_excluir_livro())
        self.delete_btn.grid(row=0, column=2, padx=10)
        self.clear_btn = tk.Button(button_frame, text="Limpar", width=12, command=self.limpar_campos)
        self.clear_btn.grid(row=0, column=3, padx=10)
        
        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=20, padx=20, fill="both", expand=True)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree = ttk.Treeview(list_frame, columns=("Código", "Título", "Autor", "Gênero", "Editora", "Ano"), yscrollcommand=scrollbar.set, show="headings")
        self.tree.bind("<<TreeviewSelect>>", self.selecionar_item)
        self.tree.pack(side=tk.LEFT, fill="both", expand=True)
        scrollbar.config(command=self.tree.yview)
        
        self.tree.heading("Código", text="Código")
        self.tree.column("Código", anchor=tk.CENTER, width=80)
        self.tree.heading("Título", text="Título")
        self.tree.column("Título", anchor=tk.W, width=200)
        self.tree.heading("Autor", text="Autor")
        self.tree.column("Autor", anchor=tk.W, width=150)
        self.tree.heading("Gênero", text="Gênero")
        self.tree.column("Gênero", anchor=tk.W, width=100)
        self.tree.heading("Editora", text="Editora")
        self.tree.column("Editora", anchor=tk.W, width=120)
        self.tree.heading("Ano", text="Ano")
        self.tree.column("Ano", anchor=tk.CENTER, width=80)

    def get_entry_data(self):
        try:
            data = {
                'codigo': int(self.entries['código'].get()),
                'titulo': self.entries['título'].get(),
                'autor': self.entries['autor'].get(),
                'genero': self.entries['gênero'].get(),
                'editora': self.entries['editora'].get(),
                'ano': int(self.entries['ano de pub'].get())
            }
            if not data['titulo']:
                logger.warning("Tentativa de adicionar/atualizar com título vazio.")
                return None
            return data
        except ValueError:
            logger.error("Erro de entrada de dados: Código e Ano devem ser números inteiros.")
            return None
        
    def selecionar_item(self, event):
        try:
            self.limpar_campos()

            selected_item = self.tree.selection()[0]
            item_values = self.tree.item(selected_item)['values']
            
            self.entries['código'].insert(0, item_values[0])
            self.entries['título'].insert(0, item_values[1])
            self.entries['autor'].insert(0, item_values[2])
            self.entries['gênero'].insert(0, item_values[3])
            self.entries['editora'].insert(0, item_values[4])
            self.entries['ano de pub'].insert(0, item_values[5])
            
        except IndexError:
            pass

    def limpar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def on_excluir_livro(self):
        try:
            selected_item = self.tree.selection()[0]
            codigo = self.tree.item(selected_item, 'values')[0]
            logger.info(f"Excluindo livro com código: {codigo}")
            self.controller.excluir_livro(codigo)
        
        except IndexError:
            logger.error("Nenhum livro selecionado para exclusão.")

    def get_search_term(self):
        return self.search_entry.get()

    def popular_lista(self, livros):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for livro in livros:
            self.tree.insert("", "end", values=livro)
