import re

def parsePrograms(input_):
    eop_count = input_.count('$')
    programs = input_.split('$')
    programs = tuple(filter(None, programs))
    program_count = len(programs)

    if eop_count is 0 or eop_count != program_count:
        print("Warning: Missing EOP '$'")

    return programs

def findMatches(string_,valid_tokens,matches):
    print('matching:', repr(string_))
    print(matches)
    for token in valid_tokens:
        pattern = ''.join(valid_tokens[token][0])

        match = re.match(pattern,string_)

        if match is not None:
            matches.append((token,match.group(0)))
    print(matches)


# Switches the regex for chars when dealing with string to include whitespace
def switchCharRegex(valid_tokens):
    char_regex = r'^[a-z]$'

    # Chars including whitespace when lexing chars inside string
    char_space_regex = r'^[a-z]|.$'

    if valid_tokens['T_char'][0] == char_regex:
        valid_tokens['T_char'] = (char_space_regex, 5)
    else:
        valid_tokens['T_char'] = (char_regex, 5)

# Check if the char regex is not including whitespaces
def charRegex(valid_tokens):
    char_regex = r'^[a-z]$'
    return valid_tokens['T_char'][0] == char_regex
     
# def consumeToken(matches):
