from random import randint


from random import choice


def subtext():
    return 'What is the result of the expression?'


def gen_question():
    '''Функция генерирующая вопрос'''
    a = randint(0, 100)
    b = randint(1, 100)
    op = choice([" + ", " - ", " * "])
    question = str(a) + op + str(b)
    answer_to_question = eval(question)
    return question, str(answer_to_question)
