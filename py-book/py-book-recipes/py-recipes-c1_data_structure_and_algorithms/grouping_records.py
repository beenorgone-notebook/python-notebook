# You have a sequence of dictionaries or instances and you want to
# iterate over the data in groups based on the value of a particular
# field, such as date. SOLUTION: itertools.groupby()

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]


# You want to iterate over the data in chunks grouped by date.
# An important preliminary step is sorting the data according to
# the field of interest. Since groupby() only examines consecutive
# items, failing to sort first won’t group the records as you want.

import collections.defaultdict as defaultdict
import itertools.groupby as groupby

date_key = lambda x: x['date']
rows_sorted = sorted(rows, key=date_key)
rows_grouped_by_date = groupby(rows_sorted, key=date_key)

for date, addresses in rows_grouped_by_date:
    print(date)
    for a in addresses:
        print('   {}'.format(a))

'''
07/01/2012
   {'date': '07/01/2012', 'address': '5412 N CLARK'}
   {'date': '07/01/2012', 'address': '4801 N BROADWAY'}
07/02/2012
   {'date': '07/02/2012', 'address': '5800 E 58TH'}
   {'date': '07/02/2012', 'address': '5645 N RAVENSWOOD'}
   {'date': '07/02/2012', 'address': '1060 W ADDISON'}
07/03/2012
   {'date': '07/03/2012', 'address': '2122 N CLARK'}
07/04/2012
   {'date': '07/04/2012', 'address': '5148 N CLARK'}
   {'date': '07/04/2012', 'address': '1039 W GRANVILLE'}
'''


# If your goal is to simply group the data together by dates into
# a large data structure that allows random access, you may have
# better luck using `defaultdict()` to build a multidict
rows_by_date = defaultdict(list)

for row in rows:
    rows_by_date[row['date']].append(row)
print(rows_by_date)

'''
defaultdict(<class 'list'>, {'07/04/2012': [{'date': '07/04/2012', 'address': '5148 N CLARK'}, {'date': '07/04/2012', 'address': '1039 W GRANVILLE'}], '07/03/2012': [{'date': '07/03/2012', 'address': '2122 N CLARK'}], '07/02/2012': [{'date': '07/02/2012', 'address': '5800 E 58TH'}, {'date': '07/02/2012', 'address': '5645 N RAVENSWOOD'}, {'date': '07/02/2012', 'address': '1060 W ADDISON'}], '07/01/2012': [{'date': '07/01/2012', 'address': '5412 N CLARK'}, {'date': '07/01/2012', 'address': '4801 N BROADWAY'}]})
'''
