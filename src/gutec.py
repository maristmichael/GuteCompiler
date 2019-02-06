import lexer

def main():
    f = open('dumb.txt', 'r')
    input_ = f.read()
    f.close()

    input_ = [char for char in input_]
    print(input_)
    
    # for char in input_:
        # lexer.lex(char)

    
if __name__ == '__main__':
    main()
    