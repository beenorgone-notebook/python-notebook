import cProfile
import itertools
import re
import time


def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
        ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation

# Faster version by Peter Norvig


def faster_solve(formula):
    '''Given a formula like 'ODD + ODD == EVEN', fill in digits to
    solve it. Input formula is a string, output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula.'''
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                yield formula.translate(table)
        except ArithmeticError:
            pass


def compile_formula(formula, verbose=False):
    '''Compile formula into a function. Also returns letters found,
    as a str, in same order as parms of function. For example,
    "YOU == ME**2" returns (lambda Y, M, E, U, O: (U+10*0+100*Y) == (E+10*M)**2), "YMEUO" '''
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    first_letters = set([word[0] for word in re.findall('[A-Z]+', formula)])
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    tests = ' and '.join(L + '!= 0' for L in first_letters)
    body = ''.join(tokens) + ' and ' + tests
    f = 'lambda {}: {}'.format(parms, body)
    if verbose:  # use for debugging
        print(f)
    return eval(f), letters


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [str(10**i) + '*' + c for i, c in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word


def test(func):
    t0 = time.clock()
    for example in examples:
        print('{}: {}'.format(example, timedcall(func, example)))
    print('Runtime is {}'.format(time.clock() - t0))


def timedcall(fn, *args):
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    try:
        return t1 - t0, tuple(result)
    except StopIteration:
        return t1 - t0, None

examples = '''TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PIG + FOX == LOVE'''.splitlines()

cProfile.run('test(faster_solve)')  # only take ~2 seconds
cProfile.run('test(solve)')  # take ~12.6 seconds
