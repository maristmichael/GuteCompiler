import re
from tokens import *
from utilities import *

VALID_TOKENS = token_kinds()

LEXEMES = {  
    # Keywords
    'while':'T_K_while',
    'print':'T_K_print',
    'int':'T_K_int',
    'string':'T_K_string',
    'boolean':'T_K_boolean',
    'true':'T_K_true',
    'false':'T_K_false',

    # Symbols
    '"':'T_quote',
    '+':'T_intop_add',
    '=':'T_assign',
    '==':'T_boolop_eq',
    '!=':'T_boolop_ineq',
    '{':'T_LBrace',
    '}':'T_RBrace',
    '(':'T_LParen',
    ')':'T_RParen',
}

# Takes in a string input and returns 
def lex(input_):
    programs = parsePrograms(input_)

    # input_ = [char for char in input_]

    # for token in VALID_TOKENS:
    #     pattern = ''.join(VALID_TOKENS[token].keys())

    #     match = re.match(pattern,input_)

    #     if match is not None:
    #         print(token,repr(match.group(0)))
    print(programs)