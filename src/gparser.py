from treelib import Node, Tree
from tokens import tokenKinds
from utilities import STDERR,STDOUT,STDWARN


def guteParse(token_stream, program_num):
    token_kinds = tokenKinds()
    cst = Tree()
    curr_node = cst.create_node('Root')
    curr_token = 0

    def parseProgram(program_num):
        nonlocal cst, curr_node
        curr_node = cst.create_node(f'Program {program_num}', parent=curr_node.identifier)
        parseBlock()
        matchConsume('T_eof')
        endChildren()


    def parseBlock():
        nonlocal cst, curr_node

        print('Block')
        curr_node = cst.create_node('Block', parent=curr_node.identifier)
        # print(cst.parent(curr_node.identifier))
        matchConsume('T_l_brace') 
        parseStatementList()
        matchConsume('T_r_brace')
        endChildren()


    def parseStatementList():
        nonlocal cst, curr_node
        print('Statement List')

        curr_node = cst.create_node('Statement List', parent=curr_node.identifier)

        if token_stream[curr_token].type_ in ('T_k_if', 'T_k_while', 'T_k_print', 'T_id', 'T_k_int', 'T_k_boolean', 'T_k_string', 'T_l_brace'):
            parseStatement()

        endChildren()

        if token_stream[curr_token].type_ in ('T_k_if', 'T_k_while', 'T_k_print', 'T_id', 'T_k_int', 'T_k_boolean', 'T_k_string', 'T_l_brace'):
            parseStatementList()
        else:
            print('empty production')


    def parseStatement():
        nonlocal cst, curr_node
        print('Statement')

        curr_node = cst.create_node('Statement', parent=curr_node.identifier)

        if token_stream[curr_token].type_ == 'T_k_print':
            parsePrint()

        elif token_stream[curr_token].type_ == 'T_k_id':
            parseAssignment()
        
        elif token_stream[curr_token].type_ in ('T_k_int', 'T_k_boolean', 'T_k_string'):
            parseVarDecl()
        
        elif token_stream[curr_token].type_ == 'T_k_while':
            parseWhile()

        elif token_stream[curr_token].type_ == 'T_k_if':
            parseIf()
        elif token_stream[curr_token].type_ == 'T_l_brace':
            parseBlock()

        endChildren()

    def parsePrint():
        nonlocal cst, curr_node
        print('Print Statement')

        curr_node = cst.create_node('Print Statement', parent=curr_node.identifier)
        matchConsume('T_k_print')
        matchConsume('T_l_brace')
        parseExpr()
        matchConsume('T_r_brace')
        endChildren()



    def parseAssignment():
        nonlocal cst, curr_node
        print('Assignment Statement')

        curr_node = cst.create_node('Assignment Statement', parent=curr_node.identifier)
        matchConsume('T_id')
        matchConsume('T_assign')
        parseExpr()
        endChildren()


    def parseVarDecl():
        nonlocal cst, curr_node
        print('Variable Decleration')

        curr_node = cst.create_node('Variable Decleration', parent=curr_node.identifier)
        if token_stream[curr_token].type_ in ('T_k_int', 'T_k_boolean', 'T_k_string'):
            parseType()
        else:
            print('var decl error')

        if token_stream[curr_token].type_ in ('T_id'):
            parseID()
        else:
            print('var decl error')

        endChildren()


    def parseWhile():
        nonlocal cst, curr_node
        print('While Statement')

        curr_node = cst.create_node('While Statement', parent=curr_node.identifier)
        matchConsume('T_k_while')
        parseBooleanExpr()
        parseBlock()
        endChildren()


    def parseIf():
        nonlocal cst, curr_node
        print('If Statement')

        curr_node = cst.create_node('If Statement', parent=curr_node.identifier)
        matchConsume('T_k_if')

        parseBooleanExpr()
        parseBlock()
        endChildren()


    def parseExpr():
        nonlocal cst, curr_node
        print('Expression')

        curr_node = cst.create_node('Expr', parent=curr_node.identifier)
        if token_stream[curr_token].type_ == 'T_digit':
            parseIntExpr()
        elif token_stream[curr_token].type_ == 'T_l_paren':
            parseBooleanExpr()
        elif token_stream[curr_token].type_ == 'T_k_true' or token_stream[curr_token].type_ == 'T_k_false':
            parseBooleanExpr()
        elif token_stream[curr_token].type_ == 'T_quote':
            parseStringExpr()
        elif token_stream[curr_token].type_ == 'T_id':
            parseID()
        else:
            pass
            # print('bad')

        endChildren()


    def parseIntExpr():
        nonlocal cst, curr_node
        print('Int Expression')

        curr_node = cst.create_node('Int Expr', parent=curr_node.identifier)
        if matchConsume('T_digit') and matchConsume('T_intop_add'):
            parseDigit()
            parseIntOp()
            parseExpr()

        elif matchConsume('T_digit'):
            parseDigit()

        endChildren()

    def parseStringExpr():
        nonlocal cst, curr_node
        print('String Expression')

        curr_node = cst.create_node('String Expr', parent=curr_node.identifier)
        matchConsume('T_quote')
        parseCharList()
        matchConsume('T_quote')
        endChildren()

    def parseBooleanExpr():
        nonlocal cst, curr_node
        print('Boolean Expression')

        curr_node = cst.create_node('Boolean Expr', parent=curr_node.identifier)
        if matchConsume('T_l_paren'):
            parseExpr()
            parseBoolOp()
            parseExpr()
            matchConsume('T_r_paren')

        elif matchConsume('T_k_true') or matchConsume('T_k_false'):
            parseBoolVal()

        endChildren()

    def parseID():
        nonlocal cst, curr_node,token_stream,curr_token
        print(f'ID')

        curr_node = cst.create_node('ID', parent=curr_node.identifier)
        matchConsume('T_id')
        endChildren()

    def parseCharList():
        nonlocal cst, curr_node
        print('Char List')

        curr_node = cst.create_node('Char List', parent=curr_node.identifier)

        if token_stream[curr_token].type_ == 'T_char':
            parseChar()
        else:
            pass
            # print('bad char list')
        endChildren()

    def parseType():
        if matchConsume('T_k_int'):
            print(f'int')
            return True
        if matchConsume('T_k_string'):
            print('string')

            return True
        if matchConsume('T_k_boolean'):
            print('boolean')

            return True
        else:
            pass
            # print('bad type parse')

    def parseChar():
        print(f'T_char')
        if matchConsume('T_char'):
            parseCharList()
        else:
            pass
            print('BAD char')


    def parseDigit():
        if matchConsume('T_digit'):
            pass
        else:
            pass
            print('bad digit parse')

    def parseBoolOp():
        if matchConsume('T_boolop_eq') or matchConsume('T_boolop_ineq'):
            pass
        else:
            pass
            print('bad bool op parse')

    def parseBoolVal():
        if matchConsume('T_k_true') or matchConsume('T_k_false'):
            pass
        else:
            pass
            print('bad bool val parse')

    def parseIntOp():
        if matchConsume('T_intop_add'):
            pass
        else:
            pass
            print('bad intop parse')

    def matchConsume(to_match):
        nonlocal cst, curr_token, token_kinds, token_stream, curr_node
        # print('trying to match', to_match)

        if token_stream[curr_token].type_ == to_match and to_match in token_kinds:
            print(token_stream[curr_token])
            cst.create_node(f'{token_stream[curr_token]}', parent=curr_node.identifier)
            curr_token += 1

        else: 
            pass
            # print('nah')

    def endChildren():
        nonlocal curr_node

        if cst.get_node(curr_node.bpointer):
            curr_node = cst.parent(curr_node.identifier)

    # def 

    parseProgram(program_num)
    return cst
