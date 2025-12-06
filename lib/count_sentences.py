#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        # Replace all punctuation with a single marker
        import re
        
        # This pattern looks for one or more punctuation marks (.!?)
        temp_value = re.sub(r'[.!?]+', '|', self.value)
        
        # Split by our marker and count non-empty strings
        sentences = [s for s in temp_value.split('|') if s.strip()]
        
        return len(sentences)