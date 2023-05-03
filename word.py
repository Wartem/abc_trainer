

class Word():
    def __init__(self, str_) -> None:
        self._name = str_
        self._viewable_chars = 0
        
    
    def next_char(self):
        self._viewable_chars += 1
        return self._name[self._viewable_chars]
    
    
    def current_char(self):
        return self._name[self._viewable_chars]
    
    
    def sub_view(self):
        return self._name[:self._viewable_chars]
    
    
    def last_char(self):
        return self._name[-1]
    
    
    def name(self):
        return self._name
        
        
        