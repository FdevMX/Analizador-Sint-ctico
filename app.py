from flask import Flask, render_template, request, jsonify
from lex import lexer, print_tokens
from yacc import parser, analizar_codigo
import io
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.json['code']
    
    # Capturar la salida del analizador léxico
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    
    print_tokens(code)
    
    lexer_output = buffer.getvalue()
    sys.stdout = old_stdout
    
    # Analizar el código
    parser_output = io.StringIO()
    sys.stdout = parser_output
    analizar_codigo(code)
    parser_message = parser_output.getvalue()
    sys.stdout = old_stdout
    
    # Procesar la salida del analizador léxico para crear una lista de tokens
    tokens = []
    for line in lexer_output.split('\n')[2:]:  # Saltar las dos primeras líneas (encabezado)
        if line.strip():
            parts = line.split()
            if len(parts) >= 3:
                token = parts[0]
                linea = parts[-1]
                lexema = ' '.join(parts[1:-1])  # Todo lo que está entre el token y la línea es el lexema
                tokens.append({'token': token, 'lexema': lexema, 'linea': linea})
    
    return jsonify({
        'parser_message': parser_message,
        'tokens': tokens
    })

if __name__ == '__main__':
    app.run(debug=True)