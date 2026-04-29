import copy
from transformer import traverse

def optimize(ast):
    """
    Optimizes the AST by performing Constant Folding.
    It evaluates binary expressions where both operands are NumericLiterals.
    """
    new_ast = copy.deepcopy(ast)

    def exit_binary_expr(node):
        # We only fold if both children are numeric literals
        left = node.get('left')
        right = node.get('right')
        
        if left and right and left.get('type') == 'NumericLiteral' and right.get('type') == 'NumericLiteral':
            operator = node.get('operator')
            left_val = left.get('value')
            right_val = right.get('value')
            
            result = None
            if operator == '+':
                result = left_val + right_val
            elif operator == '-':
                result = left_val - right_val
            elif operator == '*':
                result = left_val * right_val
            elif operator == '/':
                if right_val != 0:
                    result = left_val / right_val
            
            if result is not None:
                # Transform the BinaryExpression into a NumericLiteral
                # Remove left, right, operator fields and set value
                node.clear()
                node['type'] = 'NumericLiteral'
                node['value'] = result

    visitor = {
        'BinaryExpression': {
            'exit': exit_binary_expr
        }
    }

    traverse(new_ast, visitor)
    return new_ast
