'''
A portfolio is a grouping of financial assets, such as stocks, bonds, or fixed-income securities. Each portfolio is managed by a Portfolio Manager who is in charge of sending portfolio orders to a Trader.

A Trader receives orders of varying sizes from different portfolios to buy a quantity of a security on the market. They then identify a Seller that is willing to sell units of the desired security.

In a best-case scenario, the Seller is selling enough of the security to fulfill all of the portfolio orders for the security; however, if that is not the case, the Trader must buy as much of the security as possible and fairly allocate it amongst the portfolios.

FIXED-INCOME SECURITY

A fixed-income security has the following properties:

- minimum_trade_size - The smallest number of units that can be traded with this security.
- `increment` - The number of units the trade can be incremented with.
- `tradeable_amount` = (`minimum_trade_size`) + (`increment` * n), where n is a non-negative integer.
- `avail_units` - The number of units of the security that are available for purchase on the market.

FIXED-INCOME TRADE ORDERS

A fixed-income Trader has the following information:

- `order` - The number of units of the fixed-income security that a single portfolio wants to buy.
- `total_order` - The total (sum) number of units made up of all the underlying `order`s.

DEFINING A PROPORTIONAL ALLOCATION

If there are not enough `avail_units` to fulfill all of the portfolio orders, we must find the proportional allocation for each portfolio's order of the `avail_units` on the market.

We get a portfolio's `proportional_allocation` with this expression:

proportional_allocation = order / total_order * avail_units

HOW DO WE FAIRLY ALLOCATE UNITS?

Iterate through every underlying `order` from smallest to largest (if two portfolios order the same number of units, then sort them lexicographically by ascending ID) and apply the following process:

- If the portfolio's `proportional_allocation` is less than the `minimum_trade_size`, check if `proportional_allocation` is greater than `minimum_trade_size / 2`.
    - If false, do not allocate anything.
    - If true, attempt to allocate the `minimum_trade_size` within the defined rules.
        - If this fails; allocate nothing.
- If the portfolio's `proportional_allocation` is greater than or equal to `minimum_trade_size`:
    - If the `proportional_allocation` is larger than or equal to the `order`, allocate the `order`.
    - If the `proportional_allocation` is not a `tradeable_amount`, round it down to the closest `tradeable_amount` that you can allocate within the defined rules.
        - If you fail to find a `tradeable_amount` that satisfies the rules, allocate nothing.
- After allocating units (including the case when you allocate nothing) to a portfolio, perform the following steps to ensure that as much of the available security is purchased as is possible:
    - Recalculate the `total_order` based on the orders from the remaining portfolios (i.e., those whose orders haven't yet been allocated).
    - Subtract the quantity of units that were just allocated to an order and recalculate `avail_units`.
    - Recalculate the `proportional_allocation` of each portfolio awaiting allocation based on the remaining `avail_units`.

RULES THAT ALWAYS HOLD

- A portfolio manager only orders tradeable amounts from the Trader.
- Each portfolio has to issue its own trade, hence the quantity allocated to each portfolio must be a `tradeable_amount`.
- An untradeable amount is a value that cannot be represented as a tradeable amount. Note that an exception of 0 is allowed (meaning that 0 is a tradeable amount). You must try to never leave a portfolio with leftover units (`order - allocated`) that can't be traded on the market (i.e., an untradeable amount).

Given the basic information for a fixed-income security and a list of portfolio orders, find the `proportional_allocation` for each portfolio using the rules and processes defined above. Then, print each `portfolio_identifier` along with the amount of the security allocated to it as two space-separated values on a new line. Order your output alphabetically by `portfolio_identifier`.

INPUT FORMAT

The first line contains an integer, T, denoting the number of portfolios hoping to place orders.

The second line contains three space-separated integers denoting the respective values for the `minimum_trade_size`, `increment`, and `avail_units` for the fixed-income security.

Each of the T subsequent lines defines a portfolio order as two space-separated values; the first value is a string denoting the `portfolio_identifier`, and the second value is an integer denoting the `order`.

CONSTRAINTS

- 0 < T < 1000
- 0 < increment < minimum_trade_size < avail_units
- order = minimum_trade_size + increment * n , for some non-negative integer, n
- minimum_trade_size * number of portfolios < avail_units

OUTPUT FORMAT

Print T lines where each line contains two space-separated values: a `portfolio_identifier` followed by the number of units allocated to the portfolio. Your output must be ordered alphabetically by `portfolio_identifier`.

SAMPLE INPUT

2
10 2 40
p1 16
p2 134

SAMPLE OUTPUT

p1 0
p2 40

EXPLANATION

First, we have the following information about our fixed-income security:

- minimum_trade_size = 10
- increment = 2
- avail_units = 40

Next, we have T = 2 portfolio orders:

1. p1's order = 16.
2. p2's order = 134.

We can calculate total_order = 16 + 134 = 150

p1_proportinal_allocation = 16 / 150 * 40 = 4.26

Because `p1_proportinal_allocation < minimum_trade_size / 2 = 5`, nothing is allocated to . Therefore, all 40 `avail_units`  are allocated to p2.
'''

