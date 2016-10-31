'''
https://www.hackerrank.com/contests/blackrock-codesprint/challenges/suggest-better-spending-rates
'''

def total_income_calc(p, r, S):
    total_income = 0
    for t in range(1, len(S)+1):
        income_t = p * S[t-1] * ((1 + r / 100) ** t) / (100 ** t)
        if (t-1):
            for i in range(t-1):
                income_t = income_t * (100 - S[i])
        total_income += income_t
    return total_income

def get_and_test_input():

    pass

def spending_rates_combinations(S, threshold, adjust_budget=0):
    if len(S) == 1:
        yield [S[0] + adjust_budget]
    else:
        for i in range((-threshold), threshold + 1):
            if abs(adjust_budget - i) / (len(S) - 1) > threshold:
                continue
            else:
                a = [S[0] + i]
                for e in list(spending_rates_combinations(S[1:], threshold, adjust_budget-i)):
                    yield a + e
'''
print(list(spending_rates_combinations([37], 1, 0)))
print(list(spending_rates_combinations([42, 37], 1, 0)))
print(list(spending_rates_combinations([29, 42, 37, 100], 1, 0)))
print(list(spending_rates_combinations([29, 42, 37, 10], 3, 0)), )
'''
