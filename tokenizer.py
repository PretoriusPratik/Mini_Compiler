import re

def tokenize(code):
    tokens = []
    current = 0
    
    while current < len(code):
        char = code[current]
        
        # Skip whitespace
        if re.match(r'\s', char):
            current += 1
            continue
            
        # Punctuation
        if char in ('=', ';', '(', ')', '.', ','):
            tokens.append({'type': 'punctuation', 'value': char})
            current += 1
            continue
            
        # Operators
        if char in ('+', '-', '*', '/'):
            tokens.append({'type': 'operator', 'value': char})
            current += 1
            continue
            
        # Numbers
        if re.match(r'[0-9]', char):
            value = ''
            while current < len(code) and re.match(r'[0-9\.]', code[current]):
                value += code[current]
                current += 1
            tokens.append({'type': 'number', 'value': value})
            continue
            
        # Identifiers and Keywords
        if re.match(r'[a-zA-Z_]', char):
            value = ''
            while current < len(code) and re.match(r'[a-zA-Z0-9_]', code[current]):
                value += code[current]
                current += 1
                
            if value in ('let', 'var', 'const', 'function'):
                tokens.append({'type': 'keyword', 'value': value})
            else:
                tokens.append({'type': 'identifier', 'value': value})
            continue
            
        # Strings (simple)
        if char in ('"', "'"):
            quote = char
            value = ''
            current += 1
            while current < len(code) and code[current] != quote:
                value += code[current]
                current += 1
            current += 1 # skip closing quote
            tokens.append({'type': 'string', 'value': value})
            continue
            
        raise ValueError(f"Unexpected character: {char}")
        
    return tokens
