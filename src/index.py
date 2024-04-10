import datetime
import rich.traceback
from typing import Optional

rich.traceback.install()


def line(length: int = 50) -> None:
    print("-" * length)


def pomodoro_menu():
    pomodoro_title = "Pomodoro Timer ⏱"
    line()
    print(f"{pomodoro_title:^50}")
    line()
    print("1. 25/5")
    print("2. 30/5")
    print("3. 40/5")
    print("4. 45/5")
    print("5. 50/10")
    line()
    user_choice_time = int(input("What would you like to do? "))
    user_choice_cycles = int(input("How many cycles? "))
    line()

    if user_choice_time == 1:
        pomodoro(25, 5, user_choice_cycles)
    elif user_choice_time == 2:
        pomodoro(30, 5, user_choice_cycles)
    elif user_choice_time == 3:
        pomodoro(40, 5, user_choice_cycles)
    elif user_choice_time == 4:
        pomodoro(45, 5, user_choice_cycles)
    elif user_choice_time == 5:
        pomodoro(50, 10, user_choice_cycles)
    else:
        print("Invalid choice")
        pomodoro_menu()


def pomodoro(work_time: int, break_time: int, cycles: Optional[int]):
    if cycles is None:
        cycles = 1

    for _ in range(cycles):
        print(f"Cycle {_ + 1}")
        print(f"Work time: {work_time} minutes")
        print(f"Break time: {break_time} minutes")
        line()

    value = "Work"

    while True:
        now_time = datetime.datetime.now().strftime("%H:%M:%S")
        if now_time == f"{work_time}:00:00":
            print(f"{value} time!")
            line()
            value = "Break"
            break
        elif now_time == f"{break_time}:00:00":
            print(f"{value} time!")
            line()
            value = "Work"
            break

        cycles -= 1

    pomodoro_menu()


def main():
    pomodoro_menu()


if __name__ == "__main__":
    main()
