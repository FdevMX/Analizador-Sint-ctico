import ply.yacc as yacc
from main import tokens, lexer

errors = []

def p_for_loop(p):
    '''for_loop : FOR LPAREN initialization condition increment RPAREN LBRACE statement RBRACE'''
    if not errors:
        print("Estructura del bucle 'for' correcta")

def p_initialization(p):
    '''initialization : INT IDENTIFIER EQUALS NUMBER SEMICOLON
                      | IDENTIFIER EQUALS NUMBER SEMICOLON'''

def p_condition(p):
    '''condition : IDENTIFIER LESS_EQUAL NUMBER SEMICOLON'''

def p_increment(p):
    '''increment : IDENTIFIER INCREMENT
                 | INCREMENT IDENTIFIER'''

def p_statement(p):
    '''statement : SYSTEM DOT OUT DOT PRINTLN LPAREN STRING PLUS IDENTIFIER RPAREN SEMICOLON'''

def p_initialization_error(p):
    '''initialization : INT NUMBER EQUALS NUMBER SEMICOLON'''
    errors.append(f"Error en la línea {p.lineno(2) -1 }: No se puede usar un número como nombre de variable")

def p_increment_error(p):
    '''increment : IDENTIFIER PLUS'''
    errors.append(f"Error en la línea {p.lineno(2) - 1}: Incremento incorrecto, use '++' en lugar de '+'")

def p_error(p):
    if p:
        errors.append(f"Error de sintaxis en la línea {p.lineno - 1}, posición {p.lexpos}: Token inesperado '{p.value}'")
        parser.errok()
    else:
        check_for_missing_elements()

def check_for_missing_elements():
    stack_types = [t.type if t else '' for t in parser.symstack]
    if 'LBRACE' in stack_types and 'RBRACE' not in stack_types:
        errors.append("Error de sintaxis: Falta la llave de cierre '}' al final del bucle 'for'")
    if 'LPAREN' in stack_types and 'RPAREN' not in stack_types:
        errors.append("Error de sintaxis: Falta el paréntesis de cierre ')' en la declaración del bucle 'for'")
    if 'SEMICOLON' not in stack_types[-3:]:
        errors.append("Error de sintaxis: Falta un punto y coma ';' al final de una declaración")

def check_specific_errors(code):
    lines = code.split('\n')
    for i, line in enumerate(lines, 1):
        if 'System' in line and 'System.out.println' not in line:
            errors.append(f"Error en la línea {i}: Posible error en 'System.out.println', verifique la ortografía")
        if 'printn' in line:
            errors.append(f"Error en la línea {i}: 'printn' no es correcto, ¿quizás quiso decir 'println'?")

parser = yacc.yacc(debug=False)

def parse_for_loop(code):
    global errors
    errors = []
    lexer.lineno = 1
    check_specific_errors(code)
    result = parser.parse(code, lexer=lexer)
    if errors:
        print("Se encontraron los siguientes errores:")
        for error in errors:
            print(error)
    elif result is None:
        print("No se encontraron errores")
    return result

if __name__ == "__main__":
    code1 = '''
for (int 1 = 1; i <= 5; i+) {
    Syste.out.pritln("El valor de la cifra es: " + i);
'''
    print("Analizando código 1:")
    parse_for_loop(code1)

    print("\nAnalizando código 2:")
    code2 = '''
for (int 1 = 1; i <= 5; i+) {
    System.out.printn("El valor de la cifra es: " + i)
'''
    parse_for_loop(code2)