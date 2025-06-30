def codificar(mensagem, chave):
    mensage_texto = str(mensagem)
    [n, e] = chave
    tamanhomax_bloco = len(str(n)) - 1
    lista_codificada = []
    for i in range(0, len(mensage_texto), tamanhomax_bloco):
        bloco = mensage_texto[i:i + tamanhomax_bloco]
        if bloco[0] == '0':
            bloco = mensage_texto[i:i + tamanhomax_bloco - 1]
            i = i-1
        bloco_codificado = pow(int(bloco), e, n)
        lista_codificada.append(bloco_codificado)
    return lista_codificada