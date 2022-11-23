from random import randint


from random import choice


import prompt


subtext = 'What number is missing in the progression?'


def gen_question():
    '''Функция генерирующая вопрос'''
    # генерируем случайное число "а", которое передадим
    # в параметр start функции range
    # для определения начала последовательности
    a = randint(0, 50)
    # генерируем еще одно случайное число "b", которое передадим
    # в параметр step функции range
    # для определения шага последовательности
    b = randint(2, 5)
    # с помощью генератора списка создаем временный
    # список "с", который содержит последовательность чисел
    # от "а" до 100 со случайным шагом "b"
    c = [i for i in range(a, 100, b)]
    # генерируем случайное число "d" для определения
    # длины итоговой последовательности (от 5 до 20)
    d = randint(5, 20)
    # создаем (срезаем) список арифметической последовательности "e"
    # ограниченной (по условиям задачи) длины
    e = c[0:d]
    # выбираем случайный элемент "f" из
    # арифметической последовательности "e"
    f = choice(e)
    # узнаем индекс случайного элемента "f" из
    # арифметической последовательности "e"
    g = e.index(f)
    # меняем значение выбранного случайным образом
    # элемента на ..
    e[g] = '..'
    # "f" - преобразовываем список последовательности
    # в строку для вывода на экран пользователю
    h = " ".join(map(str, (e)))
    # возвращаем результат
    return h


def is_correct_answer(question):
    '''Функция возвращающая правильный ответ на вопрос'''
    # преобразуем список в строку для дальнейших манипуляций
    a = question.split(' ')
    # выясним индекс скрытого элемента '..'
    b = a.index('..')
    # а также длину списка
    length = (len(a)) - 1
    # так как скрытый элемент ".." может случайным образом сгененироваться
    # как первым в списке прогресии, так и последним строки в цикле if
    # elif определяют механизм определения правильного
    # числа в данных ситуациях.
    # если скрытый элемент находится последним:
    if b == length:
        # определяем индекс числа до скрытого элемента и
        # индекс числа до данного числа
        n1_index = b - 1
        n2_index = b - 2
        # узнаем значение элементов (чисел) по индексу
        # и вычитанием определяем шаг последовательности
        w = int(a[n1_index]) - int(a[n2_index])
        # складываем значение элемента стоящего перед скрытым
        # элементом и выводим ответ
        answer = int(a[n1_index]) + w
        return str(answer)
        # если скрытый элемент стоит в начале списка
        # действуем похожим образом
    elif b == 0:
        n1_index = b + 1
        n2_index = b + 2
        w = int(a[n2_index]) - int(a[n1_index])
        answer = int(a[n1_index]) - w
        return str(answer)
        # так как при решении задачи для поиска
        # правильного элемента последовательности нам нужно
        # узнать шаг последовательности путем вычитания между собой
        # соседних элементов есть вероятность что один из нужных
        # для этого элементов будет скрытый элемент '..'
        # поймаем и обработаем ошибку и вычислим шаг с помощью
        # двух других чисел последовательности
    else:
        try:
            w = int(a[4]) - int(a[3])
        except ValueError:
            w = int(a[2]) - int(a[1])
            c = int(b) + 1
            d = a[c]
            answer = int(d) - w
        else:
            w = int(a[4]) - int(a[3])
            c = int(b) + 1
            d = a[c]
            answer = int(d) - w
        return str(answer)


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