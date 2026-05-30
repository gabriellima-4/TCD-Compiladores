import re
import os

tabela_simbolos = {
    "if": "PALAVRA_CHAVE",
    "while": "PALAVRA_CHAVE",
    "for": "PALAVRA_CHAVE",
    "int": "PALAVRA_CHAVE",
    "float": "PALAVRA_CHAVE"
}


def remover_comentarios(codigo):

    codigo = re.sub(
        r'/\*.*?\*/',
        '',
        codigo,
        flags=re.DOTALL
    )

    codigo = re.sub(
        r'//.*',
        '',
        codigo
    )

    return codigo


def analise_lexica(codigo):

    erros = []

    padrao = (
        r'<=|>=|==|!=|'
        r'[+\-*/=<>]|'
        r'\d+\.\d+|'
        r'\d+|'
        r'[A-Za-z_]\w*|'
        r'[();{}]'
    )

    print("\nTABELA DE SÍMBOLOS")
    print("-" * 50)
    print("LINHA\tLEXEMA\t\tTOKEN")

    for numero_linha, linha in enumerate(
        codigo.splitlines(),
        start=1
    ):

        linha = linha.strip()

        posicoes_validas = []

        for match in re.finditer(padrao, linha):

            lexema = match.group()
            posicoes_validas.extend(
                range(match.start(), match.end())
            )

            if re.fullmatch(r'\d+\.\d+', lexema):
                token = "NUMERO_DECIMAL"

            elif re.fullmatch(r'\d+', lexema):
                token = "NUMERO"

            elif lexema in ['+', '-', '*', '/']:
                token = "OPERADOR_ARITMETICO"

            elif lexema in [
                '<', '>', '<=', '>=',
                '==', '!='
            ]:
                token = "OPERADOR_RELACIONAL"

            elif lexema in [
                '(', ')', ';', '{', '}'
            ]:
                token = "DELIMITADOR"

            elif lexema in tabela_simbolos:
                token = tabela_simbolos[lexema]

            else:

                tabela_simbolos[lexema] = "IDENTIFICADOR"
                token = "IDENTIFICADOR"

            print(
                f"{numero_linha}\t"
                f"{lexema}\t\t"
                f"{token}"
            )

        # recuperação de erro

        for indice, caractere in enumerate(linha):

            if (
                indice not in posicoes_validas
                and not caractere.isspace()
            ):

                erros.append(
                    f"Linha {numero_linha}: "
                    f"caractere inválido '{caractere}'"
                )

    return erros


def processar_arquivo(nome_arquivo):

    if not os.path.exists(nome_arquivo):
        print("Arquivo não encontrado.")
        return

    with open(
        nome_arquivo,
        "r",
        encoding="utf-8"
    ) as arq:

        codigo = arq.read()

    codigo = remover_comentarios(codigo)

    erros = analise_lexica(codigo)

    print("\nERROS")

    if erros:

        for erro in erros:
            print(erro)

    else:
        print("Nenhum erro encontrado.")


arquivo = input(
    "Digite o nome do arquivo: "
)

processar_arquivo(arquivo)