class Carro:
    def __init__(self, tipo, cor, placa, numeroDePortas):
        self.tipo = tipo
        self.cor = cor
        self.placa = placa
        self.numeroDePortas = numeroDePortas

    def exibir_placa(self):
        print(self.placa)

def main():
    carro1 = Carro("Porsche", "Branco", "ABC1234", 4)
    carro2 = Carro("Ferrari", "Ferrari", "DEF5678", 2)

    carro1.exibir_placa()
    carro2.exibir_placa()

if __name__ == "__main__":
    main()