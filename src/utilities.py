import re
from tokens import *
def parsePrograms(input_):
    eop_count = input_.count('$')
    programs = re.split('($)',input_)
    programs = tuple(filter(None, programs))
    program_count = len(programs)

    if eop_count is 0 or eop_count != program_count:
        print("Warning: Missing EOP '$'")

    return programs

def findMatches(string_,valid_tokens,matches,line,col):
    # print(matches)
    for token in valid_tokens:
        pattern = ''.join(valid_tokens[token][0])

        match = re.match(pattern,string_)

        if match is not None:
            print('matched:', repr(string_), token)
            matches.append((token,match.group(0),line,col))
            print('all matches:',matches)


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
    match_kinds = [x[0] for x in matches]
    match_literals = [x[1] for x in matches]
    match_lengths = [len(x) for x in match_literals]

    print(match_kinds,match_literals,match_lengths)
    match_priorities = [token_kinds()[x[0]][1] for x in matches]



    longest_match_i = match_lengths.index(max(match_lengths))
    longest_match = match_literals[longest_match_i]
    print('longest m:', longest_match)
    print('literals:', match_literals)


    # If there's only one longest match
    if match_literals.count(str(longest_match)) == 1:
        if matches[longest_match_i][0] == 'T_symbol' or matches[longest_match_i][0] == 'T_keyword':
            return Token(lexemes[longest_match], longest_match, matches[longest_match_i][2], matches[longest_match_i][3])
        else:
            return Token(match_kinds[0], longest_match, matches[longest_match_i][2], matches[longest_match_i][3])


        # else:
        #     print('\\\\\\\\\\\\\\\\',longest_match, longest_match_i)
            # return Token(lexemes[longest_match], longest_match, matches[longest_match_i][2], matches[longest_match_i][3])
    else:
        highest_priority_i = match_priorities.index(min(match_priorities))
        highest_priority = match_literals[highest_priority_i]
        print('returning highest priority is ', matches[highest_priority_i], highest_priority)

        return Token(matches[highest_priority_i][0], highest_priority, matches[highest_priority_i][2], matches[highest_priority_i][3])
        
        # We have to get the highest priority match

