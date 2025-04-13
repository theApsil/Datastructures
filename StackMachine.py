from stack import *


def stack_to_list(stack):
    lst = []
    while stack:
        lst.append(str(stack.value))
        stack = stack.next
    return lst[::-1]

def evaluate_postfix(expression, stack=None):
    tokens = expression.split()

    print("-" * 65)
    print(f"{'Токен':^10} | {'Стек после действия':^30}")
    print("-" * 65)

    for token in tokens:
        if token.replace('.', '', 1).lstrip('-').isdigit():
            stack = push(stack, float(token))
        elif token in "+-*/^":
            b, stack = pop(stack)
            a, stack = pop(stack)
            result = apply_operator(a, b, token)
            stack = push(stack, result)
        else:
            raise ValueError(f"Недопустимый токен: {token}")
        
        print(f"{token:^10} | {' '.join(stack_to_list(stack)):<30}")

    result, stack = pop(stack)
    if not is_empty(stack):
        raise ValueError("Ошибка: в стеке остались лишние элементы")
    
    print("-" * 65)
    return result

def apply_operator(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    if op == '^':
        return a ** b
    raise ValueError(f"Неизвестный оператор: {op}")


if __name__ == "__main__":
    try:
        expr = input("Введите постфиксное выражение: ")
        result = evaluate_postfix(expr)
        print("\nРезультат вычисления:", result)
    except Exception as e:
        print("Ошибка:", e)