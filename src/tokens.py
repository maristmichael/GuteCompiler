class Token():
    def __init__(self,type_,value,start,end):
        self.type_ = type_
        self.value = value
        self.start_position = start
        self.end_position = end

def token_kinds():
    # Token type = {regex:priority}
    return {
        'T_keyword' : {r'^if|while|print|int|string|boolean|true|false$' : 1},

        # Identifiers are 1 character long
        'T_ID' : {r'^[a-z]$': 2},

        # Valid Symbols: " + = == != { } ( )
        'T_symbol' : {r'^"|\+|=|==|!=|{|}|\(|\)$': 3},

        # Digits are of length 1
        'T_digit' : {r'^[0-9]$' : 4},

        # Chars are of length 1
        'T_char' : {
            r'^[a-z]$': 5,
            # Chars including whitespace if lexing chars inside string
            r'^[a-z]|\s$': 5
        }
    }
