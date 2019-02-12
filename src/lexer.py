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
        ignore_mode = False
        characters = [*pgm]
        matches = []
        last_match_len = 0
        last_match_idx = -1
        buffer = []

        if len(programs) > 1:
            print(f'Program:{i+1}')


        # for char in characters:
        while buffer or characters:
            if characters:
                next_char = characters[0] if 0 < len(characters) else None
                next_two_chars = ''.join(characters[0:2]) if 2 < len(characters) else None
                buffer_str = ''.join(buffer)
                # print('next char: ', repr(next_char))

                if next_two_chars == '/*' or next_two_chars == '*/':
                    del characters[0:2]
                    print('comments......')
                    ignore_mode = not ignore_mode
                    continue

                elif ignore_mode and characters:
                    col += 1
                    print('skipping......', characters[0])
                    del characters[0]
                    continue
                # Look ahead and ignore white space if we are not in a string
                elif charRegex(valid_tokens) and next_char == ' ':
                    col += 1
                    del characters[0]
                    continue
                    # continue

                elif next_char == '\n':
                    line += 1
                    col = 0
                    del characters[0]
                    continue

                elif next_char in VALID_SYMBOLS or  next_two_chars in VALID_SYMBOLS or len(characters) is 0:
                    if not buffer:
                        buffer.append(characters.pop(0))
                        next_char = characters[0] if 0 < len(characters) else None
                        next_two_chars = ''.join(characters[0:2]) if 2 < len(characters) else None
                        buffer_str = ''.join(buffer)

                        findMatches(buffer_str, valid_tokens,matches, line, col)
                        last_matched = matches[-1:][0] if 0 < len(matches) else None

                        # last_matched = matches[-1:][0]
                        last_match_len = len(matches)

                        

                        if next_char and (buffer_str+next_char) in VALID_SYMBOLS:
                            print('looking ahead for double symbol')
                            print(repr(buffer_str+next_char))
                            findMatches(buffer_str+next_char,valid_tokens, matches, line, col)
                            if last_match_len is 0:
                                 buffer.append(characters.pop(0))
                            elif last_match_len != len(matches):
                                if last_matched == matches[-1:][0]:
                                    print('same symbol curr,', matches)
                                    matches.remove(matches[-1:][0])
                                    print('after', matches)
                                print('diff symbol, curr', matches)
                                matches.remove(matches[-2:][0])
                                print(buffer)
                                buffer.append(characters.pop(0))
                                col += 1
                                print('after', matches)
                        continue
                    else:
                        print('-----stopping at:', next_char)
                        print('-----buffer:', buffer)

                        tokens.append(consumeToken(matches, LEXEMES, valid_tokens))
                        indexes_to_del = len(tokens[-1].value)

                      

                        print('~~~~~~~~~~~~~`!!!!!!!!!!deleting:', buffer[0:indexes_to_del])

                        if buffer[0:indexes_to_del][0] == '"':
                            print('switching chars')
                            valid_tokens = switchCharRegex(valid_tokens)
                        del buffer[0:indexes_to_del]
                        characters = buffer + characters
                        print("{{{remaining chars: ", characters)
                        buffer = []
                        matches = []

                        print('-----Made a token & clearing buffer')
                        print('-----tokens:', tokens)
                        print('-------------------------------------')
                        continue
        

                    # continue


                next_char = characters[0] if 0 < len(characters) else None
                # print('Popping to buffer, next char: ', repr(next_char))
                # print('Chars left: ', repr(characters))
                buffer.append(characters.pop(0))
                buffer_str = ''.join(buffer)
                # next_two_chars = ''.join(characters[0:2]) if 2 < len(characters) else None

                
                    # print(valid_tokens)
                findMatches(buffer_str, valid_tokens, matches, line, col)
                if matches:
                    last_matched = matches[-1:][0]
                    last_match_len = len(matches)
                
            else:
                # print('no chars')
                if not matches and buffer:
                    print('error, invalid token')
                    break
                # print(matches,buffer)
                tokens.append(consumeToken(matches, LEXEMES, valid_tokens))
                indexes_to_del = len(tokens[-1].value)

                

                # print('!!!!!!!!!!deleting:', buffer[0:indexes_to_del])

                if buffer[0:indexes_to_del] == '"':
                    valid_tokens = switchCharRegex(valid_tokens)

                del buffer[0:indexes_to_del]
                characters = buffer + characters
                # print("{{{remaining chars: ", characters)
                buffer = []
                matches = []

                # print('-----Made a token & clearing buffer')
                # print('-----tokens:', tokens)
                # print('-------------------------------------')
                # print(characters,matches)
