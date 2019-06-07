# pyrdp
Python implementation of a recursive descent parser to parse mathematical expressions. 

The production rules used by pyrdp:

**E**  -> T E'

**E**' -> +T E' | & | -T E'

**T**  -> P T'

**T**' -> *P T' | & | /P T' | %P T'

**P**  -> F P'

**P**' -> ^F | &

**F**  -> (E) | id

Code presented as final work of Formal Languages and Automata discipline of Computer Science course.

# Usage
Example of valid inputs:

- "2*2+2"

- "(2+2)+2^2"

- "9%2"
