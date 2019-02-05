class Token():
    def __init__(self, name, lexeme):
        self.name = name
        self.lexeme = lexeme
        self.start_position = None
        self.end_position = None
        
    