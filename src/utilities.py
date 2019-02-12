import re
from tokens import *
from lexer import *
import click

def parsePrograms(input_):
    input_ = input_.rstrip()
    eop_count = input_.count('$')
    programs = input_.split('$')

    for i in range(eop_count):
        programs[i] += '$'


    # programs = re.split('$',input_)
    # print(programs)
    programs = tuple(filter(None, programs))
    program_count = len(programs)

    if eop_count is 0 or eop_count != program_count:
        STDWARN("Warning: Missing EOP '$'")

    return programs

def findMatches(string_,valid_tokens,matches,line,col):
    changed = False
    # print('~~~~~~~Analyzing', repr(string_))
    # print(matches)
    for token in valid_tokens:
        pattern = ''.join(valid_tokens[token][0])

        match = re.match(pattern,string_)

        if match is not None:
            changed = True
            # print('matched:', repr(string_), token)
            matches.append((token,match.group(0),line,col))

    
    # if changed:
    #     print('found these',matches)


# Switches the regex for chars to now find whitespaces, and increase the priority for chars
def switchCharRegex(valid_tokens):
    char_regex = r'^[a-z]$'

    # Chars including whitespace when lexing chars inside string
    char_space_regex = r'^[a-z ]$'

    if valid_tokens['T_char'][0] == char_regex:
        # print('swapped')
        valid_tokens = {
            'T_keyword': (r'^(if)(?![\s\S])|(while)(?![\s\S])|(print)(?![\s\S])|(int)(?![\s\S])|(string)(?![\s\S])|(boolean)(?![\s\S])|(true)(?![\s\S])|(false)(?![\s\S])$', 1),
            'T_ID': (r'^[a-z]$', 5),
            'T_symbol': (r'^[\"\+{}\(\)\$](?![\s\S])|(=){1,2}(?![\s\S])|(!=)(?![\s\S])$', 3),
            'T_digit': (r'^[0-9]$', 4),
            'T_char': (char_space_regex, 2),
        }
    else:
        valid_tokens = token_kinds()
    return valid_tokens

# Check if the char regex is not including whitespaces
def charRegex(valid_tokens):
    char_regex = r'^[a-z]$'
    return valid_tokens['T_char'][0] == char_regex
     
def consumeToken(matches,lexemes,valid_tokens):
    match_kinds = [match[0] for match in matches]
    match_literals = [match[1] for match in matches]
    match_lengths = [len(match) for match in match_literals]
    # print(match_kinds, match_literals, match_lengths)
    # print(valid_tokens['T_symbol'][1])

    match_priorities = [valid_tokens[kind][1] for kind in match_kinds]


    # print(match_kinds,match_literals,match_lengths, match_priorities)



    longest_match_i = match_lengths.index(max(match_lengths))
    longest_match = match_literals[longest_match_i]
    # print('longest m:', longest_match)
    # print('literals:', match_literals)


    # If there's only one longest match
    if match_literals.count(str(longest_match)) == 1:
        if matches[longest_match_i][0] == 'T_symbol' or matches[longest_match_i][0] == 'T_keyword':
            return Token(lexemes[longest_match], longest_match, matches[longest_match_i][2], matches[longest_match_i][3])
        else:
            return Token(match_kinds[0], longest_match, matches[longest_match_i][2], matches[longest_match_i][3])

    else:

        highest_priority_i = match_priorities.index(min(match_priorities))
        highest_priority = match_literals[highest_priority_i]
        # print('highest priority indx:', highest_priority_i)
        # print('highest priority:', highest_priority)
        # print('returning highest priority is ', matches[highest_priority_i], highest_priority)

        return Token(matches[highest_priority_i][0], highest_priority, matches[highest_priority_i][2], matches[highest_priority_i][3])
        
        # We have to get the highest priority match

def STDOUT(message):
    click.echo(click.style(message, fg='green'))


def STDERR(message):
    click.echo(click.style(message, fg='red'))


def STDWARN(message):
    click.echo(click.style(message, fg='yellow'))
