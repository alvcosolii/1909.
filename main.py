lista_tarefa = []
prioridade_definidas = ["Baixa", "Média", "Alta"]
categoria_disponiveis = ["Profissional", "Saúde", "Pessoal"]

while True:
    menu = str(input(""""
    Escolha uma opção:
    1 - Adicionar tarefa
    2 - Listar tarefas
    3 - Marcar tarefa como concluída
    4 - Exibir tarefas por prioridade
    5 - Exibir tarefas por categoria
    6 - sair               
"""))

    match menu:
        case "1":
            nome = str(input("Digite o nome da tarefa: "))
            descricao = str(input("Digite a descrição da tarefa: "))
            while True:
                prioridade = int(input("""
Digite a prioridade da tarefa:
1 - Baixa
2 - Média
3 - Alta
"""))
                if prioridade == 1 or prioridade == 2 or prioridade == 3:
                    break
                else:
                    print("Escolha uma opção correta")
            
            while True:
                categoria = int(input("""
Digite a categoria da tarefa:
1 - Profissional
2 - Saúde
3 - Pessoal
"""))
                if categoria == 1 or categoria == 2 or categoria == 3:
                    break
                else:
                    print("Escolha uma opção correta")

            
            nova_tarefa = {
                "Nome": nome,
                "Descrição": descricao,
                "Prioridade": prioridade_definidas[prioridade -1],
                "Categoria": categoria,
                "concluída": False 
            }

            lista_tarefa.append(nova_tarefa)
            print("Tarefa cadastrada com sucesso")

        case "2":
            for tarefa_da_vez in lista_tarefa:
                print(f"""
                Nome: {tarefa_da_vez["Nome"]}
                Descrição: {tarefa_da_vez["Descrição"]}
                Prioridade: {tarefa_da_vez["Prioridade"]}
                Categoria: {tarefa_da_vez["Categoria"]}
                Concluída: {tarefa_da_vez["concluída"]}
                """)

        case "3":
            tarefa_concluida = str(input("Escolha a tarefa que você quer marcar como concluída: "))
            
            for tarefa_da_vez in lista_tarefa:
                if tarefa_concluida == tarefa_da_vez["Nome"]:
                    tarefa_da_vez["concluída"] = True
                    print("Tarefa Concluída")


        case "4":
            tarefa_prioridade = str(input("Digite qual a prioridade de sua escolha: "))
            tarefa_encontradas = False

            for tarefa_da_vez in lista_tarefa:
                if tarefa_da_vez["Prioridade"].lower() == tarefa_prioridade.lower():
                    tarefa_encontradas = True
                    print(f"""
                    Nome: {tarefa_da_vez["Nome"]}
                    Descrição: {tarefa_da_vez["Descrição"]}
                    Prioridade: {tarefa_da_vez["Prioridade"]}
                    Categoria: {tarefa_da_vez["Categoria"]}
                    Concluída: {tarefa_da_vez["concluída"]}
                    """)

        case "5":
            tarefa_categoria = str(input("Digite qual a categoria de sua escolha: "))
            tarefa_encontradas = False
            
            for tarefa_da_vez in lista_tarefa:
                if tarefa_da_vez["Categoria"].lower() == tarefa_categoria.lower():
                    tarefa_encontradas = True
                    print(f"""
                    Nome: {tarefa_da_vez["Nome"]}
                    Descrição: {tarefa_da_vez["Descrição"]}
                    Prioridade: {tarefa_da_vez["Prioridade"]}
                    Categoria: {tarefa_da_vez["Categoria"]}
                    Concluída: {tarefa_da_vez["concluída"]}
                    """)
        

        case "6":
            print("Finalizado")
            break
        case _:
            print("Opção Inválida")
