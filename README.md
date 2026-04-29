# Mini JavaScript Compiler

A tiny compiler written in Python that parses a small subset of modern JavaScript and transpiles it into older ES5 JavaScript syntax. 

For example, it successfully transforms modern ES6 `let` declarations into ES5 `var` declarations while preserving operations, strings, and function calls.

## Architecture

This compiler follows a classic 4-phase architecture:

1. **Lexical Analysis (`tokenizer.py`)**: Takes raw JavaScript code as a string and groups the characters into a flat list of **Tokens** (such as keywords, identifiers, and numbers).
2. **Syntactic Analysis (`parser.py`)**: Iterates through the tokens and builds an **Abstract Syntax Tree (AST)** that represents the grammatical structure of the code.
3. **Transformation (`transformer.py`)**: Traverses the AST using the Visitor pattern and modifies it to match the target language format (e.g., swapping `let` to `var`).
4. **Code Generation (`generator.py`)**: Takes the new transformed AST and stringifies it back into raw, valid JavaScript code.

## Supported Features
- Variable declarations (`let`, `const`, `var`)
- Basic mathematics (`+`, `-`, `*`, `/`)
- Strings and Numbers
- Function calls (`console.log`)

## How to Run

1. Ensure you have Python 3 installed.
2. Run the main compiler script:
   ```bash
   python3 compiler.py
   ```

When you run it, the program will print out the results of every phase so you can see exactly how the code is being transformed under the hood!

### Modifying the Input Code

If you want to feed your own JavaScript code into the compiler, open `compiler.py` and modify the `sample_code` string at the bottom of the file:

```python
if __name__ == '__main__':
    sample_code = """
    let x = 10 + 20;
    console.log("Result is", x);
    """
    compile_code(sample_code)
```

## Running Tests

To verify that the compiler is functioning correctly and successfully handling variable declarations and mathematical precedence, you can run the test suite:

```bash
python3 test_compiler.py
```
