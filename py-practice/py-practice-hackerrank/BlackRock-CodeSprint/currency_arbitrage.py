'''
An arbitrage is the simultaneous purchase and sale of an asset in order to profit from a difference in the price. This type of trade exploits price differences between similar or identical financial instruments, either on different markets or in different forms.

You are a currency trader looking for arbitrage opportunities in the currency market using these three quotes:

- The cost of USD per EUR (USD/EUR) for converting.
- The cost of EUR per GBP (EUR/GBP) for converting.
- The cost of GBP per USD (GBP/USD) for converting.

You must use your USD to buy EUR, then use your EUR to buy GBP, and finally use your GBP to buy USD, resulting in some sort of profit or loss. Reverse trading is not allowed, so you are limited to the exchanges in the direction shown above. For example, you can convert USD -> EUR, which means selling US Dollars and buying Euros; you cannot invert the fraction to sell Euros and buy US Dollars.

Given 100.000 USD for each trade, calculate the arbitrage profit truncated to whole dollars (USD); otherwise, print 0 if there is no arbitrage opportunity.

INPUT FORMAT

The first line contains a single integer, N, denoting the number of quotes.
Each of the N subsequent lines describes a quote in the form of three space-separated integers:

- The first quote is a real number denoting the price quote for USD -> EUR (USD/EUR).
- The second quote is a real number denoting the price quote for EUR -> GBP (EUR/GBP).
- The third quote is a real number denoting the price quote for GBP -> USD (GBP/USD).

CONSTRAINTS

1 <= N <= 1000
0.001 < quotes <= 1000

OUTPUT FORMAT

For each trade, print a single line denoting the arbitrage profit for that trade; if no arbitrage opportunity exists, print 0. You should have a total of N lines of output.

SAMPLE INPUT

2
1.1837 1.3829 0.6102
1.1234 1.2134 1.

SAMPLE OUTPUT

114
0

EXPLANATION

There are N test cases:

1. You use your 1000.000 USD to buy 84.480,8651 EUR. You then use your 84.480,8651 EUR to buy 61.089,6414 GBP. Finally, you use your 61.089,6414 GBP to buy 100.114,1288 USD. Because we started out with 100.000 USD, our net profit in whole dollars is 114 USD. There is no arbitrage opportunity here (the conversion would end up losing money), so we print.

2. There is no arbitrage opportunity here (the conversion would end up losing money), so we print 0.
'''

import re

def get_float_nums(a_string):
    return re.findall(r'\d+\.\d*' ,a_string)

def arbitrage_profit(quotes_input, fund=100000):
    usd_eu, eu_gbp, gbp_usd = tuple(float(i) for i in get_float_nums(quotes_input))
    revenue = fund / usd_eu / eu_gbp / gbp_usd
    if revenue > fund:
        print(int(revenue - fund))
    else:
        print(0)

n = int(input().strip())

if n < 1 or n > 1000:
    raise ValueError('n should lower than 1000 and bigger than 1')
else:
    while n:
        arbitrage_profit(input().strip())
        n -= 1
