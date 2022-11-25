from random import randint


def subtext():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def gen_question():
    '''Функция генерирующая вопрос и правильный ответ'''
    question = randint(2, 100)
    k = 0
    for i in range(2, question // 2 + 1):
        if (question % i == 0):
            k = k + 1
    answer_to_question = 'yes' if k <= 0 else 'no'
    return question, answer_to_question
