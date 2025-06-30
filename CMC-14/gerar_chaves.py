def gerar_chaves(primos):
    
    p = primos[0]
    q = primos[1]
    
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    e = 65537

    d = pow(e, -1, phi_n)
    
    chave_publica = (n, e)
    chave_privada = (n, d)

    return [chave_publica, chave_privada]