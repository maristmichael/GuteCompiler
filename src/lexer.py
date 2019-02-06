import re

VALID_SYMBOLS = {   
    '"':'T_quote',
    '+':'T_intop_add',
    '=':'T_assign',
    '==':'T_boolop_eq',
    '!=':'T_boolop_ineq',
    '{':'T_LBrace',
    '}':'T_RBrace',
    '(':'T_LParen',
    ')':'T_RParen'
}

VALID_KEYWORDS = {
    'while':'T_K_while',
    'print':'T_K_print',
    'int':'T_K_int',
    'string':'T_K_string',
    'boolean':'T_K_boolean',
    'true':'T_K_true',
    'false':'T_K_false'
}

LEXEMES = {

    # Format = name: {regex:priority}
    'T_keyword':{r'^if|while|print|int|string|boolean|true|false$' : 1},

    # Identifiers are 1 character long
    'T_ID': {r'^[a-z]$': 2},

    # Valid Symbols: " + = == != { } ( )
    'T_symbol' : {r'^"|\+|=|==|!=|{|}|\(|\)$': 3},

    # Digits are of length 1
    'T_digit' : {r'^[0-9]$' : 4},

    # Chars are of length 1
    'T_char' : {r'^[a-z]$': 5},

    # Chars including whitespace if dealing with string expressions | Can Space be a CHAR????
    'T_char_space' : {r'^[a-z]|\s$': 5},

}

def lex(input_):
    for lexeme in LEXEMES:
        match = re.match(LEXEMES[lexeme],input_)
        if match:
            print(match)
