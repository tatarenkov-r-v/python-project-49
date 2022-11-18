from random import randint


import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        question = randint(1, 100)
        print(f'Questions: {question}')
        user_answer = input('Your answer:')
        if (question % 2 == 0 and user_answer == 'yes') or \
                (question % 2 != 0 and user_answer == 'no'):
            print('Correct!')
            i += 1
        elif question % 2 == 0 and user_answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'."
                  f"\nLet's try again, {name}!")
            exit()
        elif question % 2 != 0 and user_answer == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'."
                  f"\nLet's try again, {name}!")
            exit()
        else:
            exit()
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
