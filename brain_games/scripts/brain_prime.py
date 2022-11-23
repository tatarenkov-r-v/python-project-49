from random import randint


import prompt


subtext = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def gen_question():
    '''Функция генерирующая вопрос'''
    return randint(2, 100)


def is_correct_answer(question):
    '''Функция возвращающая правильный ответ на вопрос'''
    k = 0
    for i in range(2, question // 2 + 1):
        if (question % i == 0):
            k = k + 1
    return 'yes' if k <= 0 else 'no'


def main():
    '''Движок игры'''
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print(subtext)
    i = 0
    while i < 3:
        question = gen_question()
        print(f'Questions: {question}')
        user_answer = input('Your answer:')
        correct_answer = is_correct_answer(question)
        if user_answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was"
                  f" '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
