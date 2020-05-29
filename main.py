import random

dict_of_names = {
    # fill with words and difficulty number 1-3
    # eg '1:['','','','','','','','']'
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

length_of_word = len(random_word)


