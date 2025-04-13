from stack import *


def stack_to_list(stack):
    lst = []
    while stack:
        lst.append(stack.value)
        stack = stack.next
    return lst[::-1]


def peek(stack):
    if stack is None:
        return None
    return stack.value

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


def is_left_associative(op):
    return op != '^'


def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue
        if expr[i].isalnum():
            token = expr[i]
            while i + 1 < len(expr) and expr[i + 1].isalnum():
                i += 1
                token += expr[i]
            tokens.append(token)
        else:
            tokens.append(expr[i])
        i += 1
    return tokens


def infix_to_postfix(expression):
    output = []
    stack = None

    tokens = tokenize(expression)

    print("-" * 65)
    print(f"{'Токен':^10} | {'Выход':^30} | {'Стек':^20}")
    print("-" * 65)

    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack = push(stack, token)
        elif token == ')':
            while not is_empty(stack) and peek(stack) != '(':
                top, stack = pop(stack)
                output.append(top)
            if is_empty(stack):
                raise ValueError("Скобки несбалансированы")
            _, stack = pop(stack)
        elif token in "+-*/^":
            while (
                not is_empty(stack) and
                peek(stack) != '(' and
                (
                    precedence(peek(stack)) > precedence(token) or
                    (precedence(peek(stack)) == precedence(token) and is_left_associative(token))
                )
            ):
                top, stack = pop(stack)
                output.append(top)
            stack = push(stack, token)
        print(f"{token:^10} | {' '.join(output):<30} | {' '.join(stack_to_list(stack)):<20}")

    while not is_empty(stack):
        top, stack = pop(stack)
        if top == '(':
            raise ValueError("Скобки несбалансированы")
        output.append(top)
        print(f"{'—':^10} | {' '.join(output):<30} | {' '.join(stack_to_list(stack)):<20}")
    
    print("-" * 65)
    return " ".join(output)


if __name__ == "__main__":
    try:
        expr = input("Введите арифметическое выражение: ")
        postfix = infix_to_postfix(expr)
        print("Постфиксная форма:", postfix)
    except Exception as e:
        print("Ошибка:", e)