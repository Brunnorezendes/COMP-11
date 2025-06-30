# Autores: William Teleken e Brunno Rezende
import tkinter as tk
from app import App
from logger import logger

if __name__ == "__main__":

    logger.set_enabled(True)
    logger.info("Aplicação iniciada.")

    root = tk.Tk()

    app = App(root)

    root.mainloop()

    logger.info("Aplicação encerrada.")