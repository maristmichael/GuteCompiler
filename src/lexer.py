LEXEMES = {
    # Primitives
    'CHAR' : r'[a-z]',
    'DIGIT' : r'[0-9]',
    'SPACE' : r'\s',
        
    # Keywords
    'T_if':r'if',
    'T_while':r'while',
    'T_print':r'print',
    'T_type':r'int|string|boolean',
    'T_bool':r'true|false',

    # Symbols
    'T_quote':r'"',
    'T_intop_add':r'\+',
    'T_assign':r'=',
    'T_boolop':r'==|!=',
    'T_LBrace':r'{',
    'T_RBrace':r'}',
    'T_LParen':r'\(',
    'T_RParen':r'\)',
}