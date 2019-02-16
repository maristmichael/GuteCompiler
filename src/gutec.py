import lexer
import time
from utilities import STDWARN,STDOUT


def main(filepath):
    start_time = time.time()
    # Open the file and read all its content
    f = open(filepath, 'r')
    input_ = f.read()
    f.close()


    # Give the lexer the input
    lexer.lex(input_)
    message = f'Sucessfully lexed {filepath}'
    STDWARN("------------------------------------")
    STDOUT(message)
    STDWARN("--- %s seconds ---" % (time.time() - start_time))
    
if __name__ == '__main__':
    main()
    
