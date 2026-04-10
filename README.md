# Trabalho-de-Engenharia-de-Software

# Trabalho-de-Engenharia-de-Software


# Trabalho de Engenharia de Software

Sistema simples de controle de vagas de estacionamento feito em Python.

O projeto representa as vagas como objetos, permite listar e alterar o status de uma vaga e inclui uma função para contar quantas vagas estão disponíveis.

## Como o projeto está organizado

- [main.py](main.py): cria a lista inicial de vagas do estacionamento.
- [vaga.py](vaga.py): define a classe `Vaga` com os dados da vaga e seus métodos.
- [funcaoVaga.py](funcaoVaga.py): contém funções de menu e de alteração de status.
- [contador_vagas.py](contador_vagas.py): função para contar vagas livres.
- [contador_vagas..py](contador_vagas..py): script de teste para validar a contagem de vagas.

## Explicação rápida

- Cada vaga tem `id`, `tipo` e `status`.
- O `tipo` pode ser, por exemplo, `Reservada` ou `Comum`.
- O `status` indica se a vaga está disponível ou ocupada.
- A lista de vagas é criada com 100 posições no arquivo principal.

## Execução

O projeto pode ser executado com Python no terminal.

Exemplo:

```bash
python main.py
```

Se quiser testar a contagem de vagas, execute o script:

```bash
python contador_vagas..py
```

## Observação

O projeto ainda está em uma versão básica. Se quiser, eu posso também organizar o README com imagens, exemplo de uso e diagrama das classes.
