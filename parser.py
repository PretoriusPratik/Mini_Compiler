class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        body = []
        while self.current < len(self.tokens):
            body.append(self.parse_statement())
        return {'type': 'Program', 'body': body}

    def peek(self):
        if self.current < len(self.tokens):
            return self.tokens[self.current]
        return None

    def consume(self):
        token = self.peek()
        self.current += 1
        return token

    def parse_statement(self):
        token = self.peek()
        if token['type'] == 'keyword' and token['value'] in ('let', 'var', 'const'):
            return self.parse_variable_declaration()
        return self.parse_expression_statement()

    def parse_variable_declaration(self):
        kind = self.consume()['value'] # let, var, const
        id_token = self.consume()
        if id_token['type'] != 'identifier':
            raise ValueError(f"Expected identifier, got {id_token['value']}")
        
        # expect '='
        eq_token = self.consume()
        if eq_token['value'] != '=':
            raise ValueError(f"Expected '=', got {eq_token['value']}")
            
        init = self.parse_expression()
        
        # expect optional ';'
        if self.peek() and self.peek()['value'] == ';':
            self.consume()
            
        return {
            'type': 'VariableDeclaration',
            'kind': kind,
            'id': {'type': 'Identifier', 'name': id_token['value']},
            'init': init
        }

    def parse_expression_statement(self):
        expr = self.parse_expression()
        # expect optional ';'
        if self.peek() and self.peek()['value'] == ';':
            self.consume()
        return {
            'type': 'ExpressionStatement',
            'expression': expr
        }

    def parse_expression(self):
        return self.parse_additive()

    def parse_additive(self):
        left = self.parse_multiplicative()
        while self.peek() and self.peek()['type'] == 'operator' and self.peek()['value'] in ('+', '-'):
            operator = self.consume()['value']
            right = self.parse_multiplicative()
            left = {
                'type': 'BinaryExpression',
                'operator': operator,
                'left': left,
                'right': right
            }
        return left

    def parse_multiplicative(self):
        left = self.parse_primary()
        while self.peek() and self.peek()['type'] == 'operator' and self.peek()['value'] in ('*', '/'):
            operator = self.consume()['value']
            right = self.parse_primary()
            left = {
                'type': 'BinaryExpression',
                'operator': operator,
                'left': left,
                'right': right
            }
        return left

    def parse_primary(self):
        token = self.consume()
        
        if token['type'] == 'number':
            return {'type': 'NumericLiteral', 'value': float(token['value']) if '.' in token['value'] else int(token['value'])}
        elif token['type'] == 'string':
            return {'type': 'StringLiteral', 'value': token['value']}
        elif token['type'] == 'identifier':
            node = {'type': 'Identifier', 'name': token['value']}
            # Check for MemberExpression (e.g. console.log)
            while self.peek() and self.peek()['value'] == '.':
                self.consume() # consume '.'
                prop = self.consume()
                node = {
                    'type': 'MemberExpression',
                    'object': node,
                    'property': {'type': 'Identifier', 'name': prop['value']}
                }
            # Check for CallExpression (e.g. log(...))
            if self.peek() and self.peek()['value'] == '(':
                self.consume() # consume '('
                arguments = []
                while self.peek() and self.peek()['value'] != ')':
                    arguments.append(self.parse_expression())
                    if self.peek() and self.peek()['value'] == ',':
                        self.consume() # consume ','
                self.consume() # consume ')'
                node = {
                    'type': 'CallExpression',
                    'callee': node,
                    'arguments': arguments
                }
            return node
        elif token['value'] == '(':
            expr = self.parse_expression()
            self.consume() # consume ')'
            return expr
            
        raise ValueError(f"Unexpected token in expression: {token}")

def parse(tokens):
    return Parser(tokens).parse()
