import ply.lex as lex

reserved = {
	'float' : 'FLOAT',
	'char' : 'CHAR',
	'int' : 'INT',
}
tokens = list(reserved.values())+['ID','TYPEID', 'COMMA', 'SEMI', 'NUMBER', 'LBRACKET', 'RBRACKET',]

t_COMMA = '\,'
t_SEMI = '\;'
t_LBRACKET = '\['
t_RBRACKET = '\]'

def t_ID(t):
	r'[A-Za-z_][A-Za-z0-9_]*'
	t.type = reserved.get(t.value, 'ID')
	return t

def t_NUMBER(t):
    r'\d+'
    return t

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()