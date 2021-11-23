# Using Backus–Naur form
# node[0] = data
# node[1] = left
# node[2] = right

import re as regex
import argparse
import sys

operations = ['.', "**", "^", "//", '/', '*', '-', '+']

def parenthesis(lexmes):
    stack = [[]]
    j = 1
    for current_token in lexmes:
        if current_token == '(':
            stack.append([])
            j += 1
        elif current_token == ')':
            if j > 0:
                j -= 1
                stack[j - 1].append(stack.pop())
            else:
                return None
        else:
            stack[j - 1].append(current_token)
    if j == 1:
        return stack[0]
    else:
        return None


def make_concrete_syntax_tree(expression):
    if len(expression) < 3:
        return expression
    for e in expression:
        if isinstance(expression, list):
            make_concrete_syntax_tree(e)
    i = 1
    for operand in operations:
        while i < len(expression):
            if expression[i] == operand:
                left = expression.pop(i - 1)
                expression.pop(i - 1)
                right = expression.pop(i - 1)
                expression.insert(i - 1, [operand, left, right])
            else:
                i += 1
        i = 1
    return expression[0]


def make_abstract_syntax_tree(node):
    if isinstance(node, str):
        return str
    if isinstance(node, list) and len(node) <= 1:
        return node[0]
    if isinstance(node[1], list):
        node[1] = make_abstract_syntax_tree(node[1])
    if len(node) > 2:
        if isinstance(node[2], list):
            node[2] = make_abstract_syntax_tree(node[2])
    else:
        node = [node[0], 0, node[1]]
    return node


def evaluate(node):
    optable = {  #
        '+': lambda a, b: a + b,  #
        '-': lambda a, b: a - b,  #
        '*': lambda a, b: a * b,  #
        '/': lambda a, b: a / b,  #
       r"//": lambda a, b: a // b,
        '.': lambda a, b: a + (b*0.1),
        '^': lambda a, b: a ** b,
        "**":lambda a, b:  optable['^'](a,b)
    }
    var = [0, 0]
    if node[0] not in operations:
        if len(node) == 1:
            node = ['+', 0, node[0]]
        else:
            raise "Something went wrong"
    for i in range(1, 3):
        res = []
        if isinstance(node[i], list):
            res = evaluate(node[i])
        else:
            res = node[i]
        if res:
            var[i - 1] = float(res)
    #print(f"{var[0]} {node[0]} {var[1]} = "
    #f"{optable[node[0]](var[0], var[1])}")
    return optable[node[0]](var[0], var[1])


def calc(string):
    lexemes = regex.findall(r"[*\/]{2}|[()*\/+-.^]|\d+", string)
    tokens = parenthesis(lexemes)

    if tokens == None:
        raise "Missing Parenthesis"
    cst = make_concrete_syntax_tree(tokens)
    #print(cst)
    ast = make_abstract_syntax_tree(cst)

    res = evaluate(ast)
    if not int(res) - res:
      res = int(res)
    return res


tests = [
    "3+6*(1+3)",
    "6/2*(1+2)",
    "(6/1)*2/(1+2)",
    "(2)^(2.5)",
    "1/2",
    "4//3",
    "-1",
    "1",
    "-(0)",
    "0",
    "1-1",
    "(((2)))",
    "1+1+1+1+1",
    "2/2/2",
    "2^10",
    "2*2*2*2*2*2*2*2*2*2"  # 2^10
]
string = ""
for current_equation in tests:
    calculated_result = calc(current_equation)
    print(f"{current_equation} = {calculated_result}")

"""
def main(argc, argv):
    parser = argparse.ArgumentParser(prog='Calculator',
                                     usage='%(prog)s <expression>',
                                     description='This program will calculate the result of an expression')
    args, unknown = parser.parse_known_args()
    if argc <= 1:
        parser.print_help()
        exit(0)
    expr = argv[1]
    calculated_result = calc(expr)
    print(f"{calculated_result=}")
    return


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)"""
