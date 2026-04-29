def generate_code(node):
    if node['type'] == 'Program':
        return '\n'.join([generate_code(child) for child in node['body']])
        
    elif node['type'] == 'VariableDeclaration':
        init_code = generate_code(node['init'])
        return f"{node['kind']} {generate_code(node['id'])} = {init_code};"
        
    elif node['type'] == 'ExpressionStatement':
        return f"{generate_code(node['expression'])};"
        
    elif node['type'] == 'BinaryExpression':
        return f"{generate_code(node['left'])} {node['operator']} {generate_code(node['right'])}"
        
    elif node['type'] == 'CallExpression':
        callee = generate_code(node['callee'])
        args = ', '.join([generate_code(arg) for arg in node['arguments']])
        return f"{callee}({args})"
        
    elif node['type'] == 'MemberExpression':
        obj = generate_code(node['object'])
        prop = generate_code(node['property'])
        return f"{obj}.{prop}"
        
    elif node['type'] == 'Identifier':
        return node['name']
        
    elif node['type'] == 'NumericLiteral':
        return str(node['value'])
        
    elif node['type'] == 'StringLiteral':
        return f'"{node["value"]}"'
        
    else:
        raise ValueError(f"Unknown node type for generation: {node['type']}")
