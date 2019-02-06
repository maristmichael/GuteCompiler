import lexer

def main():
    # Open the file and read all its content
    f = open('dumb.txt', 'r')
    input_ = f.read()
    f.close()


    # Give the lexer the input
    lexer.lex(input_)

    
if __name__ == '__main__':
    main()
    