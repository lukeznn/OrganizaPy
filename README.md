# OrganizaPy

Um gerenciador de tarefas simples, feito em Python, que funciona pelo terminal e salva os dados localmente em um arquivo JSON.

## Funcionalidades

- Adicionar tarefas com prioridade baixa, média ou alta.
- Listar tarefas cadastradas.
- Marcar tarefas como concluídas.
- Remover tarefas.
- Salvar os dados automaticamente, mesmo depois de fechar o programa.

## Requisitos

- Python 3.9 ou superior.
- Nenhuma biblioteca externa é necessária.

## Como executar

1. Baixe ou clone este repositório.
2. Abra o terminal na pasta do projeto.
3. Execute os comandos abaixo.

### Adicionar uma tarefa

```bash
python main.py adicionar "Estudar matemática" --prioridade alta
```

### Listar tarefas

```bash
python main.py listar
```

### Concluir uma tarefa

Use o número exibido na listagem:

```bash
python main.py concluir 1
```

### Remover uma tarefa

```bash
python main.py remover 1
```

Os dados são armazenados automaticamente em `tarefas.json`, criado na pasta do projeto.

## Estrutura

```text
OrganizaPy/
├── main.py
├── README.md
├── .gitignore
└── tests/
    └── test_main.py
```

## Tecnologias e conceitos utilizados

- Python
- Funções e estruturas condicionais
- Listas e dicionários
- Manipulação de arquivos
- JSON para persistência de dados
- Argumentos de linha de comando (`argparse`)
- Testes automatizados (`unittest`)

## Testes

Execute:

```bash
python -m unittest discover -s tests -v
```

## Objetivo do projeto

O OrganizaPy foi desenvolvido como projeto educacional para praticar lógica de programação, organização de código e persistência de dados.
