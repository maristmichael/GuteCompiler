# import lexer
from lexer import guteLex
from gparser import guteParse
import time
from utilities import STDWARN,STDOUT,STDERR,dividePrograms


def main(filepath):
    start_time = time.time()
    try:
        # Open the file and read all its content
        with open(filepath, 'r') as f:
            input_ = f.read()
    except Exception as e:
            error = f'File Error: {e}'
            error = error.replace('[Errno 2] ','')
            error = error.replace(' or directory', '')
            STDERR(error)
            exit()

    # Split the programs up by EOP
    programs = dividePrograms(input_)

    # print(programs)
    # programs = ['{int a = 2}$']
    # print(programs)
    [guteCompile(i, program) for i, program in enumerate(programs)]
    # lexer(programs)

    STDWARN('------------------------------------')
    STDOUT(f'Sucessfully lexed & parsed {filepath}')
    STDWARN(f'--- {time.time() - start_time} seconds ---')

def guteCompile(i,program):
    STDWARN(f'------PROGRAM {i+1}------')
    STDOUT(f'LEXER:')
    tokens = guteLex(program)
#     [print(f'{token.type_}......line {token.line_num}') for token in tokens]
    STDOUT(f'LEXED PROGRAM SUCCESSFULLY\n')
    STDOUT(f'PARSER:')


    cst = guteParse(tokens, i)
#     cst.DEPTH.show()
    STDWARN('CST:')


    print(cst)
#     [print(f'{cst.level(cst.get_node(i))}') for i in cst.expand_tree()]

#     [print(f'{cst.level(cst.get_node(i))-1*"  "}{cst.get_node(i).tag}') for i in cst.expand_tree()]

if __name__ == '__main__':
    main()
    
