import lex

reserved = {
'iniciar_programa' : 'COMANDO_INICIAR'
, 'finalizar_programa' : 'COMANDO_FINALIZAR'
, 'inicia_ejecucion' : 'COMANDO_INICIA'
, 'termina_ejecucion' : 'COMANDO_TERMINA'
, 'inicia_ejecucion' : 'COMANDO_INICIA'
, 'terminar' : 'COMANDO_TERMINAR'
, 'avanza' : 'COMANDO_AVANZAR'
, 'gira_izquierda' : 'COMANDO_GIRAR_IZQ'
, 'coge_zumbador' : 'COMANDO_COGER_ZUMBADOR'
, 'deja_zumbador' : 'COMANDO_DEJAR_ZUMBADOR'
, 'apagate' : 'COMANDO_APAGAR'
, 'define_nueva_instrucion' : 'SENTENCIA_DEFINE_NUEVA_INSTRUCCION'
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
, 'frente_libre' : 'CONDICION_FRENTE_LIBRE'
, 'junto_a_zumbador' : 'CONDICION_JUNTO_A_ZUMBADOR'	 
, 'orientado_al_este' : 'CONDICION_ORIENTADO_AL_ESTE'
, 'frente_bloqueado' : 'CONDICION_FRENTE_BLOQUEADO'	
, 'no_junto_a_zumbador' : 'CONDICION_NO_JUNTO_A_ZUMBADOR'
, 'orientado_al_oeste' : 'CONDICION_ORIENTADO_AL_OESTE'
, 'izquierda_libre' : 'CONDICION_IZQUIERDA_LIBRE'
, 'algun_zumbador_en_la_mochila' : 'CONDICION_ALGUN_ZUMBADOR_EN_LA_MOCHILA'
, 'no_orientado_al_norte' : 'CONDICION_NO_ORIENTADO_AL_NORTE'
, 'izquierda_bloqueada' : 'CONDICION_IZQUIERDA_BLOQUEADA'
, 'ningun_zumbador_en_la_mochila' : 	'CONDICION_NINGUN_ZUMBADOR_EN_LA_MOCHILA'
, 'no_orientado_al_sur' : 'CONDICION_NO_ORIENTADO_AL_SUR'
, 'derecha_libre' : 	'CONDICION_DERECHA_LIBRE'
, 'orientado_al_norte' : 'CONDICION_ORIENTADO_AL_NORTE'	
, 'no_orientado_al_este' : 'CONDICION_NO_ORIENTADO_AL_ESTE'
, 'derecha_bloqueada' : 'CONDICION_DERECHA_BLOQUEADA'	
, 'orientado_al_sur' : 'CONDICION_ORIENTADO_AL_SUR'	
, 'no_orientado_al_oeste' : 'CONDICION_NO_ORIENTADO_AL_OESTE'
, 'verdadero' : 'BOOLEANO_VERDADERO'
, 'falso' : 'BOOLEANO_FALSO'
, 'void' : 'DECLARACION_VOID'
, 'class' : 'DECLARACION_CLASS'
}

t_ignore = ' \n | \t'
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

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
def leerArchivo(entrada):
    return open(entrada, "r")

def remplazar(texto):
     texto = texto.replace("_","_SUBLINE_")
     texto = texto.replace("-","_")
     return texto

lex.lex()
for i in leerArchivo(input("introduzca el nombre del archivo con la extension .txt\n")):
    lex.input(remplazar(i))
    while True:
        tok = lex.token()
        if not tok: break
        print (str(tok.value) + " - " + str(tok.type))
