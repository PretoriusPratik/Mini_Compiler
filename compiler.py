from tokenizer import tokenize
from parser import parse
from transformer import transform
from generator import generate_code

def compile_code(input_code):
    print(f"--- Original Code ---\n{input_code}\n")
    
    # 1. Lexical Analysis
    tokens = tokenize(input_code)
    print("--- Tokens ---")
    for t in tokens:
        print(t)
    print()
    
    # 2. Syntactic Analysis
    ast = parse(tokens)
    print("--- Abstract Syntax Tree (AST) ---")
    import json
    print(json.dumps(ast, indent=2))
    print()
    
    # 3. Transformation
    new_ast = transform(ast)
    print("--- Transformed AST ---")
    print(json.dumps(new_ast, indent=2))
    print()
    
    # 4. Code Generation
    output_code = generate_code(new_ast)
    print(f"--- Output Code ---\n{output_code}\n")
    
    return output_code

if __name__ == '__main__':
    sample_code = """
    let x = 10 + 20;
    console.log("Result is", x);
    """
    compile_code(sample_code)
