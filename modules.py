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
