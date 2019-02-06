import re
from tokens import *

VALID_TOKENS = valid_tokens()

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

def lex(input_):
    print
    for token in VALID_TOKENS:
        pattern = ''.join(VALID_TOKENS[token].keys())

        match = re.match(pattern,input_)

        if match is not None:
            print(token,match.group(0))
