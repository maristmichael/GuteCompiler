import re
from tokens import *
def parsePrograms(input_):
    eop_count = input_.count('$')
    programs = input_.split('$')
    programs = tuple(filter(None, programs))
    program_count = len(programs)

    if eop_count is 0 or eop_count != program_count:
        print("Warning: Missing EOP '$'")

    return programs

def findMatches(string_,valid_tokens,matches,line,col,idx):
    print('matching:', repr(string_))
    # print(matches)
    for token in valid_tokens:
        pattern = ''.join(valid_tokens[token][0])

        match = re.match(pattern,string_)

        if match is not None:
            idx += 1
            matches.append((token,match.group(0),line,col))
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
     
def consumeToken(matches,lexemes):
    matches_literals = [x[1] for x in matches]
    match_lengths = [len(x) for x in matches_literals]
    longest_match_i = match_lengths.index(max(match_lengths))
    longest_match = matches_literals[longest_match_i]

    # print(matches_literals, match_lengths, longest_match_i, longest_match)
    # print(matches_literals.count(str(longest_match)))
    if matches_literals.count(str(longest_match)) == 1:
        if matches[longest_match_i][0] == 'T_symbol' or matches[longest_match_i][0] == 'T_keyword':
            return Token(lexemes[longest_match], longest_match, matches[longest_match_i][2], matches[longest_match_i][3])
