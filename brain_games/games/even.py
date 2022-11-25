from random import randint


def subtext():
    return 'Answer "yes" if the number is even, otherwise answer "no"?'


def gen_question():
    '''Функция генерирующая вопрос и правильный ответ'''
    question = randint(1, 100)
    answer_to_question = 'yes' if question % 2 == 0 else 'no'
    return question, answer_to_question
