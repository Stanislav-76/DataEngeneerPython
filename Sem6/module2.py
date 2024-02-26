import random as rnd


def guess_riddle(riddle: str, answers: list, attempts: int):
    right_answer = rnd.randint(0, len(answers) - 1)
    attempt_number = 0
    print(riddle)
    for i, j in enumerate(answers, 1):
        print(f"{i}. {j}")
    while attempt_number < attempts:
        attempt_number += 1
        answer = int(input("Введите номер отгадки: "))
        if answer == right_answer - 1:
            print("Правильно!")
            return attempt_number
    return 0