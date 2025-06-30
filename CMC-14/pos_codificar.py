def pos_codificar(mensagem):

    codigos = {
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F',
        '16': 'G',
        '17': 'H',
        '18': 'I',
        '19': 'J',
        '20': 'K',
        '21': 'L',
        '22': 'M',
        '23': 'N',
        '24': 'O',
        '25': 'P',
        '26': 'Q',
        '27': 'R',
        '28': 'S',
        '29': 'T',
        '30': 'U',
        '31': 'V',
        '32': 'X',
        '33': 'W',
        '34': 'Y',
        '35': 'Z',
        '36': ' ',
        '37': '.',
    }

    mensagem_texto = str(mensagem)
    mensagem_pos_codificada = ''

    for i in range(0, len(mensagem_texto), 2):
        letra = mensagem_texto[i:i + 2]
        try:
            mensagem_pos_codificada += codigos[letra]
        except KeyError:
            mensagem_pos_codificada += '_'

    return mensagem_pos_codificada