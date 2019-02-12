# import re
from tokens import token_kinds
from utilities import *


# Takes in a string input and returns 
def lex(input_):
    valid_tokens = token_kinds()


    LEXEMES = {
        # Keywords
        'while': 'T_K_while',
        'print': 'T_K_print',
        'int': 'T_K_int',
        'if': 'T_K_if',
        'string': 'T_K_string',
        'boolean': 'T_K_boolean',
        'true': 'T_K_true',
        'false': 'T_K_false',

        # Symbols
        '"': 'T_quote',
        '+': 'T_intop_add',
        '=': 'T_assign',
        '==': 'T_boolop_eq',
        '!=': 'T_boolop_ineq',
        '{': 'T_LBrace',
        '}': 'T_RBrace',
        '(': 'T_LParen',
        ')': 'T_RParen',
        '$': 'T_EOF'
    }

    VALID_SYMBOLS = tuple(LEXEMES.keys())[7::]

    tokens = []
    line,col = 1,1
    programs = parsePrograms(input_)



    for i, pgm in enumerate(programs):
        characters = [*pgm]
        matches = []
        last_match_len = 0
        last_match_idx = -1
        buffer = []

        if len(programs) > 1:
            print(f'Program:{i+1}')


        # for char in characters:
        while buffer or characters:
            next_char = next(iter(characters), None)
            print('next char is....',repr(next_char))

            # Look ahead and ignore white space if we are not in a string
            if charRegex(valid_tokens) and next_char == ' ':
                col += 1
                del characters[0]
                continue

            if next_char == '\n':
                line += 1
                col = 0
                del characters[0]
                continue

            if next_char in VALID_SYMBOLS and buffer or not characters:
                print(buffer)
                tokens.append(consumeToken(matches, LEXEMES,valid_tokens))
                print('-----added new token, current:', tokens)
                del_upto = len(tokens[-1].value)
                print(buffer[0:del_upto])
                # print(valid_tokens, '########')
                if buffer[0:del_upto][0] == '"':
                    valid_tokens = switchCharRegex(valid_tokens)
                    # print(valid_tokens)
                del buffer[0:del_upto]
                characters = buffer + characters
                buffer = []
                print('-----Consuming a token & clearing buffer')
                # print(tokens)
                matches = []

            if characters:
                col += 1
                buffer.append(characters.pop(0))

            



            buffer_string = ''.join(buffer)
            findMatches(buffer_string, valid_tokens, matches,line,col)
            if matches:
                last_matched = matches[-1:][0]
                last_match_len = len(matches)

            if last_matched[0] == 'T_symbol' and characters:
                print('looking ahead for double symbol')
                print(repr(buffer_string+characters[0]))
                findMatches(buffer_string+characters[0],valid_tokens, matches,line,col)
                if last_match_len != len(matches):
                    if last_matched == matches[-1:][0]:
                        print('same symbol curr,',matches)
                        matches.remove(matches[-1:][0])
                        print('after', matches)
                    print('diff symbol, curr',matches)
                    matches.remove(matches[-2:][0])
                    print(buffer)
                    buffer.append(characters.pop(0))
                    col += 1
                    print('after', matches)
