import ply.yacc as yacc

from ctokens import tokens
from ctokens import lexer

def p_declaration(p):
	'''
	declaration : token identifier_list final_line_identifier
				| if 
				| else
				| switch
				| case
	'''
	if len(p) == 2:
		p[0] = p[1]
	else:
		p[0] = p[1]+str(p[2])+p[3]

def p_if(p):
	'''
	if : IF comparison command final_line_identifier
		| if_withou_else
	'''
	if len(p) == 2:
		p[0] = p[1]
	else:
		p[0] = p[1]+str(p[2])+str(p[3])

def p_if_withou_else(p):
	'''
	if_withou_else : IF comparison command 
	'''
	p[0] = p[1]+str(p[2])+str(p[3]);

def p_if_else(p):
	'''
	else : if_withou_else ELSE command final_line_identifier
	'''
	p[0] = p[1]+p[2]+str(p[3]);

def p_switch(p):
	'''
	switch : SWITCH LPAR identifier RPAR LCBRACKET case RCBRACKET
	'''
	p[0] = p[1]+p[2]+p[3]+p[4]+p[5]+p[6]

def p_case(p):
	'''
	case : CASE DPOINT command_case
	'''
	p[0] = p[1]+p[2]+str(p[3])

def p_command(p):
	'''
	command : LCBRACKET NUMBER MINUS NUMBER final_line_identifier RCBRACKET
			| LCBRACKET NUMBER PLUS NUMBER final_line_identifier RCBRACKET
			| LCBRACKET NUMBER TIMES NUMBER final_line_identifier RCBRACKET
			| LCBRACKET NUMBER DIVIDE NUMBER final_line_identifier RCBRACKET
	'''
	if p[3] == '-':
		p[0] = p[1]+str(p[2]-p[4])+p[5]+p[6]
	elif p[3] == '+':
		p[0] = p[1]+str(p[2]+p[4])+p[5]+p[6]
	elif p[3] == '/':
		p[0] = p[1]+str(int(p[2])/int(p[4]))+p[5]+p[6]
	elif p[3] == '*':
		p[0] = p[1]+str(int(p[2])*int(p[4]))+p[5]+p[6]
	else:
		p_error(p);

def p_command_case(p):
	'''
	command_case : LCBRACKET NUMBER MINUS NUMBER BREAK final_line_identifier RCBRACKET
			| LCBRACKET NUMBER PLUS NUMBER BREAK final_line_identifier RCBRACKET
			| LCBRACKET NUMBER TIMES NUMBER BREAK final_line_identifier RCBRACKET
			| LCBRACKET NUMBER DIVIDE NUMBER BREAK final_line_identifier RCBRACKET
	'''
	p[0] = f'{p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]}'



def p_comparison(p):
	'''
	comparison : LPAR NUMBER GTH NUMBER RPAR
				| LPAR NUMBER LTH NUMBER RPAR
                | LPAR NUMBER GTHOREQUAL NUMBER RPAR
                | LPAR NUMBER LTHOREQUAL NUMBER RPAR
                | LPAR NUMBER EQUALEQUAL NUMBER RPAR
                | LPAR NUMBER NOTEQUAL NUMBER RPAR
	'''
	if p[3] == '>':
		if p[2] > p[4]:
			p[0] = True
		else:
			p[0] = False

	elif p[3] == '<':
		if p[2] > p[4]:
			p[0] = True
		else:
			p[0] = False

	elif p[3] == '>=':
		if p[2] > p[4]:
			p[0] = True
		else:
			p[0] = False

	elif p[3] == '<=':
		if p[2] > p[4]:
			p[0] = True
		else:
			p[0] = False

	elif p[3] == '==':
		if p[2] > p[4]:
			p[0] = True
		else:
			p[0] = False

	elif p[3] == '!=':
		if p[2] > p[4]:
			p[0] = True
		else:
			p[0] = False 


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
	print(f'Digitou algo errado! {p}')


parser = yacc.yacc()

arquivo = open('arquivo_input.txt', 'r')
for data in arquivo:
	try:
		s = data
	except EOFError:
		break
	if not s: continue
	result = parser.parse(s, debug=False)
	print(result)
