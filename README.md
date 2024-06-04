# Gerenciador de Tarefas - Atividade de Backend com Cartesi Rollups

## Descrição

Este repositório contém um backend de exemplo que simula um gerenciador de tarefas utilizando Cartesi Rollups. O objetivo desta atividade é educar os alunos sobre o desenvolvimento de backends e a resolução de problemas comuns em ambientes do Cartesi Rollups. O backend foi propositalmente implementado com alguns erros que os alunos devem identificar e corrigir. Conceitos podem estar misturados, podem haver logicas incorretas de codigo, entre outros.

## Objetivo

Os alunos devem:

1.  Analisar o código fornecido.
2.  Identificar os erros propositais no backend.
3.  Corrigir os erros e validar as correções.
4.  Garantir que o backend funcione corretamente para as ações de criação, listagem e exclusão de tarefas.

### Estrutura de Dados

-   **tasks**: Um dicionário que armazena as tarefas com `id` como chave e `description` como valor.

## JSONs de Entrada

### Criar Tarefa


`{
    "action": "create",
    "id": "1",
    "description": "Estudar blockchain"
}` 

usando o cartesi send:
```bash
cartesi send generic \
    --dapp=0xab7528bb862fB57E8A2BCd567a2e929a0Be56a5e \
    --chain-id=31337 \
    --rpc-url=http://127.0.0.1:8545 \
    --mnemonic-passphrase='test test test test test test test test test test test junk' \
    --input="{"action": "create","id": "1","description": "Estudar blockchain"}"
```
### Listar Tarefas


`{
    "action": "list"
}` 

usando o cartesi send:
```bash
cartesi send generic \
    --dapp=0xab7528bb862fB57E8A2BCd567a2e929a0Be56a5e \
    --chain-id=31337 \
    --rpc-url=http://127.0.0.1:8545 \
    --mnemonic-passphrase='test test test test test test test test test test test junk' \
    --input="{"action": "list"}"
```
### Deletar Tarefa


`{
    "action": "delete",
    "id": "1"
}` 

usando o cartesi send:
```bash
cartesi send generic \
    --dapp=0xab7528bb862fB57E8A2BCd567a2e929a0Be56a5e \
    --chain-id=31337 \
    --rpc-url=http://127.0.0.1:8545 \
    --mnemonic-passphrase='test test test test test test test test test test test junk' \
    --input="{"action": "delete","id": "1"}"
```

### Ação Inválida


`{
    "action": "invalid_action"
}` 

usando o cartesi send:
```bash
cartesi send generic \
    --dapp=0xab7528bb862fB57E8A2BCd567a2e929a0Be56a5e \
    --chain-id=31337 \
    --rpc-url=http://127.0.0.1:8545 \
    --mnemonic-passphrase='test test test test test test test test test test test junk' \
    --input="{"action": "invalid_action"}"
```
## JSONs de Resposta

### Criar Tarefa - Sucesso


`{
    "message": "Task '1' created"
}` 

### Criar Tarefa - Erro


`{
    "error": "Task ID already exists"
}` 

### Listar Tarefas


`{
    "tasks": {
        "1": "Estudar blockchain",
        "2": "Revisar contratos inteligentes"
    }
}` 

### Deletar Tarefa - Sucesso


`{
    "message": "Task '1' deleted"
}` 

### Ação Inválida


`{
    "error": "Invalid action"
}` 

## Passos para a Atividade

1.  **Clone o Repositório**
    
    `git clone <URL do repositório>
    cd <diretório do repositório>` 
    
2.  **Analise o Código**
    
    -   Examine o código e identifique possíveis erros.
    
3.  **Corrija os Erros**
    
    -   Identifique e corrija os erros no código.
    -   Reexecute os testes para verificar se as correções foram bem-sucedidas.

## Dicas

-   Verifique os logs gerados pelo servidor para entender melhor os erros.

Boa sorte e bom aprendizado!

----------
