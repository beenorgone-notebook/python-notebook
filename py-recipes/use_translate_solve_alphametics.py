def alphametics(puzzle):
    '''
    Solve alphametics puzzle:
    HAWAII + IDAHO + IOWA + OHIO == STATES
    510199 + 98153 + 9301 + 3593 == 621246
    The letters spell out actual words, but if you replace each letter
    with a digit from 0–9, it also “spells” an arithmetic equation.
    The trick is to figure out which letter maps to each digit.
    All the occurrences of each letter must map to the same digit,
    no digit can be repeated, and no “word” can start with the digit 0.
    '''
    from re import findall
    from itertools import permutations
    # Get all characters in puzzle
    words = findall('[A-Z]+', puzzle.upper())
    unique_chars = set(''.join(words))
    # Check if characters in use is less than 10 or not
    number_of_chars = len(unique_chars)
    number_of_digits = 10
    assert number_of_chars <= number_of_digits, 'Too many letters.'
    # get 1st character of each "word"
    first_letters = {w[0] for w in words}
    # Create sorted_chars in which first_chars is in head part.
    sorted_chars = ''.join(first_letters) + \
        ''.join(unique_chars - first_letters)
    n = len(first_letters)
    # Loop throw permutations of 10 digits 0-9 and
    # create an arithmetic equation. Check if equation is True.
    chars = tuple(ord(c) for c in sorted_chars)
    digits = tuple(ord(c) for c in '0123456789')
    # We need ord() because translate() only works with ordinals.
    zero = digits[0]
    for guess in permutations(digits, number_of_chars):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(chars, guess)))
            if eval(equation):
                return equation

if __name__ == '__main__':
    import sys
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)

puzzles = ['HAWAII + IDAHO + IOWA + OHIO == STATES',
           'SEND + MORE == MONEY', 'PIG + FOX == LOVE',
           'LEO + CRIS == INVISIBLES']

for p in puzzles:
    print(alphametics(p))
