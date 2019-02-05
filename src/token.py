class Token():
    def __init__(self,type_,value,start,end):
        self.type_ = type_
        self.value = value
        self.start_position = start
        self.end_position = end
