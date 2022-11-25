from random import randint


from math import gcd


def subtext():
    return 'Find the greatest common divisor of given numbers?'


def gen_question():
    '''Функция генерирующая вопрос и правильный ответ'''
    a = randint(0, 100)
    b = randint(1, 100)
    question = str(a) + " " + str(b)
    string_to_list = question.split(' ')
    first_i = string_to_list[0]
    second_i = string_to_list[1]
    answer_to_question = str(gcd(int(first_i), int(second_i)))
    return question, answer_to_question
