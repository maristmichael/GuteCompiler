import sys,time
from treelib import Node
from gutec.glexer import guteLex
from gutec.gparser import guteParse
from gutec.ganalysis import analyze
from gutec.utilities import *


def main():
    start_time = time.time()
    try:
        # Open the file and read all its content
        with open(sys.argv[1], 'r') as f:
            input_ = f.read()
    except Exception as e:
            error = f'File Error: {e}'
            error = error.replace('[Errno 2] ', '')
            error = error.replace(' or directory', '')
            STDERR(error)
            exit()

    # Split the programs up by EOP
    input_ = removeComments(input_)
    programs = dividePrograms(input_)

    [guteCompile(i, program) for i, program in enumerate(programs)]
    # lexer(programs)

    STDWARN(f'--- {time.time() - start_time} seconds ---')


def guteCompile(i, program):
    print('')
    STDWARN(f'------PROGRAM {i+1}------')

    tokens = guteLex(program)
    if not tokens:
        return

    [print(f'{token.type_}......line {token.line_num}') for token in tokens]
    STDOUT(f'LEXED PROGRAM SUCCESSFULLY\n')

    cst, parse_error = guteParse(tokens, i)
    if parse_error:
        return
    STDWARN('CST:')
    printTree(cst)
    STDOUT(f'PARSED PROGRAM SUCCESSFULLY\n')

    cst_nodes = getInorderList(cst, cst.get_node(cst.root), [])
    
    analyze(cst_nodes, i)


if __name__ == '__main__':
    main()
