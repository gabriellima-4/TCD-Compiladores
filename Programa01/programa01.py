"""
Programa 01 - devera traduzir as expressões infixas com: 
Números inteiros de um e/ou mais de um dígito; 
Os operadores aritméticos (*, /, +, -); e  
Espaços. 
Implementar e entregar, os seguintes itens: 
1. Desenvolver um programa em código _fonte utilizando a linguagem C (faremos em python). que: 
2. Traduza uma expressão infixa para a forma pós-fixa;  
3. Lógica pura usando a tabela de símbolos versão 1 (sem ponteiro); 
4. Diagrama de Transição com Case.

"""

###############################################################################################
###############################################################################################

#--------------------#
# Tabela de Símbolos #
#--------------------#






#---------------------------#
# Prioridade dos Operadores #
#---------------------------#
def prioridade(op):
    match op:
        case '+' | '-':
            return 1
        
        case '*' | '/':
            return 2
        
        case _:
            return 0






















def tradutor_de_expressoes():
    pass