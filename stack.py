from dataclasses import dataclass

@dataclass
class Node:
    value: str
    next: 'Node'


def create_stack():
    return None 


def is_empty(stack):
    return stack is None


def push(stack, value):
    new_node = Node(value, stack)
    return new_node


def pop(stack):
    if is_empty(stack):
        raise IndexError("pop from empty stack")
    return stack.value, stack.next


def read_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def print_reversed_text(stack, text):
    for char in text:
        stack = push(stack, char)

    while not is_empty(stack):
        char, stack = pop(stack)
        print(char, end='')


if __name__ == "__main__":
    stack = create_stack()
    text = read_text_file("text.txt")
    print_reversed_text(stack, text)
