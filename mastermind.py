# AI will pick 4 numbers from 1 to 8 without repeat as the solution.
# User guess 4 numbers each round.
# AI will tell how many numbers appeared in the solution and in correct position (A).
# AI will also tell how many number appeared in the solution but not in correct position (B).
# AI tells how many guesses the user took after the correct solution is entered.

import random

list = [1, 2, 3, 4, 5, 6, 7, 8]
solution = []

for i in range(1, 5):
    pick = random.randint(1, len(list)) - 1
    solution.append(list[pick])
    list.pop(pick)

num_guess = 0

while True:
    a = 0
    b = 0
    solution_copy = solution.copy()
    guess = int(input("What do you guess? please input four numbers: "))
    # find each digit
    first = guess // 1000
    second = guess % 1000 // 100
    third = guess % 100 // 10
    forth = guess % 10
    guess_list = [first, second, third, forth]

    # compare to the solution (exact match)
    for i in range(0, 4):
        if guess_list[i] == None:
            break
        if guess_list[i] == solution_copy[i]:
            a += 1
            guess_list[i] = None
            solution_copy[i] = None

    # compare to the solution (right about the number but not position)
    for i in range(0, 4):
        for y in range(0, 4):
            if guess_list[i] == None:
                break
            if guess_list[i] == solution_copy[y]:
                b += 1
                guess_list[i] = None
                solution_copy[y] = None
                break

    # print(solution_copy)
    # print(solution)
    num_guess += 1
    if a != 4:
        print(f"{a}A{b}B")
    else:
        break

print(f"You win! you guessed {num_guess} times.")