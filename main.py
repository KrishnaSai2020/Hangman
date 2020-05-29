import random
from modules import hangman_gen

dict_of_names = {
    1: ['Name','How'],
    2: ['howdy'],
    3: ['skiddlywup']

}

try:
    difficulty_level = int(input("please enter the level of difficulty(1,2,3 with 3 being the hardest): "))
    assert 1 <= difficulty_level <= 3

except TypeError:
    print("you cannot enter a word please enter ")
    difficulty_level = int(input("please enter the level of difficulty(1,2,3 with 3 being the hardest): "))

except AssertionError:
    print("please enter a difficulty between 1-3 ")
    difficulty_level = int(input("please enter the level of difficulty(1,2,3 with 3 being the hardest): "))

except:
    print("an unknown exception occurred")
    difficulty_level = int(input("please enter the level of difficulty(1,2,3 with 3 being the hardest): "))

random_word = random.choice(dict_of_names[difficulty_level])
length_of_word = int(len(random_word))

for i in random_word:
    print('_', end='')

print("")

attempts = []
num_attempts = len(attempts)

hangman_gen(num_attempts)
