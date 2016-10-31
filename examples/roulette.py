'''
Available Bets in Roulette

Roulette Table layout:
http://itmaybeahack.com/book/oodesign-python-2.1/html/_images/Roulette2.png

A “straight bet” is a bet on a single number.
There are 38 possible bets, and they pay odds of 35 to 1.
Each bin on the wheel pays one of the straight bets.

A “split bet” is a bet on an adjacent pair of numbers. It pays 17:1.
The table layout has the numbers arranged sequentially in
three columns and twelve rows.
Adjacent numbers are in the same row or column.
The number 5 is adjacent to 4, 6, 2, 8;
the number 1 is adjacent to 2 and 4.
There are 114 of these split bet combinations.
Each bin on the wheel pays from two to four of
the available split bets. Any of two bins can make a split bet a winner.

A “street bet” includes the three numbers in a single row,
which pays 11:1.
There are twelve of these bets on the table.
A single bin selects one street bet;
any of three bins make a street bet a winner.

A square of four numbers is called a “corner bet” and pays 8:1. There are 72 of these bets available.

At one end of the layout, it is possible to place a bet on
the Five numbers 0, 00, 1, 2 and 3. This pays 6:1.
It is the only combination bet that includes 0 or 00.

A “line bet” is a six number block, which pays 5:1.
It is essentially two adjacent street bets.
There are 11 such combinations.

"Outside" bets

Any of the three 12-number ranges (1-12, 13-24, 25-36) pays 2:1.
There are just three of these bets.

The layout offers the three 12-number columns at 2:1 odds.
All of the numbers in a given column have
the same remainder when divided by three.
Column 1 contains 1, 4, 7, etc., all of which have a remainder of 1
when divided by 3.

There are two 18-number ranges:
1-18 is called low, 19-36 is called high.
These are called even money bets because they pay at 1:1 odds.

The individual numbers are colored red or black in an arbitrary pattern.
Note that 0 and 00 are colored green.
The bets on red or black are even money bets, which pay at 1:1 odds.

The numbers (other than 0 and 00) are also either even or odd.
These bets are also even money bets.
'''
