class Token():
    def __init__(self,type_,value,line_num,col_num):
        self.type_ = type_
        self.value = value
        self.line_num = line_num
        self.col_num = col_num

def token_kinds():
    # { kind : (regex,priority) }
    return {
        'T_keyword' : (r'^if|while|print|int|string|boolean|true|false$', 1),

        # Identifiers are 1 character long
        'T_ID' : (r'^[a-z]$', 2),

        # Valid Symbols: " + = == != { } ( )
        'T_symbol': (r'^[\"\+{}\(\)](?![\s\S])|(=){1,2}(?![\s\S])|(!=)(?![\s\S])$$', 3),

        # Digits are of length 1
        'T_digit' : (r'^[0-9]$', 4),

        # Chars are of length 1
        'T_char' : ( r'^[a-z]$', 5)
    }
