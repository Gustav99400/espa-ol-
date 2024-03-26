import ply.lex as lex

tokens = (
    'PROGRAMA',
    'INICIO',
    'FIN',
    'FUNCION',
    'PARA',
    'SI',
    'ENTONCES',
    'SINO',
    'CONCATENAR',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'BOOLEANO',
    'MOSTRAR',
    'RETORNAR',
    'IDENTIFICADOR',
    'NUMERO',
    'NUMDECIMAL',
    'PUNTO',
    'ASIGNACION',
    'IGUALDAD',
    'MENOR',
    'MAYOR',
    'MENORIGUAL',
    'MAYORIGUAL',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'COMA',
    'PARENTESIS_A',
    'PARENTESIS_C',
    'PUNTO_COMA',
    'INCREMENTO',
)

# Expresiones regulares para tokens simples
t_ASIGNACION = r'='
t_IGUALDAD = r'=='
t_MENOR = r'<'
t_MAYOR = r'>'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_COMA = r','
t_PUNTO = r'\.'
t_PARENTESIS_A = r'\('
t_PARENTESIS_C = r'\)'
t_PUNTO_COMA = r';'
t_INCREMENTO = r'\+\+'

# Expresion regular para CADENA
def t_CADENA(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Elimina las comillas
    return t

def t_COMENTARIO_LINEA(t):
    r'//.*'
    pass

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Expresiones regulares con acciones asociadas
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')  # Chequea si es palabra reservada
    return t

def t_NUMERO(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_NUMDECIMAL(t):
    r'[-+]?[0-9]*\.?[0-9]+'
    t.value = float(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Palabras reservadas
reserved = {
    'PROGRAMA': 'PROGRAMA',
    'INICIO': 'INICIO',
    'FIN': 'FIN',
    'FUNCION': 'FUNCION',
    'PARA': 'PARA',
    'SI': 'SI',
    'ENTONCES': 'ENTONCES',
    'SINO': 'SINO',
    'CONCATENAR': 'CONCATENAR',
    'ENTERO': 'ENTERO',
    'DECIMAL': 'DECIMAL',
    'CADENA': 'CADENA',
    'BOOLEANO': 'BOOLEANO',
    'MOSTRAR': 'MOSTRAR',
    'RETORNAR': 'RETORNAR'
}

# Prueba del lexer
data = '''
PROGRAMA HolaMundo
INICIO
    MOSTRAR "¡Hola, mundo!".
FIN.

PROGRAMA FactorialIterativo
INICIO
    ENTERO numero = 5.
    ENTERO factorial = 1.

    PARA ENTERO i = 1; i <= numero; i++.
    INICIO
        factorial = factorial * i.
    FIN

    MOSTRAR "El factorial de " CC numero CC " es: " CC factorial CC ".".
FIN.

PROGRAMA FactorialRecursivo
INICIO
    ENTERO numero = 5.
    ENTERO resultado = factorialRecursivo(numero).
    MOSTRAR "El factorial de " CC numero CC " es: " CC resultado CC ".".
FIN.

FUNCION ENTERO factorialRecursivo(ENTERO n)
INICIO
    SI n == 0 ENTONCES
    INICIO
        RETORNAR 1.
    FIN
    SINO
    INICIO
        RETORNAR n * factorialRecursivo(n - 1).
    FIN SI
FIN.
'''
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

lexer.input(data)

token_list = []

while True:
    tok = lexer.token()
    if not tok:
        break
    token_info = {
        'type': tok.type,
        'value': tok.value,
        'lineno': tok.lineno,
        'lexpos': tok.lexpos
    }
    token_list.append(token_info)

print(token_list)