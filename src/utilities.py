import re

def parsePrograms(input_):
    eop_count = input_.count('$')
    programs = input_.split('$')
    program_count = len(programs)

    if eop_count is 0 or eop_count != program_count:
        print("Warning: Missing EOP '$'")

    return programs

def findMatches(string_,valid_tokens):
    for token in valid_tokens:
        pattern = ''.join(valid_tokens[token].keys())

        match = re.match(pattern,string_)

        if match is not None:
            print(token,repr(match.group(0)))
