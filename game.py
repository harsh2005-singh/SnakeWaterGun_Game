# game.py
import random

def play(choice: str) -> dict:
    computer = random.choice([-1, 0, 1])
    you_dict = {"s": 1, "w": -1, "g": 0}
    reverse = {1: "Snake", -1: "Water", 0: "Gun"}

    you = you_dict[choice]

    if computer == you:
        result = "draw"
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        result = "win"
    else:
        result = "lose"

    return {
        "you": reverse[you],
        "computer": reverse[computer],
        "result": result
    }