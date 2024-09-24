import ply.yacc as yacc
from lex import tokens, print_tokens, lexer

precedence = (
    ('left', 'MAS'),
    ('left', 'MENOR_IGUAL'),
)

def p_programa(p):
    '''programa : sentencia_for'''
    p[0] = p[1]

def p_sentencia_for(p):
    '''sentencia_for : PALABRA_RESERVADA PARENTESIS_IZQ declaracion_for PARENTESIS_DER bloque'''
    p[0] = ("for", p[3], p[5])

def p_declaracion_for(p):
    '''declaracion_for : PALABRA_RESERVADA IDENTIFICADOR IGUAL NUMERO PUNTO_COMA condicion_for PUNTO_COMA incremento_for'''
    p[0] = ("for_declaracion", p[2], p[4], p[6], p[8])

def p_condicion_for(p):
    '''condicion_for : IDENTIFICADOR MENOR_IGUAL NUMERO'''
    p[0] = ("condicion", p[1], p[2], p[3])

def p_incremento_for(p):
    '''incremento_for : IDENTIFICADOR MAS MAS
                      | IDENTIFICADOR MAS'''
    if len(p) == 4:
        p[0] = ("incremento", p[1], "++")
    else:
        print(f"Error de sintaxis en línea {p.lineno(2)}, posición {p.lexpos(2)}: incremento incompleto '{p[1]}+'")
        p[0] = None

def p_bloque(p):
    '''bloque : LLAVE_IZQ sentencia_imprimir LLAVE_DER'''
    p[0] = p[2]

def p_sentencia_imprimir(p):
    '''sentencia_imprimir : PALABRA_RESERVADA PUNTO PALABRA_RESERVADA PUNTO PALABRA_RESERVADA PARENTESIS_IZQ expresion_concatenacion PARENTESIS_DER PUNTO_COMA'''
    p[0] = ("imprimir", p[7])

def p_expresion_concatenacion(p):
    '''expresion_concatenacion : COMILLAS cadena COMILLAS
                               | COMILLAS cadena COMILLAS MAS IDENTIFICADOR'''
    if len(p) == 4:
        p[0] = ("cadena", p[2])
    else:
        p[0] = ("concatenacion", p[2], p[5])

def p_cadena(p):
    '''cadena : IDENTIFICADOR
              | cadena IDENTIFICADOR
              | cadena MAYOR_QUE
              | cadena MENOR_IGUAL
              | cadena IGUAL
              | cadena MAS
              | cadena PUNTO
              | cadena PUNTO_COMA
              | cadena NUMERO
              | '''
    if len(p) == 1:
        p[0] = ""
    elif len(p) == 2:
        p[0] = str(p[1])
    else:
        p[0] = p[1] + str(p[2])

def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}, posición {p.lexpos}: token inesperado '{p.value}'")
    else:
        print("Error de sintaxis: fin de archivo inesperado")

parser = yacc.yacc()

def analizar_codigo(data):
    lexer.lineno = 0
    result = parser.parse(data)
    if result:
        print("Análisis sintáctico completado con éxito.")
    else:
        print("Error en el análisis sintáctico.")

# Ejemplo de código en Java con un error en el incremento
data = '''
for (int i = 1; i <= 5; i+) { 
    System.out.println("El valor de la cifra es: " + i);
}
'''

analizar_codigo(data)
print_tokens(data)