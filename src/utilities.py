import re

def parsePrograms(input_):
    eop_count = input_.count('$')
    programs = tuple(input_.split('$'))
    program_count = len(programs)

    if eop_count is 0 or eop_count != program_count:
        print("Warning: Missing EOP '$'")

    return programs

def findMatches(string_,valid_tokens):
    for token in valid_tokens:
        pattern = ''.join(valid_tokens[token][0])

        match = re.match(pattern,string_)

        if match is not None:
            print('match',token,repr(match.group(0)))

# Switches the regex for chars when dealing with string to include whitespace
def switchCharRegex(valid_tokens):
    char_regex = r'^[a-z]'

    # Chars including whitespace when lexing chars inside string
    char_space_regex = r'^[a-z]|\s$'


    if valid_tokens['T_char'][0] is char_regex:
        valid_tokens['T_char'] = (char_space_regex, 5)
    else:
        valid_tokens['T_char'] = (char_regex, 5)

