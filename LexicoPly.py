import lex

reserved = {
'iniciar-programa' : 'COMANDO_INICIAR'
, 'finalizar-programa' : 'COMANDO_FINALIZAR'
, 'inicia-ejecucion' : 'COMANDO_INICIA'
, 'termina-ejecucion' : 'COMANDO_TERMINA'
, 'inicia-ejecucion' : 'COMANDO_INICIA'
, 'terminar' : 'COMANDO_TERMINAR'
, 'avanza' : 'COMANDO_AVANZAR'
, 'gira-izquierda' : 'COMANDO_GIRAR_IZQ'
, 'coge-zumbador' : 'COMANDO_COGER_ZUMBADOR'
, 'deja-zumbador' : 'COMANDO_DEJAR_ZUMBADOR'
, 'apagate' : 'COMANDO_APAGAR'
, 'define-nueva-instrucion' : 'SENTENCIA_DEFINE_NUEVA_INSTRUCCION'
, 'como' : 'SENTENCIA_COMO'
, 'si' : 'SENTENCIA_SI'
, 'entonces' : 'SENTENCIA_ENTONCES'
, 'sino' : 'SENTENCIA_SINO'
, 'repetir' : 'SENTENCIA_REPETIR'
, 'veces' : 'SENTENCIA_REPETIR_VECES'
, 'mientras' : 'SENTENCIA_MIENTRAS'
, 'hacer' : 'SENTENCIA_MIENTRAS_HACER'
, 'y' : 'OPERADOR_Y'
, 'o' : 'OPERADOR_O'
, 'no' : 'OPERADOR_NO'
, 'frente-libre' : 'CONDICION_FRENTE_LIBRE'
, 'junto-a-zumbador' : 'CONDICION_JUNTO_A_ZUMBADOR'	 
, 'orientado-al-este' : 'CONDICION_ORIENTADO_AL_ESTE'
, 'frente-bloqueado' : 'CONDICION_FRENTE_BLOQUEADO'	
, 'no-junto-a-zumbador' : 'CONDICION_NO_JUNTO_A_ZUMBADOR'
, 'orientado-al-oeste' : 'CONDICION_ORIENTADO_AL_OESTE'
, 'izquierda-libre' : 'CONDICION_IZQUIERDA_LIBRE'
, 'algun-zumbador-en-la-mochila' : 'CONDICION_ALGUN_ZUMBADOR_EN_LA_MOCHILA'
, 'no-orientado-al-norte' : 'CONDICION_NO_ORIENTADO_AL_NORTE'
, 'izquierda-bloqueada' : 'CONDICION_IZQUIERDA_BLOQUEADA'
, 'ningun-zumbador-en-la-mochila' : 	'CONDICION_NINGUN_ZUMBADOR_EN_LA_MOCHILA'
, 'no-orientado-al-sur' : 'CONDICION_NO_ORIENTADO_AL_SUR'
, 'derecha-libre' : 	'CONDICION_DERECHA_LIBRE'
, 'orientado-al-norte' : 'CONDICION_ORIENTADO_AL_NORTE'	
, 'no-orientado-al-este' : 'CONDICION_NO_ORIENTADO_AL_ESTE'
, 'derecha-bloqueada' : 'CONDICION_DERECHA_BLOQUEADA'	
, 'orientado-al-sur' : 'CONDICION_ORIENTADO_AL_SUR'	
, 'no-orientado-al-oeste' : 'CONDICION_NO_ORIENTADO_AL_OESTE'
, 'verdadero' : 'BOOLEANO_VERDADERO'
, 'falso' : 'BOOLEANO_FALSO'
, 'void' : 'DECLARACION_VOID'
, 'class' : 'DECLARACION_CLASS'
}

t_ignore = ' \n'
t_CONECTOR = r'-' #Token temporal, no puedo hacer que lea una palabra con un conector interno --> ej: no-orientado-al-oeste
t_PUNTUACION_PUNTO_Y_COMA = ';'
t_PUNTUACION_LLAVES_ABRIR = '{'
t_PUNTUACION_LLAVES_CERRAR = '}'
t_PUNTUACION_CORCHETES_ABRIR = r'\('
t_PUNTUACION_CORCHETES_CERRAR = r'\)'

tokens = ['PUNTUACION_PUNTO_Y_COMA','PUNTUACION_LLAVES_ABRIR','PUNTUACION_LLAVES_CERRAR','PUNTUACION_CORCHETES_ABRIR',
          'PUNTUACION_CORCHETES_CERRAR', 'NOMBRE', 'NUMERO', 'CONECTOR'] + list(reserved.values())
def t_NOMBRE(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'NOMBRE') 
     return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
def leerArchivo(entrada):
    return open(entrada, "r")

lex.lex() # Build the lexer
print(reserved.values())
for i in leerArchivo(input("introduzca el nombre del archivo con la extension .txt\n")):
    lex.input(i)
    while True:
        tok = lex.token()
        if not tok: break
        print (str(tok.value) + " - " + str(tok.type))
