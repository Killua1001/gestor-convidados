convidados_noivo = []
convidados_noiva = []

def adicionar_convidado(nome, tipo):
    if not nome:
        return {'error': 'Nome é obrigatório'}
    
    if tipo == 'noivo':
        if len(convidados_noivo) >= 10:
            return {'error': 'O noivo já convidou 10 pessoas'}
        convidados_noivo.append(nome)
    elif tipo == 'noiva':
        if len(convidados_noiva) >= 10:
            return {'error': 'A noiva já convidou 10 pessoas'}
        convidados_noiva.append(nome)
    else:
        return {'error': 'Tipo inválido'}
    
    return {'message': f'Convidado {nome} adicionado pelo {tipo}'}

def listar_convidados(tipo=None):
    if tipo == 'noivo':
        return convidados_noivo
    elif tipo == 'noiva':
        return convidados_noiva
    return {'noivo': convidados_noivo, 'noiva': convidados_noiva}

def remover_convidado(nome, tipo):
    if tipo == 'noivo':
        if nome in convidados_noivo:
            convidados_noivo.remove(nome)
            return {'message': f'{nome} removido dos convidados do noivo'}
    elif tipo == 'noiva':
        if nome in convidados_noiva:
            convidados_noiva.remove(nome)
            return {'message': f'{nome} removido dos convidados da noiva'}
    return {'error': 'Convidado não encontrado'}

def menu():
    while True:
        print("\n--- Painel de Controle ---")
        print("1. Selecionar Noivo")
        print("2. Selecionar Noiva")
        print("3. Ver todos os convidados")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            painel('noivo')
        elif opcao == '2':
            painel('noiva')
        elif opcao == '3':
            print(listar_convidados())
        elif opcao == '4':
            break
        else:
            print("Opção inválida!")

def painel(tipo):
    while True:
        print(f"\n--- Painel do {tipo.capitalize()} ---")
        print("1. Adicionar Convidado")
        print("2. Remover Convidado")
        print("3. Listar Convidados")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do convidado: ")
            print(adicionar_convidado(nome, tipo))
        elif opcao == '2':
            nome = input("Nome do convidado para remover: ")
            print(remover_convidado(nome, tipo))
        elif opcao == '3':
            print(listar_convidados(tipo))
        elif opcao == '4':
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    menu()
