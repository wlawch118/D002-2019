﻿import random
print('')
p_choice=int(input("""Welcome to the rock-paper-scissor game!
You are going to play against a minion!
Please input your choice
1.                 2.                           3.
    _______                 _______                      _______
---'   ____)            ---'   ____)____             ---'   ____)____
      (_____)                     ______)                      ______) 
      (_____)                     _______)                  __________)
      (____)                     _______)                  (____)
---.__(___)             ---.__________)              ---.__(___)
"""))
m_choice=random.randint(1,3)
status = 0
if (p_choice+2)%3==m_choice%3:
    status=1
elif (p_choice+1)%3==m_choice%3:
    status=2
elif p_choice==m_choice:
    status=3
if m_choice == 1:
    print("Minion chooses rock!")
elif m_choice == 2:
    print("Minion chooses paper!")
elif m_choice == 3:
    print("Minion chooses scissor!")
if status == 1:
    print("You Win! Minion Loses!")
    print("""──────────▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
────────█═════════════════█
──────█═════════════════════█
─────█═══▄▄▄▄▄▄▄═══▄▄▄▄▄▄▄═══█
────█═══█████████═█████████═══█
────█══██▀────▀█████▀────▀██══█
───██████──█▀█──███──█▀█──██████
───██████──▀▀▀──███──▀▀▀──██████
────█══▀█▄────▄██─██▄────▄█▀══█
────█════▀█████▀───▀█████▀════█
────█═════════════════════════█
────█══════════▄▀▀▀▄══════════█
───▐▓▓▌═══════▀═════▀═══════▐▓▓▌
───▐▐▓▓▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐▓▓▌▌
───█══▐▓▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄▓▌══█
──█══▌═▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌═▐══█
──█══█═▐▓▓▓▓▓▓▄▄▄▄▄▄▄▓▓▓▓▓▓▌═█══█
──█══█═▐▓▓▓▓▓▓▐██▀██▌▓▓▓▓▓▓▌═█══█
──█══█═▐▓▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▌═█══█
──█══█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█══█
─▄█══█▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌█══█▄
─█████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─█████
─██████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─██████
──▀█▀█──▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌───█▀█▀
─────────▐▓▓▓▓▓▓▌▐▓▓▓▓▓▓▌
──────────▐▓▓▓▓▌──▐▓▓▓▓▌
─────────▄████▀────▀████▄
─────────▀▀▀▀────────▀▀▀▀""")
elif status == 2:
    print("You Lose! Minion Wins!")
    print("""──────────▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
────────█═════════════════█
──────█═════════════════════█
─────█═══▄▄▄▄▄▄▄═══▄▄▄▄▄▄▄═══█
────█═══█████████═█████████═══█
────█══██▀────▀█████▀────▀██══█
───██████──█▀█──███──█▀█──██████
───██████──▀▀▀──███──▀▀▀──██████
────█══▀█▄────▄██─██▄────▄█▀══█
────█════▀█████▀───▀█████▀════█
────█═════════════════════════█
────█═════════▀▄═══▄▀═════════█
───▐▓▓▌═════════▀▀▀═════════▐▓▓▌
───▐▐▓▓▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐▓▓▌▌
───█══▐▓▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄▓▌══█
──█══▌═▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌═▐══█
──█══█═▐▓▓▓▓▓▓▄▄▄▄▄▄▄▓▓▓▓▓▓▌═█══█
──█══█═▐▓▓▓▓▓▓▐██▀██▌▓▓▓▓▓▓▌═█══█
──█══█═▐▓▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▌═█══█
──█══█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█══█
─▄█══█▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌█══█▄
─█████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─█████
─██████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─██████
──▀█▀█──▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌───█▀█▀
─────────▐▓▓▓▓▓▓▌▐▓▓▓▓▓▓▌
──────────▐▓▓▓▓▌──▐▓▓▓▓▌
─────────▄████▀────▀████▄
─────────▀▀▀▀────────▀▀▀▀""")
elif status == 3:
    print('Draw!')
    print("""──────────▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
────────█═════════════════█
──────█═════════════════════█
─────█═══▄▄▄▄▄▄▄═══▄▄▄▄▄▄▄═══█
────█═══█████████═█████████═══█
────█══██▀────▀█████▀────▀██══█
───██████──█▀█──███──█▀█──██████
───██████──▀▀▀──███──▀▀▀──██████
────█══▀█▄────▄██─██▄────▄█▀══█
────█════▀█████▀───▀█████▀════█
────█═════════════════════════█
────█═══════▄▄▄▄▄▄▄▄▄▄▄═══════█
───▐▓▓▌═════════════════════▐▓▓▌
───▐▐▓▓▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▐▓▓▌▌
───█══▐▓▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄▓▌══█
──█══▌═▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌═▐══█
──█══█═▐▓▓▓▓▓▓▄▄▄▄▄▄▄▓▓▓▓▓▓▌═█══█
──█══█═▐▓▓▓▓▓▓▐██▀██▌▓▓▓▓▓▓▌═█══█
──█══█═▐▓▓▓▓▓▓▓▀▀▀▀▀▓▓▓▓▓▓▓▌═█══█
──█══█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█══█
─▄█══█▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌█══█▄
─█████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─█████
─██████▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌─██████
──▀█▀█──▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌───█▀█▀
─────────▐▓▓▓▓▓▓▌▐▓▓▓▓▓▓▌
──────────▐▓▓▓▓▌──▐▓▓▓▓▌
─────────▄████▀────▀████▄
─────────▀▀▀▀────────▀▀▀▀""")
else:
    print("Wrong input!")
input()
