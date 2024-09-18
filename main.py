import json
import re
from datetime import datetime

dir_file = "dados.json"

# Função para carregar dados de um arquivo JSON
def carregar_dados():
    try:
        with open(dir_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Arquivo '{dir_file}' não encontrado ou inválido. Criando uma nova lista de tarefas.")
        return {"tarefas": []}

# Função para salvar dados no arquivo JSON
def salvar_dados():
    with open(dir_file, 'w') as f:
        json.dump(dados, f, indent=4)

# Carregar os dados na memória
dados = carregar_dados()

# Função para gerar o próximo ID
def proximo_id():
    return dados['tarefas'][-1]["id"] + 1 if dados['tarefas'] else 1

# Função para inserir nova tarefa
def insert(description):
    id = proximo_id()
    data_atual = datetime.now().isoformat()
    nova_tarefa = {
        "id": id,
        "description": description,
        "status": "todo",
        "createdAt": data_atual,
        "updatedAt": data_atual
    }
    dados['tarefas'].append(nova_tarefa)
    print(f"Task added successfully (ID: {id})")
    salvar_dados()

# Função para deletar tarefa
def delete(id):
    tarefa = next((t for t in dados['tarefas'] if t['id'] == id), None)
    if tarefa:
        dados['tarefas'].remove(tarefa)
        print(f"Task deleted successfully (ID: {id})")
        salvar_dados()
    else:
        print(f"Task not found (ID: {id})")

# Função para listar tarefas
def list(status=None):
    tarefas_filtradas = dados['tarefas'] if status is None else [t for t in dados['tarefas'] if t['status'] == status]
    for tarefa in tarefas_filtradas:
        print(f"Tarefa {tarefa['id']}: {tarefa['description']} - Status: {tarefa['status']}")

# Função para alterar o status da tarefa
def altstatus(id, new_status):
    tarefa = next((t for t in dados['tarefas'] if t['id'] == id), None)
    if tarefa:
        tarefa['status'] = new_status
        tarefa['updatedAt'] = datetime.now().isoformat()
        print(f"Status updated successfully (ID: {id}, New Status: {new_status})")
        salvar_dados()
    else:
        print(f"Task not found (ID: {id})")

# Função para atualizar a descrição da tarefa
def update(id, description):
    tarefa = next((t for t in dados['tarefas'] if t['id'] == id), None)
    if tarefa:
        tarefa['description'] = description
        tarefa['updatedAt'] = datetime.now().isoformat()
        print(f"Task description updated successfully (ID: {id})")
        salvar_dados()
    else:
        print(f"Task not found (ID: {id})")

# Função para processar a ação
def processar_comando(action):
    if "add" in action:
        match = re.search(r'\"(.*?)\"', action)
        if match:
            description = match.group(1)
            insert(description)

    elif "update" in action:
        match = re.search(r'\"(.*?)\"', action)
        if match:
            description = match.group(1)
            id = int(action.split()[2])
            update(id, description)

    elif "delete" in action:
        id = int(action.split()[2])
        delete(id)

    elif "list" in action:
        if "in-progress" in action:
            list("In-Progress")
        elif "done" in action:
            list("done")
        elif "todo" in action:
            list("todo")
        else:
            list()

    elif "mark" in action:
        id = int(action.split()[2])
        if "in-progress" in action:
            altstatus(id, "In-Progress")
        elif "done" in action:
            altstatus(id, "done")

# Loop para processar comandos continuamente
while True:
    action = input().strip()
    processar_comando(action)
