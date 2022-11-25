from random import randint


from random import choice


def subtext():
    return 'What number is missing in the progression?'


def gen_question():
    '''Функция генерирующая вопрос и возвращающая ответ'''
    a = randint(0, 50)
    b = randint(2, 5)
    c = [i for i in range(a, 100, b)]
    d = randint(5, 20)
    e = c[0:d]
    f = choice(e)
    g = e.index(f)
    answert_to_question = e[g]
    e[g] = '..'
    question = " ".join(map(str, (e)))
    return question, str(answert_to_question)
