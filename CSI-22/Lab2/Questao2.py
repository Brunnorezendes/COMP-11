#Questao 2
agenda = {}
def incluirNovoNome(nome, telefones):
    global agenda
    agenda[nome] = telefones

def incluirTelefone(nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
    else:
        x = input("Nome não encontrado, deseja incluir como um novo nome?")
        if x == "sim":
            incluirNovoNome(nome, [telefone])

def excluirTelefone(nome, telefone):
    global agenda
    if nome in agenda:
        if telefone in agenda[nome]:
            agenda[nome].remove(telefone)
        else:
            print("Telefone não encontrado")
    else:
        print("Nome não encontrado")