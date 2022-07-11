import ply.lex as lex

reserved = {
	'float' : 'FLOAT',
	'char' : 'CHAR',
	'int' : 'INT',
	'switch': 'SWITCH',
	'while': 'WHILE',
	'for': 'FOR',
	'case': 'CASE',
	'if': 'IF',
	'else': 'ELSE',
	'break': 'BREAK',
}
tokens = list(reserved.values())+[
	'ID', 'TYPEID', 'COMMA', 'SEMI', 'LBRACKET', 'RBRACKET','LCBRACKET', 'RCBRACKET','LPAR',
	'RPAR','PLUS', 'MINUS','TIMES','DIVIDE','NAME','NUMBER',
	'GTH', 'LTH', 'GTHOREQUAL', 'LTHOREQUAL', 'EQUALEQUAL', 'NOTEQUAL', 'DPOINT'
]

t_COMMA = '\,'
t_SEMI = '\;'
t_LBRACKET = '\['
t_LCBRACKET = '\{'
t_RBRACKET = '\]'
t_RCBRACKET = '\}'
t_LPAR = '\('
t_RPAR = '\)'
t_DPOINT = '\:'
t_SWITCH = r'switch'
t_WHILE = r'while'
t_FOR = r'for'
t_CASE = r'case'
t_IF = r'if'
t_ELSE = r'else'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_GTH = r'\>'
t_LTH = r'\<'
t_GTHOREQUAL = r'\>='
t_LTHOREQUAL = r'\<='
t_EQUALEQUAL = r'\=='
t_NOTEQUAL = r'\!='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_ID(t):
	r'[A-Za-z_][A-Za-z0-9_]*'
	t.type = reserved.get(t.value, 'ID')
	return t

def t_NUMBER(t):
    r'\d+'
    return t


t_ignore = " \t"

 
def t_nl(t):
	r'(\n|\r|\r\n)|\s|\t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()