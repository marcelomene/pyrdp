# pyrdp
Implementação em Python de um analisador descendente recursivo para expressões matemáticas.

As regras de produção usadas pelo pyrdp:

**E**  -> T E'

**E**' -> +T E' | & | -T E'

**T**  -> P T'

**T**' -> *P T' | & | /P T' | %P T'

**P**  -> F P'

**P**' -> ^F | &

**F**  -> (E) | id

Código apresentado como trabalho final da disciplina Linguagens Formais e Autômatos do curso de Ciência da Computação.

# Uso
Exemplo de entradas válidas:

- "2*2+2"

- "(2+2)+2^2"

- "9%2"
