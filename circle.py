from dataclasses import dataclass

@dataclass
class Node:
    name: str
    next: 'Node'


def create_circle(n):
    first = Node(f"Игрок_1", None)
    prev = first
    for i in range(2, n + 1):
        node = Node(f"Игрок_{i}", None)
        prev.next = node
        prev = node
    prev.next = first
    return first


def run_counting_game(start, k):
    current = start
    prev = None

    while current.next != current:
        for _ in range(k - 1):
            prev = current
            current = current.next
        print(f"{current.name} выбывает из игры.")
        prev.next = current.next
        current = current.next

    return current.name


def play_game(circle, n, k):
    if n <= k:
        print("Ошибка: количество участников должно быть больше количества слов в считалочке.")
        return

    
    winner = run_counting_game(circle, k)
    print(f"\n🏆 Победитель: {winner}")


if __name__ == "__main__":
    try:
        N = int(input("Введите количество участников (N): "))
        circle = create_circle(N)
        K = int(input("Введите количество слов в считалочке (K): "))
        play_game(circle, N, K)
    except ValueError:
        print("Ошибка: введите целые числа.")
