from random import randint


import prompt


from math import gcd


subtext = 'Find the greatest common divisor of given numbers?'


def gen_question():
    '''Функция генерирующая вопрос'''
    a = randint(0, 100)
    b = randint(1, 100)
    return str(a) + " " + str(b)


def is_correct_answer(question):
    '''Функция возвращающая правильный ответ на вопрос'''
    string_to_list = question.split(' ')
    first_i = string_to_list[0]
    second_i = string_to_list[1]
    return str(gcd(int(first_i), int(second_i)))


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
