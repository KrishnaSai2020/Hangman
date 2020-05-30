def hangman_gen(num_attempts):
    if num_attempts == 0:
        print('0 attempts')
    elif num_attempts == 1:
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('_____________')

    elif num_attempts == 2:
        print('|            ')
        print('|            ')
        print('|            ')
        print('|            ')
        print('|            ')
        print('|            ')
        print('|____________')

    elif num_attempts == 3:
        print('|------------')
        print('|            ')
        print('|            ')
        print('|            ')
        print('|            ')
        print('|            ')
        print('|____________')

    elif num_attempts == 4:
        print('|-------------')
        print('|      |      ')
        print('|   { .  . }  ')
        print('|       |     ')
        print('|       |     ')
        print('|     |   |   ')
        print('|_____|___|___')
