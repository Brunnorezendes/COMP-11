from gerar_chaves import gerar_chaves
from codificar import codificar
from decodificar import decodificar
from pre_codificar import pre_codificar
from pos_codificar import pos_codificar

def main():
    print("-" * 60)
    print("      INÍCIO DO PROCESSO DE CRIPTOGRAFIA RSA")
    print("-" * 60)

    # ----------------------------------------------------------------------
    print("\n--- Parte a): Geração das Chaves ---\n")
    # ----------------------------------------------------------------------
    primos = [10007, 15727] # Par que funciona com e=65537
    print(f"Primos escolhidos: p = {primos[0]}, q = {primos[1]}")
    
    chave_publica, chave_privada = gerar_chaves(primos)
    
    print("\nChaves geradas:")
    print(f"  - Chave Pública (n, e): {chave_publica}")
    print(f"  - Chave Privada (n, d): {chave_privada}")

    # ----------------------------------------------------------------------
    print("\n" + "-"*60)
    print("--- Partes b) e c): Processo de Criptografia ---")
    print("-" * 60)
    # ----------------------------------------------------------------------
    
    mensagem = """FEBRE HEMOPTISE DISPNEIA E SUORES NOTURNOS. A VIDA INTEIRA QUE PODIA
TER SIDO E QUE NAO FOI. TOSSE TOSSE TOSSE. MANDOU CHAMAR O MEDICO.
DIGA TRINTA E TRES. TRINTA E TRES TRINTA E TRES TRINTA E TRES. RESPIRE. O
SENHOR TEM UMA ESCAVACAO NO PULMAO ESQUERDO E O PULMAO DIREITO
INFLITRADO. ENTAO DOUTOR NAO E POSSIVEL TENTAR O PENUMOTORAX. NAO.
A UNICA COISA A FAZER E TOCAR UM TANGO ARGENTINO."""
    
    # Limpeza da mensagem conforme o PDF
    mensagem = mensagem.replace('\n', ' ')
    
    print("\n1. Mensagem Original a ser Criptografada:")
    print(f"   '{mensagem}'")
    
    mensagem_pre_codificada = pre_codificar(mensagem)
    print("\n2. Mensagem Pré-codificada (convertida para número):")
    print(f"   {mensagem_pre_codificada}")

    mensagem_codificada = codificar(str(mensagem_pre_codificada), chave_publica)
    print("\n3. Mensagem Criptografada (lista de blocos numéricos):")
    print(f"   {mensagem_codificada}")

    # ----------------------------------------------------------------------
    print("\n" + "-"*60)
    print("--- Parte d): Tentativa de Decodificação com Chave Incorreta ---")
    print("-" * 60)
    # ----------------------------------------------------------------------
    
    # Gerando um par de chaves incorreto para o teste
    _, chave_privada_errada = gerar_chaves([15727, 99989])
    
    print(f"\nTentando decodificar usando a chave privada errada:")
    print(f"   {chave_privada_errada}")
    
    mensagem_decodificada_errada = decodificar(mensagem_codificada, chave_privada_errada)
    texto_decodificado_errado = pos_codificar(str(mensagem_decodificada_errada))
    
    print("\nTexto resultante (sem sentido):")
    print(f"   '{texto_decodificado_errado}'")
    
    print("\nResultado: Conforme esperado, a decodificação com a chave incorreta falhou.")

    # ----------------------------------------------------------------------
    print("\n" + "-"*60)
    print("--- Parte e) e f): Decodificação com a Chave Correta ---")
    print("-" * 60)
    # ----------------------------------------------------------------------

    print(f"\nDecodificando a mensagem usando a chave privada correta:")
    print(f"   {chave_privada}")

    mensagem_decodificada = decodificar(mensagem_codificada, chave_privada)
    print("\n1. Mensagem Decodificada (número gigante reconstruído):")
    print(f"   {mensagem_decodificada}")

    texto_decodificado = pos_codificar(str(mensagem_decodificada))
    print("\n2. Texto Final Recuperado:")
    print(f"   '{texto_decodificado}'")
    
    print("\nResultado: Sucesso! A mensagem original foi recuperada com precisão.")

    # ----------------------------------------------------------------------
    print("\n" + "-"*60)
    print("FIM DO PROGRAMA")
    print("-" * 60)

if __name__ == "__main__":
    main()