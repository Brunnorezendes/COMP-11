while input("Deseja encerrar? ")!="sim":
    [temperatura, velocidadeVento] = input("Digite a temperatura e a velocidade do vento: ").split()
    temperatura = float(temperatura)
    velocidadeVento = float(velocidadeVento)
    if temperatura>10 or velocidadeVento<=4.8:
        print("A sensação térmica não é válida para esses valores de temperatura e velocidade do vento")
    else:
        sensacaoTermica = round(13.12 + 0.6215*temperatura - 11.37*velocidadeVento**0.16 + 0.3965*temperatura*velocidadeVento**0.16)
        print(f"A sensação térmica é de {sensacaoTermica}")