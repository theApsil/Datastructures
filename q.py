from dataclasses import dataclass
import random

@dataclass
class Node:
    name: str
    next: 'Node'


def create_queue():
    return None, None


def is_empty(queue):
    head, _ = queue
    return head is None


def enqueue(queue, name):
    head, tail = queue
    new_node = Node(name, None)
    if tail is None:
        return new_node, new_node
    tail.next = new_node
    return head, new_node


def dequeue(queue):
    head, tail = queue
    if head is None:
        print("Очередь пуста.")
        return queue
    print(f"{head.name} завершил стирку и покидает очередь.")
    return head.next, tail if head.next is not None else (None, None)


def print_queue(queue):
    head, _ = queue
    current = head
    print("Текущая очередь:")
    if not current:
        print("  [пусто]")
    while current:
        print(f"  {current.name}")
        current = current.next

 
def simulate_washing_queue(queue):
    user_id = 1

    print("Нажмите Enter для следующего шага или введите 'q' чтобы выйти.\n")

    while True:
        action = random.choice(['enqueue', 'dequeue'])

        if action == 'enqueue':
            name = f"Студент_{user_id}"
            queue = enqueue(queue, name)
            print(f"{name} добавлен в очередь на стирку.")
            user_id += 1
        else:
            queue = dequeue(queue)

        print_queue(queue)

        user_input = input("\nПродолжить? [Enter] / Выйти [q]: ").strip().lower()
        if user_input == 'q':
            print("Симуляция завершена.")
            break
        print()


if __name__ == "__main__":
    queue = create_queue()
    simulate_washing_queue(queue)
