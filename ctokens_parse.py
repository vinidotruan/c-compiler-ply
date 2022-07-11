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
				| while
				| for
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

def p_while(p):
	'''
	while : WHILE comparison command
	'''
	p[0] = p[1]+p[2]+p[3]

def p_for(p):
	'''
	for : FOR condition_for
	'''
	p[0] = p[1]+p[2]

def p_case(p):
	'''
	case : CASE DPOINT command_case
	'''
	p[0] = p[1]+p[2]+str(p[3])

def p_condition_for(p):
	'''
	condition_for : LPAR identifier final_line_identifier comparison_without_par final_line_identifier identifier PLUS PLUS RPAR command
				  | LPAR identifier final_line_identifier comparison_without_par final_line_identifier identifier MINUS MINUS RPAR command
	'''
	p[0] = f'{p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]+p[8]+p[9]+p[10]}'

def p_command(p):
	'''
	command : LCBRACKET NUMBER MINUS NUMBER final_line_identifier RCBRACKET
			| LCBRACKET NUMBER PLUS NUMBER final_line_identifier RCBRACKET
			| LCBRACKET NUMBER TIMES NUMBER final_line_identifier RCBRACKET
			| LCBRACKET NUMBER DIVIDE NUMBER final_line_identifier RCBRACKET
	'''
	p[0] = f'{p[1]+p[2]+p[3]+p[4]+p[5]+p[6]}'

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
	p[0] = f'{p[1]+p[2]+p[3]+p[4]+p[5]}'
def p_comparison_without_par(p):
	'''
	comparison_without_par : NUMBER GTH NUMBER
				| NUMBER LTH NUMBER
                | NUMBER GTHOREQUAL NUMBER
                | NUMBER LTHOREQUAL NUMBER
                | NUMBER EQUALEQUAL NUMBER
                | NUMBER NOTEQUAL NUMBER

				| identifier GTH NUMBER
				| identifier LTH NUMBER
                | identifier GTHOREQUAL NUMBER
                | identifier LTHOREQUAL NUMBER
                | identifier EQUALEQUAL NUMBER
                | identifier NOTEQUAL NUMBER

				| NUMBER GTH identifier
				| NUMBER LTH identifier
                | NUMBER GTHOREQUAL identifier
                | NUMBER LTHOREQUAL identifier
                | NUMBER EQUALEQUAL identifier
                | NUMBER NOTEQUAL identifier

				| identifier GTH identifier
				| identifier LTH identifier
                | identifier GTHOREQUAL identifier
                | identifier LTHOREQUAL identifier
                | identifier EQUALEQUAL identifier
                | identifier NOTEQUAL identifier
	'''
	p[0] = f'{p[1]+p[2]+p[3]}'

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
