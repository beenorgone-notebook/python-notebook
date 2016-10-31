# ou need to execute a reduction function
# (e.g., sum() , min() , max()), but first need to transform or filter the data.

# SOLUTION: Use generator-expression.

# Determine if any .py files exist in a directory
import os

dirname = '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/py-recipes'
files = os.listdir(dirname)

if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)

print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
