#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Marcelo Jordano C. Menezes | 201613917 | Ciência da Computação

Implementar um analisador recursivo descendente para avaliar expressões aritméticas, com as seguintes operações:

Adição +
Subtração -
Multiplicação *
Divisão /
Resto da Divisão Inteira %
Potenciação ^
A linguagem deve respeitar a prioridade natural dos operadores, e deve aceitar a inversão de prioridade mediante o uso de parênteses -- "(" e ")".

Gramática final implementada (após aplicação das regras de remoção de recursões a esquerda):

E  -> T E'
E' -> +T E' | & | -T E'
T  -> P T'
T' -> *P T' | & | /P T' | %P T'
P  -> F P'
P' -> ^F | &
F  -> (E) | id

"""

def getNumberIndex(inp):
    """Retorna o index do fim do valor numérico na string"""
    index = 0
    for i in range(0, len(inp)):
        if inp[i].isdigit():
            index = index + 1
        else:
            break 
    return index

def skip_spaces(inp):
    """Ignora espaços em branco no inicio da entrada."""
    return inp.lstrip()

def E(inp):
    inp = skip_spaces(inp)
    print("E -> T E'")
    inp, v1 = T(inp)
    inp, v2 = Eprime(inp,v1)
    return (inp, v2 if v2 is not None else v1)

def Eprime(inp, value):
    inp = skip_spaces(inp)
    print("E' -> +T E' | & | -T E'")
    if inp[0:1] == '+':
        inp, v1 = T(inp[1:])
        inp, v2 = Eprime(inp, value + v1)
        return(inp, v2 if v2 is not None else value)
    elif inp[0:1] == '-':
        inp, v1 = T(inp[1:])
        inp, v2 = Eprime(inp, value - v1)
        return(inp, v2 if v2 is not None else value)
    else:
        return(inp, value)
    
def T(inp):
    inp = skip_spaces(inp)
    print("T -> P T'")
    inp, v1 = P(inp)
    inp, v2 = Tprime(inp, v1)
    return(inp, v2 if v2 is not None else v1)
    
def Tprime(inp, value):
    inp = skip_spaces(inp)
    print("*P T' | & | /P T' | %P T'")
    if inp[0:1] == '*':
        inp, v1 = P(inp[1:])
        inp, v2 = Tprime(inp, value * v1)
        return(inp, v2 if v2 is not None else value)
    elif inp[0:1] == '/':
        inp, v1 = P(inp[1:])
        inp, v2 = Tprime(inp, value / v1)
        return(inp, v2 if v2 is not None else value)
    elif inp[0:1] == '%':
        inp, v1 = P(inp[1:])
        inp, v2 = Tprime(inp, value % v1)
        return(inp, v2 if v2 is not None else value)
    else:
        return(inp, value)
    
def P(inp):
    inp = skip_spaces(inp)
    print("P -> F P'")
    inp, v1 = F(inp)
    inp, v2 = Pprime(inp, v1)
    return (inp, v2 if v2 is not None else v1)

def Pprime(inp, value):
    inp = skip_spaces(inp)
    print("P' -> ^F | &")
    if inp[0:1] == '^':
        inp, v1 = F(inp[1:])
        return(inp, value ** v1)
    else:
        return(inp, None)
    
def F(inp):
    inp = skip_spaces(inp)
    print("F -> (E) | id")
    if inp[0:1] == '(':
        inp, value = E(inp[1:])
        inp = skip_spaces(inp)
        if inp[0:1] != ')':
            raise Exception("Esperado '(', obtido '{}'".format(inp[0]))
        return(inp[1:],value)
    else:
        maxIndex = getNumberIndex(inp)
        value = inp[:maxIndex]
        return(inp[maxIndex:],int(value))
        
if __name__ == "__main__":
    while True:
        entrada = input("Digite uma expressao:")
        if not entrada:
            break
        inp, result = E(entrada)
        print inp
        if inp:
            raise Exception("A entrada nao foi completamente utilizada.")
        print("Resultado:", result)
