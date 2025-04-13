from SortingStation import infix_to_postfix
from StackMachine import evaluate_postfix


if __name__ == "__main__":
    expr = input("Введите арифметическое выражение: ")
    try:
        postfix_expr = infix_to_postfix(expr)
        print("Постфиксная форма:", postfix_expr)

        result = evaluate_postfix(postfix_expr)
        print("Результат:", result)
    except Exception as e:
        print("Ошибка:", e)