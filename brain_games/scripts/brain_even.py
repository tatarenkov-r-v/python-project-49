
from brain_games.scripts.brain_games import welcome

from random import randint

welcome()

def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        question = randint(1, 100)
        print(f'Questions: {question}')
        user_answer = input('Your answer:')
        if (question % 2 == 0 and user_answer == 'yes') or (question % 2 != 0 and user_answer == 'no'):
            print('Correct!')
            i += 1
        elif question % 2 == 0 and user_answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            exit()
        elif question % 2 != 0 and user_answer == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            exit()
        else:
            exit()
    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
