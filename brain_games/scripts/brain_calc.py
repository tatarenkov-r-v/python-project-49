import random


import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        a = random.randint(0, 100)
        b = random.randint(1, 100)
        op = random.choice([" + ", " - ", " * "])
        question = str(a) + op + str(b)
        print(f'Question: {question}?')
        user_answer = int(input())
        print(f'Your answer: {user_answer}')
        if user_answer == eval(question):
            print("Correct!")
            i += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer is '{str(eval(question))}'."
                  f"\nLet's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
