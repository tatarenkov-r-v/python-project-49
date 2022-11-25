from brain_games.engine import engine


from brain_games.games.gcd import subtext, gen_question


def main():
    return engine(subtext, gen_question)


main()
