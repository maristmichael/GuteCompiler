# import re
from tokens import token_kinds
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

VALID_SYMBOLS = tuple(LEXEMES.keys())[7::]

# Takes in a string input and returns 
def lex(input_):
    tokens = []
    line,col = 0,0
    last_match_idx = -1
    programs = parsePrograms(input_)

    for i, pgm in enumerate(programs):
        characters = [char for char in pgm]
        matches = []
        # scope = []
        buffer = []

        if len(programs) > 1:
            print(f'Program:{i+1}')


        # for char in characters:
        while buffer or characters:
            next_char = next(iter(characters), None)
            print('next char is....',repr(next_char))

            # Look ahead and ignore white space if we are not in a string
            if charRegex(VALID_TOKENS) and next_char == " ":
                col += 1
                del characters[0]
                print('deleting space')
                continue

            if next_char == "\n":
                line += 1
                col = 0
                del characters[0]
                print('deleting tab')
                continue

            if next_char in VALID_SYMBOLS and buffer or not characters:
                tokens.append(consumeToken(matches, LEXEMES))
                print('Consuming a token')
                print(tokens)
                matches = []
                buffer = []

            if characters:
                col += 1
                buffer.append(characters.pop(0))

            



            buffer_string = ''.join(buffer)
            findMatches(buffer_string, VALID_TOKENS, matches,line,col,last_match_idx)
          
                # print(matches)

            # print(characters[0:1], VALID_SYMBOLS[2])
            # next_char = next(iter(characters),None)
            # next_char_is_sym = next_char in VALID_SYMBOLS
            # print(repr(next_char), 'is next char')
            # print(next_char_is_sym,'a sym')

            
                
                # matches.append(findMatches(string_, VALID_TOKENS))
                # print(repr(string_), matches)


            if buffer[0:] == '"':
                switchCharRegex(VALID_TOKENS)

            # print(repr(char))
        # print(f'    {repr(pgm)}')
       
        # Loop as long as we have characters or the buffer is not empty



