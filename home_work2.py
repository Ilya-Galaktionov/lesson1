def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    phrase = f'{one} {delimiter} {two}'
    print(phrase.upper())
get_summ('Learn', 'python')