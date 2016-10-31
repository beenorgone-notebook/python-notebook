'''Find solutions to alphametic equations.

>>> alphametics.solve('SEND + MORE == MONEY')
'9567 + 1085 == 10652'
'''

import re
import itertools

def solve(puzzle):
    '''Find solutions to alphametic equations.

    >>> solve('SEND + MORE == MONEY')
    9567 + 1085 == 10652
    '''
    words = re.findall('[A-Z]+', puzzle.upper()) # characters to be substituted
    unique_characters = set(''.join(words)) # find all unique characters
    assert len(unique_characters) <= 10, 'Too many letters' # there are only ten possible digits
    first_letters = {word[0] for word in words} # first letters of each of word
    n = len(first_letters) # chars[:n] cannot be assigned zero
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

if __name__ == '__main__':
    import sys
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)

for alphametic in [
        'SEND + MORE == MONEY',
        'VIOLIN * 2 + VIOLA == TRIO + SONATA',
        'SEND + A + TAD + MORE == MONEY',
        'ZEROES + ONES == BINARY',
        'DCLIZ + DLXVI == MCCXXV',
        'COUPLE + COUPLE == QUARTET',
        'FISH + N + CHIPS == SUPPER',
        'SATURN + URANUS + NEPTUNE + PLUTO == PLANETS',
        'EARTH + AIR + FIRE + WATER == NATURE',
        ('AN + ACCELERATING + INFERENTIAL + ENGINEERING + TALE + ' +
            'ELITE + GRANT + FEE + ET + CETERA == ARTIFICIAL + INTELLIGENCE'),
        'TWO * TWO == SQUARE',
        'HIP * HIP == HURRAY',
        'PI * R ** 2 == AREA',
        'NORTH / SOUTH == EAST / WEST',
        'NAUGHT ** 2 == ZERO ** 3',
        'I + THINK + IT + BE + THINE == INDEED',
        'DO + YOU + FEEL == LUCKY',
        'NOW + WE + KNOW + THE == TRUTH',
        'SORRY + TO + BE + A + PARTY == POOPER',
        'SORRY + TO + BUST + YOUR == BUBBLE',
        'STEEL + BELTED == RADIALS',
        'ABRA + CADABRA + ABRA + CADABRA == HOUDINI',
        'I + GUESS + THE + TRUTH == HURTS',
        'LETS + CUT + TO + THE == CHASE',
        'THATS + THE + THEORY == ANYWAY',
        '1/(2*X-Y) == 1',
    ]:
    print(alphametic, end='\n')
    print(solve(alphametic), end='\n')

# Copyright (c) 2009, Raymond Hettinger, All rights reserved.
# Ported to Python 3 and modified by Mark Pilgrim
# original: http://code.activestate.com/recipes/576615/
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
