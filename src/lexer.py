# import re
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

    tokens = []
    line_number = 1
    programs = parsePrograms(input_)

    for i, pgm in enumerate(programs):
        if len(programs) > 1:
            print(f'Program:{i+1}')
        # print(f'    {repr(pgm)}')
        characters = [char for char in pgm]
        scope = []
        buffer = []

        # Loop as long as we have characters or the buffer is not empty
        while buffer or characters:
            if characters:
                buffer.append(characters.pop(0))

            findMatches(buffer,VALID_TOKENS)