import operator
import re

def closest_tradeable(num, minimum, increment):
    if num < minimum:
        return None
    else:
        return num - ((num - minimum) % increment)

def tradeable(num, minimum, increment):
    return num - minimum >= 0 and (num - minimum) % increment == 0

def allocate_order(order, avail_units, total_order, minimum_trade_size, increment):
    prop_allo = order / total_order * avail_units
    if prop_allo < minimum_trade_size:
        test_prop_allo = prop_allo <= minimum_trade_size / 2
        test_order = order < minimum_trade_size
        if test_prop_allo or test_order:
            return 0
        elif tradeable(order - minimum_trade_size, minimum_trade_size, increment):
            return minimum_trade_size
        else:
            return 0
    elif prop_allo >= order:
        if tradeable(order, minimum_trade_size, increment):
            return order
        else:
            return 0
    elif tradeable(prop_allo, minimum_trade_size, increment):
        if tradeable(order - prop_allo, minimum_trade_size, increment):
            return int(prop_allo)
        else:
            return 0
    else:
        to_trade = closest_tradeable(prop_allo, minimum_trade_size, increment)
        if to_trade and tradeable(order - to_trade, minimum_trade_size, increment):
            return int(to_trade)
        else:
            return 0


def sec_allo(orders_log, avail_units, minimum_trade_size, increment):
    if not 0 < increment < minimum_trade_size < avail_units:
        raise ValueError('Your input is invalid.')
    elif not minimum_trade_size * len(orders_log) < avail_units:
        raise ValueError("Avaiable units aren't enough to start allocate.")
    else:
        raw_allocation_log = []
        total_order = sum(o[1] for o in orders_log)
        for o in orders_log:
            o_allocated = allocate_order(o[1], avail_units, total_order, minimum_trade_size, increment)
            raw_allocation_log.append((o[0], o_allocated))
            avail_units -= o_allocated
            total_order -= o[1]
        allocation_log = sorted(raw_allocation_log, key=operator.itemgetter(0))
        for a in allocation_log:
            print('{} {}'.format(a[0], a[1]))

def get_nums(a_string):
    return re.findall(r'\d+' ,a_string)

T = int(input().strip())

minimum_trade_size, increment, avail_units = map(int, get_nums(input().strip()))

def build_orders_log(T):
    raw_orders_log = []
    for i in range(T):
        portfolio = input().strip()
        if portfolio:
            nums = get_nums(portfolio)
            portfolio_id = 'p' + nums[0]
            raw_orders_log.append((portfolio_id, int(nums[1])))

    #sort order based on value
    orders_log = sorted(raw_orders_log, key=operator.itemgetter(1, 0))
    return orders_log

sec_allo(build_orders_log(T), avail_units, minimum_trade_size, increment)
