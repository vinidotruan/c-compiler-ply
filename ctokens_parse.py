import ply.yacc as yacc

from ctokens import tokens
from ctokens import lexer

# int teste;
# [INTEGER] [teste] [;]

def p_declaration(p):
	'''
	declaration : token identifier_list final_line_identifier
	'''
	
	p[0] = p[1]+' '+p[2]+p[3]

def p_identifier_list(p):
	'''
	identifier_list : identifier
					| char_array
					| identifier_list COMMA identifier
					| identifier_list COMMA char_array
	'''
	if len(p) == 2:
		p[0] = p[1]
	else:
		for x in p:
			if x != None:
				p[0] = p[1]+','+x

def p_char_array(p):
	'char_array : identifier array_identifier'
	p[0] = p[1]+p[2]

def p_array_identifier(p):
	'''
	array_identifier : LBRACKET NUMBER RBRACKET
	'''
	p[0] = p[1]+p[2]+p[3]

def p_identifier(p):
	'''
	identifier : ID
	'''
	p[0] = p[1]

def p_token(p):
	'''
	token : TYPEID
		| FLOAT
		| INT
		| CHAR
	'''
	p[0] = p[1]

def p_semi(p):
	'final_line_identifier : SEMI'
	p[0] = p[1]

def p_error(p):
	print('Digitou algo errado!', p)

parser = yacc.yacc()


while True:
	try:
		s = input('digite: ')
	except EOFError:
		break
	if not s: continue
	result = parser.parse(s, debug=False)
	print(result)
