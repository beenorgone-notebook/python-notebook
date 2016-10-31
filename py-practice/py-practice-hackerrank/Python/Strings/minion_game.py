# The Minion Game: https://www.hackerrank.com/challenges/the-minion-game

# Both players are given the same string, S.
# Both players have to make substrings using
# the letters of the string.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made
# all possible substrings.

# Scoring:
# A player gets +1 point for each occurrence
# of the substring in the string.

# Your task is to determine the winner of the game and their score.


VOWELS = 'AEIOU'
KEVIN_SCORE = 0
STUART_SCORE = 0
S = 'BANANA'

# SOLUTION: take all possible substrings, split them into two sets
# according to starting letter, then sum elements in sets.

for i in range(len(S)):
    if S[i] in VOWELS:
        KEVIN_SCORE += (len(S) - i)
    else:
        STUART_SCORE += (len(S) - i)

if KEVIN_SCORE > STUART_SCORE:
    print('Kevin', KEVIN_SCORE)
elif KEVIN_SCORE < STUART_SCORE:
    print('Stuart', STUART_SCORE)
else:
    print('Draw')
