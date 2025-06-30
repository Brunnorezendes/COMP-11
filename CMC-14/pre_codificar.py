
def pre_codificar(mensagem):
    
    codigos = {
        'A':'10',
        'B':'11',
        'C':'12',
        'D':'13',
        'E':'14',
        'F':'15',
        'G':'16',
        'H':'17',
        'I':'18',
        'J':'19',
        'K':'20',
        'L':'21',
        'M':'22',
        'N':'23',
        'O':'24',
        'P':'25',
        'Q':'26',
        'R':'27',
        'S':'28',
        'T':'29',
        'U':'30',
        'V':'31',
        'X':'32',
        'W':'33',
        'Y':'34',
        'Z':'35',
        ' ':'36',
        '.':'37',
    }

    mensagem_pre_codificada = ''
    for letra in mensagem:
        try:
            mensagem_pre_codificada += codigos[letra]
        except KeyError:
            mensagem_pre_codificada += '37'

    return int(mensagem_pre_codificada)