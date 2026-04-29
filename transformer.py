def traverse_node(node, visitor):
    # Call enter if defined
    if node['type'] in visitor and 'enter' in visitor[node['type']]:
        visitor[node['type']]['enter'](node)

    # Traverse children
    if node['type'] == 'Program':
        for child in node['body']:
            traverse_node(child, visitor)
    elif node['type'] == 'VariableDeclaration':
        traverse_node(node['id'], visitor)
        if node['init']:
            traverse_node(node['init'], visitor)
    elif node['type'] == 'ExpressionStatement':
        traverse_node(node['expression'], visitor)
    elif node['type'] == 'BinaryExpression':
        traverse_node(node['left'], visitor)
        traverse_node(node['right'], visitor)
    elif node['type'] == 'CallExpression':
        traverse_node(node['callee'], visitor)
        for arg in node['arguments']:
            traverse_node(arg, visitor)
    elif node['type'] == 'MemberExpression':
        traverse_node(node['object'], visitor)
        traverse_node(node['property'], visitor)
    elif node['type'] in ('NumericLiteral', 'StringLiteral', 'Identifier'):
        pass # No children to traverse
    else:
        raise ValueError(f"Unknown node type to traverse: {node['type']}")

    # Call exit if defined
    if node['type'] in visitor and 'exit' in visitor[node['type']]:
        visitor[node['type']]['exit'](node)

def traverse(ast, visitor):
    traverse_node(ast, visitor)

def transform(ast):
    # In this mini-compiler, we will just transform 'let' or 'const' to 'var'
    # and we could also rename variables, but let's stick to the ES6 -> ES5 keyword change.
    import copy
    new_ast = copy.deepcopy(ast)

    def visit_var_decl(node):
        if node['kind'] in ('let', 'const'):
            node['kind'] = 'var'

    visitor = {
        'VariableDeclaration': {
            'enter': visit_var_decl
        }
    }

    traverse(new_ast, visitor)
    return new_ast
