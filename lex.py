import ply.lex as lex

# Lista de palabras reservadas
reserved = {
    'if': 'PALABRA_RESERVADA',
    'for': 'PALABRA_RESERVADA',
    'int': 'PALABRA_RESERVADA',
    'System': 'PALABRA_RESERVADA',
    'out': 'PALABRA_RESERVADA',
    'println': 'PALABRA_RESERVADA'
}

# Lista de tokens
tokens = [
    'IDENTIFICADOR',
    'NUMERO',
    'MAYOR_QUE',
    'MENOR_IGUAL',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'LLAVE_IZQ',
    'LLAVE_DER',
    'IGUAL',
    'MAS',
    'PUNTO',
    'PUNTO_COMA',
    'COMILLAS',
    'DOSPUNTOS',  # Agrega este
    'CADENA_TEXTO',  # Agrega este
] + list(reserved.values())

# Definición de tokens
t_MAYOR_QUE = r'>'
t_MENOR_IGUAL = r'<='
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_IGUAL = r'='
t_MAS = r'\+'
t_PUNTO = r'\.'
t_PUNTO_COMA = r';'
t_COMILLAS = r'\"'  # Manejo de comillas para cadenas
t_DOSPUNTOS = r':'  # Agrega este


# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Definición para cadenas de texto
def t_CADENA_TEXTO(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Elimina las comillas alrededor de la cadena
    return t

# Definición para números
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Definición para identificadores y palabras reservadas
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')  # Verificar si es palabra reservada
    return t

# Contador de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Función para imprimir tokens
def print_tokens(data):
    lexer.input(data)
    lexer.lineno = 1  # Empezar la numeración desde la línea 1
    print(f"{'Token':<20} {'Lexema':<20} {'Línea'}")
    print("-" * 50)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"{tok.type:<20} {tok.value:<20} {tok.lineno}")

def get_tokens(data):
    lexer.input(data)
    lexer.lineno = 1
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append((tok.type, tok.value, tok.lineno))
    return tokens
