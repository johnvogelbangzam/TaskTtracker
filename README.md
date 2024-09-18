
# Gerenciador de Tarefas em Python

Este programa é um gerenciador de tarefas baseado em linha de comando que utiliza um arquivo JSON para armazenamento. Ele permite adicionar, atualizar, deletar, listar e alterar o status de tarefas.

## Funcionalidades

- **Adicionar tarefa**: Adiciona uma nova tarefa à lista.
- **Atualizar tarefa**: Atualiza a descrição de uma tarefa existente.
- **Deletar tarefa**: Remove uma tarefa da lista.
- **Listar tarefas**: Exibe todas as tarefas ou filtra por status (`todo`, `in-progress`, `done`).
- **Alterar status**: Muda o status de uma tarefa para `in-progress` ou `done`.

## Instalação

1. Clone o repositório ou copie o código para o seu ambiente local.
2. Certifique-se de ter Python instalado (versão 3.6 ou superior).
3. O programa utiliza o arquivo `dados.json` para armazenar as tarefas. Se o arquivo não existir, ele será criado automaticamente.

## Uso

Você pode executar o script e usar os seguintes comandos no terminal para interagir com o programa:

### Adicionar uma nova tarefa

```bash
puthon3 ./main.py
task-cli add "descrição da tarefa"
```

Exemplo:

```bash
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### Atualizar uma tarefa

```bash
task-cli update <id> "nova descrição da tarefa"
```

Exemplo:

```bash
task-cli update 1 "Buy groceries and cook dinner"
```

### Deletar uma tarefa

```bash
task-cli delete <id>
```

Exemplo:

```bash
task-cli delete 1
```

### Alterar o status de uma tarefa para "In-Progress"

```bash
task-cli mark-in-progress <id>
```

Exemplo:

```bash
task-cli mark-in-progress 1
```

### Alterar o status de uma tarefa para "Done"

```bash
task-cli mark-done <id>
```

Exemplo:

```bash
task-cli mark-done 1
```

### Listar todas as tarefas

```bash
task-cli list
```

### Listar tarefas por status

Para listar tarefas que estão concluídas (`done`):

```bash
task-cli list done
```

Para listar tarefas que ainda precisam ser feitas (`todo`):

```bash
task-cli list todo
```

Para listar tarefas que estão em progresso (`in-progress`):

```bash
task-cli list in-progress
```

## Estrutura do JSON

As tarefas são armazenadas em um arquivo `dados.json` com a seguinte estrutura:

```json
{
    "tarefas": [
        {
            "id": 1,
            "description": "Buy groceries",
            "status": "todo",
            "createdAt": "2024-09-18T10:00:00",
            "updatedAt": "2024-09-18T10:00:00"
        }
    ]
}
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é de código aberto e está disponível sob a licença MIT.