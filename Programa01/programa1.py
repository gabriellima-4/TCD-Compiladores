import re
import os

def prioridade(op):
    # Define a precedencia dos operadores aritmeticos.
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    return 0


def infixa_para_posfixa(expressao):

    # Remove espacos para facilitar a separacao dos tokens.
    expressao = expressao.replace(" ", "")

    saida = []
    pilha = []

    # Captura numeros, parenteses e operadores da expressao.
    tokens = re.findall(r'\d+|[()+\-*/]', expressao)

    for token in tokens:

        # Numeros ja podem ir diretamente para a saida.
        if token.isdigit():
            saida.append(token)

        elif token == '(':
            pilha.append(token)

        elif token == ')':

            # Desempilha operadores ate encontrar o parenteses de abertura.
            while pilha and pilha[-1] != '(':
                saida.append(pilha.pop())

            pilha.pop()

        else:

            # Garante que operadores de maior ou igual precedencia saiam antes.
            while (
                pilha and
                pilha[-1] != '(' and
                prioridade(pilha[-1]) >= prioridade(token)
            ):
                saida.append(pilha.pop())

            pilha.append(token)

    # Ao final, todos os operadores restantes entram na saida.
    while pilha:
        saida.append(pilha.pop())

    return " ".join(saida)


def processar_arquivo(nome_arquivo):

    # Verifica se o arquivo informado existe antes de tentar abri-lo.
    if not os.path.exists(nome_arquivo):
        print("Arquivo não encontrado.")
        return

    # Le a expressao completa do arquivo.
    with open(nome_arquivo, "r", encoding="utf-8") as arq:
        expressao = arq.read().strip()

    print("Expressão infixa:")
    print(expressao)

    print("\nExpressão pós-fixa:")
    print(infixa_para_posfixa(expressao))


arquivo = input("Digite o nome do arquivo: ")
processar_arquivo(arquivo)
