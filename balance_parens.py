from stacks import Stack

def balance(equation):
    """check if parentheses are balanced"""

    parens = Stack()

    for char in equation:
        if char == "(":
            parens.push("(")
        elif char == ")":
            if parens.is_empty():
                return False
            parens.pop()

    return parens.is_empty()
