# ✅ Gerenciador de Tarefas CLI

Um sistema simples de gerenciamento de tarefas desenvolvido em **Python**, executado diretamente no terminal. O programa permite cadastrar tarefas, acompanhar seu andamento e armazenar todas as informações em um arquivo JSON.

---

## 📌 Funcionalidades

* ✅ Adicionar tarefas
* ✅ Listar tarefas cadastradas
* ✅ Marcar tarefas como concluídas
* ✅ Excluir tarefas
* ✅ Armazenamento automático em JSON
* ✅ Interface simples via terminal (CLI)

---

## 🛠 Tecnologias Utilizadas

* Python 3
* JSON
* Biblioteca `os`

Todas as bibliotecas utilizadas fazem parte da biblioteca padrão do Python.

---

## 📁 Estrutura do Projeto

```text
todo-cli/
│
├── main.py
├── tarefas.json      # Criado automaticamente
└── README.md
```

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/todo-cli.git
```

### 2. Entre na pasta

```bash
cd todo-cli
```

### 3. Execute

```bash
python main.py
```

---

## 💻 Exemplo de Uso

```text
======== GERENCIADOR DE TAREFAS ========

1 - Adicionar Tarefa
2 - Listar Tarefas
3 - Concluir Tarefa
4 - Excluir Tarefa
0 - Sair
```

### Exemplo de cadastro

```text
Título: Estudar Python
Descrição: Revisar funções e listas
Prioridade: Alta
```

### Listagem

```text
ID: 0

Título: Estudar Python
Descrição: Revisar funções e listas
Prioridade: Alta
Status: ❌ Pendente
```

Após concluir:

```text
Status: ✔ Concluída
```

---

## 💾 Armazenamento

As tarefas são salvas automaticamente no arquivo `tarefas.json`.

Exemplo:

```json
[
    {
        "titulo": "Estudar Python",
        "descricao": "Revisar funções e listas",
        "prioridade": "Alta",
        "concluida": false
    }
]
```

---

## 🎯 Objetivos do Projeto

Este projeto foi desenvolvido para praticar:

* Manipulação de arquivos JSON
* Estruturas de dados
* Funções
* Modularização
* Persistência de dados
* Desenvolvimento de aplicações CLI
* Tratamento básico de erros

---

## 🚀 Melhorias Futuras

* Editar tarefas
* Definir data de vencimento
* Pesquisar tarefas
* Filtrar por prioridade
* Filtrar por status
* Exportar para CSV
* Utilizar SQLite
* Login de usuários
* Testes automatizados com `pytest`

---

## 👨‍💻 Autor

Desenvolvido por **Maria Anjos** como projeto de estudos em Python.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
