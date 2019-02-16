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

    VALID_SYMBOLS = tuple(LEXEMES.keys())[8::]

    tokens = []
    line,col = 1,1
    programs = parsePrograms(input_)

    # Iterate through every program given as input
    for i, pgm in enumerate(programs):
        comment_mode = False
        characters = [*pgm]
        matches = []
        buffer = []
        last_match_len = 0
        # last_match_idx = -1

        # If more than one program make note of it when lexing
        if len(programs) > 1:
            STDOUT(f'Program: {i+1}')

        # As long as we have something in the buffer or characters, try to generate tokens
        while buffer or characters:
            if characters:
                next_char = characters[0] if 0 < len(characters) else None
                next_two_chars = ''.join(characters[0:2]) if 2 < len(characters) else None

                # Concatenate the buffer list to one string to use regex on it
                buffer_str = ''.join(buffer)

                # Toggle comment mode when we detect the apprpiate characters
                if next_two_chars == '/*' or next_two_chars == '*/':
                    del characters[0:2]
                    comment_mode = not comment_mode
                    continue

                # Ignore anything if inside a comment block
                elif comment_mode and characters:
                    col += 1
                    del characters[0]
                    continue

                # Look ahead and ignore whitespace if we are not inside a two quotes (string)
                elif charRegex(valid_tokens) and next_char == ' ':
                    col += 1
                    del characters[0]
                    continue

                # Ignore newlines as characters
                elif next_char == '\n':
                    line += 1
                    col = 0
                    del characters[0]
                    continue


                # If the next 1-2 characters are recognized symbols or we have no characters, try to generate a token
                elif next_char in VALID_SYMBOLS or next_two_chars in VALID_SYMBOLS or len(characters) is 0:
                    # If nothing is in the buffer, try and find a lexeme match for the upcoming symbol
                    if not buffer:
                        # Add the symbol to the buffer
                        buffer.append(characters.pop(0))
                        buffer_str = ''.join(buffer)

                        next_char = characters[0] if 0 < len(characters) else None
                        next_two_chars = ''.join(characters[0:2]) if 2 < len(characters) else None

                        # Find any lexeme matches
                        findMatches(buffer_str, valid_tokens,matches, line, col)

                        last_matched = matches[-1:][0] if 0 < len(matches) else None
                        last_match_len = len(matches)

                        # If the next character is also a symbol, try and see if it could lead to a symbol of size 2 by concatenating it with the symbol we just found
                        if next_char in VALID_SYMBOLS and buffer_str+next_char in VALID_SYMBOLS:
                            findMatches(buffer_str+next_char,valid_tokens, matches, line, col)

                            # If there's no match for a 2 character symbol, add the original one character symbol we found to the buffer
                            if last_match_len is 0:
                                buffer.append(characters.pop(0))

                            # If we found a 2 character symbol, remove the 1 character symbol from our lexeme matches list
                            elif last_match_len != len(matches):
                                matches.remove(matches[-2:][0])
                                buffer.append(characters.pop(0))
                                col += 1

                        # Go back to the top of the loop
                        continue
                    
                    # If there's something in the buffer, lets generate the token from one of our lexeme matches
                    else:

                        # If we dont have any matches or anything in the buffer, we don't have a supported character for our language
                        if not matches and buffer:
                            STDERR('ERROR: invalid token')
                            break

                        # Generate one token given all the matches we found
                        token = generateToken(matches, LEXEMES, valid_tokens)
                        STDOUT(f'LEXER > {token}-[{token.value}] on line {token.line_num}')
                        tokens.append(token)

                        # Keep track of how long our token was to remove its characters from the buffer
                        indexes_to_del = len(tokens[-1].value)

                        # If we are removing a quote, toggle the function to enable/disable whitespace matching for characters
                        if buffer[0:indexes_to_del][0] == '"':
                            valid_tokens = switchCharRegex(valid_tokens)

                        # Purge those indexes wherein the characters of the token are apart of
                        del buffer[0:indexes_to_del]

                        # Prepend whatever's left in the buffer to start this whole process again
                        characters = buffer + characters

                        # Reset our buffer and found matches
                        buffer = []
                        matches = []
                        continue
      

                # If our next character isn't a symbol, take a character and try to find a match
                next_char = characters[0] if 0 < len(characters) else None
                
                buffer.append(characters.pop(0))
                buffer_str = ''.join(buffer)
                
                findMatches(buffer_str, valid_tokens, matches, line, col)

                # Keep track of what we found last, and the length of that match
                if matches:
                    last_matched = matches[-1:][0]
                    last_match_len = len(matches)
                
            # If we have no characters left, try and generate a token
            else:

                # If we dont have any matches or anything in the buffer, we don't have a supported character for our language
                if not matches and buffer:
                    STDERR('ERROR: invalid token')
                    break

                # Generate one token given all the matches we found so far
                token = generateToken(matches, LEXEMES, valid_tokens)
                STDOUT(f'LEXER > {token}-[{token.value}] on line {token.line_num}')
                tokens.append(token)

                # Keep track of how long our token was to remove its characters from the buffer
                indexes_to_del = len(tokens[-1].value)

                # If we are removing a quote, toggle the function to enable/disable whitespace matching for characters
                if buffer[0:indexes_to_del][0] == '"':
                    valid_tokens = switchCharRegex(valid_tokens)

                # Purge those indexes wherein the characters of the token are apart of
                del buffer[0:indexes_to_del]

                
                # Prepend whatever's left in the buffer to start this whole process again
                characters = buffer + characters

                # Reset our buffer and found matches
                buffer = []
                matches = []
