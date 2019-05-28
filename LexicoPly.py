import lex

tokens = ['COMANDO_INICIAR','COMANDO_FINALIZAR','COMANDO_AVANZAR','COMANDO_GIRAR_IZQ','COMANDO_COGER_ZUMBADOR', 'COMANDO_DEJAR_ZUMBADOR', 'COMANDO_APAGAR','SENTENCIA_DEFINE_NUEVA_INSTRUCCION','SENTENCIA_COMO','SENTENCIA_SI','SENTENCIA_ENTONCES','SENTENCIA_SINO','SENTENCIA_REPETIR','SENTENCIA_REPETIR_VECES','SENTENCIA_MIENTRAS','SENTENCIA_MIENTRAS_HACER','OPERADOR_Y','OPERADOR_O','OPERADOR_NO','CONDICION_FRENTE_LIBRE','CONDICION_JUNTO_A_ZUMBADOR','CONDICION_ORIENTADO_AL_ESTE','CONDICION_FRENTE_BLOQUEADO','CONDICION_NO_JUNTO_A_ZUMBADOR','CONDICION_ORIENTADO_AL_OESTE','CONDICION_IZQUIERDA_LIBRE','CONDICION_ALGUN_ZUMBADOR_EN_LA_MOCHILA','CONDICION_NO_ORIENTADO_AL_NORTE','CONDICION_IZQUIERDA_BLOQUEADA','CONDICION_NINGUN_ZUMBADOR_EN_LA_MOCHILA','CONDICION_NO_ORIENTADO_AL_SUR','CONDICION_DERECHA_LIBRE','CONDICION_ORIENTADO_AL_NORTE','CONDICION_NO_ORIENTADO_AL_ESTE','CONDICION_DERECHA_BLOQUEADA','CONDICION_ORIENTADO_AL_SUR','CONDICION_NO_ORIENTADO_AL_OESTE','BOOLEANO_VERDADERO','BOOLEANO_FALSO']
t_COMANDO_INICIAR = 'iniciar-'
t_COMANDO_FINALIZAR = 'finalizar-'
t_COMANDO_AVANZAR = 'avanza'
t_COMANDO_GIRAR_IZQ = 'gira-izquierda'
t_COMANDO_COGER_ZUMBADOR = 'coge-zumbador'
t_COMANDO_DEJAR_ZUMBADOR = 'deja-zumbador'
t_COMANDO_APAGAR = 'apagate'
t_SENTENCIA_DEFINE_NUEVA_INSTRUCCION = 'define-nueva-instrucion'
t_SENTENCIA_COMO = 'como'
t_SENTENCIA_SI = 'si'
t_SENTENCIA_ENTONCES = 'entonces'
t_SENTENCIA_SINO = 'sino'
t_SENTENCIA_REPETIR = 'repetir'
t_SENTENCIA_REPETIR_VECES = 'veces'
t_SENTENCIA_MIENTRAS = 'mientras'
t_SENTENCIA_MIENTRAS_HACER = 'hacer'
t_OPERADOR_Y = 'y'
t_OPERADOR_O = 'o'
t_OPERADOR_NO = 'no'
t_CONDICION_FRENTE_LIBRE = 'frente-libre'
t_CONDICION_JUNTO_A_ZUMBADOR = 'junto-a-zumbador'	 
t_CONDICION_ORIENTADO_AL_ESTE = 'orientado-al-este'
t_CONDICION_FRENTE_BLOQUEADO = 'frente-bloqueado'	
t_CONDICION_NO_JUNTO_A_ZUMBADOR = 'no-junto-a-zumbador'	
t_CONDICION_ORIENTADO_AL_OESTE = 'orientado-al-oeste'
t_CONDICION_IZQUIERDA_LIBRE = 'izquierda-libre'	
t_CONDICION_ALGUN_ZUMBADOR_EN_LA_MOCHILA = 'algun-zumbador-en-la-mochila'
t_CONDICION_NO_ORIENTADO_AL_NORTE = 'no-orientado-al-norte'
t_CONDICION_IZQUIERDA_BLOQUEADA = 'izquierda-bloqueada'	
t_CONDICION_NINGUN_ZUMBADOR_EN_LA_MOCHILA = 'ningun-zumbador-en-la-mochila'	
t_CONDICION_NO_ORIENTADO_AL_SUR = 'no-orientado-al-sur'
t_CONDICION_DERECHA_LIBRE = 'derecha-libre'	
t_CONDICION_ORIENTADO_AL_NORTE = 'orientado-al-norte'	
t_CONDICION_NO_ORIENTADO_AL_ESTE = 'no-orientado-al-este'
t_CONDICION_DERECHA_BLOQUEADA = 'derecha-bloqueada'	
t_CONDICION_ORIENTADO_AL_SUR = 'orientado-al-sur'	
t_CONDICION_NO_ORIENTADO_AL_OESTE = 'no-orientado-al-oeste'
t_BOOLEANO_VERDADERO = 'verdadero'
t_BOOLEANO_FALSO = 'falso'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
def leerArchivo():
    return open("comando.txt").readlines()

lex.lex() # Build the lexer
for i in leerArchivo():
    print(i)
for i in leerArchivo():
    lex.input(i)
    while True:
        tok = lex.token()
        if not tok: break
        print (str(tok.value) + " - " + str(tok.type))
