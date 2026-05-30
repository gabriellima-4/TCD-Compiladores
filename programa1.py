import re
import os

def prioridade(op):
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    return 0


def infixa_para_posfixa(expressao):

    expressao = expressao.replace(" ", "")

    saida = []
    pilha = []

    tokens = re.findall(r'\d+|[()+\-*/]', expressao)

    for token in tokens:

        if token.isdigit():
            saida.append(token)

        elif token == '(':
            pilha.append(token)

        elif token == ')':

            while pilha and pilha[-1] != '(':
                saida.append(pilha.pop())

            pilha.pop()

        else:

            while (
                pilha and
                pilha[-1] != '(' and
                prioridade(pilha[-1]) >= prioridade(token)
            ):
                saida.append(pilha.pop())

            pilha.append(token)

    while pilha:
        saida.append(pilha.pop())

    return " ".join(saida)


def processar_arquivo(nome_arquivo):

    if not os.path.exists(nome_arquivo):
        print("Arquivo não encontrado.")
        return

    with open(nome_arquivo, "r", encoding="utf-8") as arq:
        expressao = arq.read().strip()

    print("Expressão infixa:")
    print(expressao)

    print("\nExpressão pós-fixa:")
    print(infixa_para_posfixa(expressao))


arquivo = input("Digite o nome do arquivo: ")
processar_arquivo(arquivo)