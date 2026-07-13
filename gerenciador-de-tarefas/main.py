import json
import os

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


def adicionar_tarefa(tarefas):
    print("\n=== Nova Tarefa ===")

    titulo = input("Título: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade (Baixa/Média/Alta): ")

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "concluida": False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

    print("\nTarefa adicionada com sucesso!\n")


def listar_tarefas(tarefas):
    print("\n===== TAREFAS =====")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas):
        status = "✔ Concluída" if tarefa["concluida"] else "❌ Pendente"

        print(f"""
ID: {i}
Título: {tarefa['titulo']}
Descrição: {tarefa['descricao']}
Prioridade: {tarefa['prioridade']}
Status: {status}
""")


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    if not tarefas:
        return

    try:
        indice = int(input("Digite o ID da tarefa: "))

        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa concluída!")
        else:
            print("ID inválido.")

    except ValueError:
        print("Digite um número válido.")


def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    if not tarefas:
        return

    try:
        indice = int(input("Digite o ID para excluir: "))

        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            salvar_tarefas(tarefas)
            print("Tarefa removida.")
        else:
            print("ID inválido.")

    except ValueError:
        print("Digite um número válido.")


def menu():
    tarefas = carregar_tarefas()

    while True:

        print("""
======== GERENCIADOR DE TAREFAS ========

1 - Adicionar Tarefa
2 - Listar Tarefas
3 - Concluir Tarefa
4 - Excluir Tarefa
0 - Sair

========================================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            concluir_tarefa(tarefas)

        elif opcao == "4":
            excluir_tarefa(tarefas)

        elif opcao == "0":
            print("Até logo!")
            break

        else:
            print("Opção inválida.")


menu()