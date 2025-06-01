import sys
from antlr4 import *
from gLexer import gLexer
from gParser import gParser
from gVisitorImpl import GVisitorImpl

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 g.py <source_file.j>")
        sys.exit(1)

    input_file = sys.argv[1]
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = gLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = gParser(tokens)

    tree = parser.root()
    # Descomentar la següent línia per a veure el parse tree.
    # print(tree.toStringTree(recog=parser))
    visitor = GVisitorImpl()
    visitor.visit(tree)


if __name__ == '__main__':
    main()