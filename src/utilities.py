import re
from tokens import *
from lexer import *
import click

# Given an input string of programs, split it by the eof symbol ($) and return them as a list
def parsePrograms(input_):
    input_ = input_.rstrip()
    eop_count = input_.count('$')
    programs = input_.split('$')

    # Add back the eof character after the splt
    for i in range(eop_count):
        programs[i] += '$'

    # Filter out any empty strings
    programs = tuple(filter(None, programs))

    # if our program count doesn't match the count of eop's in the input, or the eop count is 0 then we are missing a trailing eop
    program_count = len(programs)
    if eop_count is 0 or eop_count != program_count:
        STDWARN("Warning: Missing EOP '$'")

    return programs

# Given a string of chars and a set of valid tokens find and return the kinds of tokens the string matches
def findMatches(char_string,valid_tokens,matches,line,col):
    # Search through token kinds to find a pattern match
    for token in valid_tokens:
        pattern = ''.join(valid_tokens[token][0])

        match = re.match(pattern, char_string)

        if match is not None:
            matches.append((token,match.group(0),line,col))

# Switches the regex for char tokens to now find whitespaces, and increase the priority for chars given our list of token kinds
def switchCharRegex(valid_tokens):
    char_regex = r'^[a-z]$'

    # Chars tokens including whitespace when lexing chars inside string
    char_space_regex = r'^[a-z ]$'

    if valid_tokens['T_char'][0] == char_regex:
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

# Check if the char token regex is not including whitespaces
def charRegex(valid_tokens):
    char_regex = r'^[a-z]$'
    return valid_tokens['T_char'][0] == char_regex
     

# Given a list of token kind matches lexeme that will get us the longest match or the highest priority match
def generateToken(matches,lexemes,valid_tokens):
    match_kinds = [match[0] for match in matches]
    match_literals = [match[1] for match in matches]
    match_lengths = [len(match) for match in match_literals]

    match_priorities = [valid_tokens[kind][1] for kind in match_kinds]

    longest_match_i = match_lengths.index(max(match_lengths))
    longest_match = match_literals[longest_match_i]

    # If there's only one longest match
    if match_literals.count(str(longest_match)) == 1:

        # Create the appropiate Token
        if matches[longest_match_i][0] == 'T_symbol' or matches[longest_match_i][0] == 'T_keyword':
            return Token(lexemes[longest_match], longest_match, matches[longest_match_i][2], matches[longest_match_i][3])
        else:
            return Token(match_kinds[0], longest_match, matches[longest_match_i][2], matches[longest_match_i][3])

    else:
        # Find the highest priority match
        highest_priority_i = match_priorities.index(min(match_priorities))
        highest_priority = match_literals[highest_priority_i]
        return Token(matches[highest_priority_i][0], highest_priority, matches[highest_priority_i][2], matches[highest_priority_i][3])

# Functions to print to the command line with pretty colors
def STDOUT(message):
    click.echo(click.style(message, fg='green'))

def STDERR(message):
    click.echo(click.style(message, fg='red'))

def STDWARN(message):
    click.echo(click.style(message, fg='yellow'))
