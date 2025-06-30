def decodificar(lista_codificada, chave):
    [n, d] = chave
    mensagem_decodificada = ""
    for bloco in lista_codificada:
        bloco_decodificado = pow(bloco, d, n)
        mensagem_decodificada += str(bloco_decodificado)
    return int(mensagem_decodificada)