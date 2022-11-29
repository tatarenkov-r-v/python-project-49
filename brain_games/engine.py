import prompt


def engine(subtext, gen_question):
    '''Движок игры'''
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    text = subtext()
    print(text)
    i = 0
    while i < 3:
        questions = gen_question()
        que = list(questions)
        question = que[0]
        correct_answer = que[1]
        print(f'Question: {question}')
        user_answer = input('Your answer:')
        if user_answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was"
                  f" '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')
    exit()
