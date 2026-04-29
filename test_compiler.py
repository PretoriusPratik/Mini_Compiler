import unittest
from compiler import compile_code

class TestMiniCompiler(unittest.TestCase):
    def test_variable_declaration(self):
        input_code = "let x = 100;"
        output_code = compile_code(input_code)
        self.assertEqual(output_code.strip(), "var x = 100;")

    def test_basic_math(self):
        input_code = "const result = 10 + 20 * 5;"
        output_code = compile_code(input_code)
        # Note: Our simple string generation will output exactly as it was structured
        # 20 * 5 happens first based on precedence parser, but parenthesis aren't generated 
        # unless we explicitly add them. It will still evaluate correctly in JS.
        self.assertEqual(output_code.strip(), "var result = 10 + 20 * 5;")

    def test_console_log(self):
        input_code = 'console.log("hello", 42);'
        output_code = compile_code(input_code)
        self.assertEqual(output_code.strip(), 'console.log("hello", 42);')

    def test_complex_program(self):
        input_code = '''
        let a = 10;
        let b = a * 2;
        console.log(b);
        '''
        output_code = compile_code(input_code)
        expected = 'var a = 10;\nvar b = a * 2;\nconsole.log(b);'
        self.assertEqual(output_code.strip(), expected)

if __name__ == '__main__':
    unittest.main()
