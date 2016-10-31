# https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming
import functools
import operator
import random

# 1. Use `map` and `reduce` instead of iterate over lists
# ========================================================

# Example I:
# ---------
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

# Iterate
# this algorithm can potentially assign the same secret code name to
# multiple secret agents. Hopefully, this won’t be a source of
# confusion during the secret mission.
for i in range(len(names)):
    names[i] = random.choice(code_names)

# `map` calls can be twice as fast as equivalent `for` loops, and
# list comprehensions are often faster than `map` calls.
# functional style with map():
secret_names = tuple(map(lambda x: random.choice(
    code_names), names))


# Example II:
# ----------
# iterate
for i in range(len(names)):
    names[i] = hash(names[i])

# functional style with map():
secret_names = tuple(map(hash, names))


# Example III:
# -----------
sentences = ['Mary read a story to Sam and Isla.',
             'Isla cuddled Sam.',
             'Sam chortled.']

sam_count = 0
for sentence in sentences:
    sam_count += sentence.count('Sam')

# functional style with reduce():
sam_count = functools.reduce(lambda a, x: a + x.count('Sam'), sentences, 0)

# Example IV:
# ----------
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

# functional style with map(), reduce() and filter():
heights = tuple(map(lambda x: x['height'], filter(
    lambda x: 'height' in x, people)))

if len(heights) > 0:
    average_height = functools.reduce(operator.add, heights) / len(heights)
    print(average_height)

# 2. Write declaratively, not imperatively
# ========================================

# Example V:
# ----------
time = 5
car_positions = [1, 1, 1]

while time:
    # decrease time
    time -= 1

    print('')
    for i in range(len(car_positions)):
        # move car
        if random.random() > 0.3:
            car_positions[i] += 1

        # draw car
        print('-' * car_positions[i])


# Use functions:
def move_cars():
    for i, _ in enumerate(car_positions):
        if random.random() > 0.3:
            car_positions[i] += 1


def draw_car(car_position):
    print('-' * car_position)


def run_step_of_race():
    global time
    time -= 1
    move_cars()


def draw():
    print('')
    for car_position in car_positions:
        draw_car(car_position)

time = 5
car_positions = [1, 1, 1]

while time:
    run_step_of_race()
    draw()


# functional version:
def move_cars(car_positions):
    return map(lambda x: x + 1 if random.random() > 0.3 else x, car_positions)


def output_car(car_position):
    return '-' * car_position


def run_step_of_race(state):
    return {'time': state['time'] - 1,
            'car_positions': move_cars(state['car_positions'])}


def draw(state):
    print('')
    print('\n'.join(map(output_car, state['car_positions'])))


def race(state):
    draw(state)
    if state['time']:
        race(run_step_of_race(state))

race({'time': 5,
      'car_positions': [1, 1, 1]})


# Example VI:
# ----------
def zero(s):
    if s[0] == "0":
        return s[1:]


def one(s):
    if s[0] == "1":
        return s[1:]


# Imagine a function called rule_sequence(). It takes a string and
# a list of rule functions of the form of zero() and one().
# It calls the first rule on the string. Unless None is returned,
# it takes the return value and calls the second rule on it.
# Unless None is returned, it takes the return value and
# calls the third rule on it. And so forth.
# If any rule returns None, rule_sequence() stops and returns None.
# Otherwise, it returns the return value of the final rule.


# Imperative version:
def rule_sequence(s, rules):
    for rule in rules:
        s = rule(s)
        if s == None:
            break
    return s


# Declarative version with recursion:
def rule_sequence(s, rules):
    if s == None or not rules:
        return s
    else:
        return rule_sequence(rules[0](s), rules[1:])

# More examples: search_phonebook (hackerrank)

# 3. Use pipelines
# ================
# The loop below performs transformations on dictionaries that hold the name, incorrect country of origin and active status of some bands.
# Imperative version:
bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]


def format_bands(bands):
    for band in bands:
        band['country'] = 'Canada'
        band['name'] = band['name'].replace('.', '')
        band['name'] = band['name'].title()

format_bands(bands)


# functional version:
def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d


def set_canada_as_country(band):
    return assoc(band, 'country', 'Canada')


def strip_punctuation_from_name(band):
    return assoc(band, 'name', band['name'].replace('.', ''))


def capitalize_names(band):
    return assoc(band, 'name', band['name'].title())


# replace() and title() do not mutate the strings they operate on.
# This is because strings are immutable in Python.
# Every string methods are functional.


def pipeline_each(data, fns):
    return functools.reduce(lambda a, x: map(x, a), fns, data)

print(pipeline_each(bands, [set_canada_as_country,
                            strip_punctuation_from_name,
                            capitalize_names]))


# 4. Functional with higher order function and lambda function:
# ============================================================

# A higher order function takes a function as an argument, or returns a
# function.
bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]


def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d


def call(fn, key):
    def apply_fn(record):
        return assoc(record, key, fn(record.get(key)))
    return apply_fn


def pipeline_each(data, fns):
    return list(functools.reduce(lambda a, x: map(x, a), fns, data))


set_canada_as_country = call(lambda x: 'Canada', 'country')
strip_punctuation_from_name = call(lambda x: x.replace('.', ''), 'name')
capitalize_names = call(str.title, 'name')

print(pipeline_each(bands, [call(lambda x: 'Canada', 'country'),
                            call(lambda x: x.replace('.', ''), 'name'),
                            call(str.title, 'name')]))


# Example VII: pluck() takes a list of keys to extract from each record.
# --------------------------------------------------------------
def pluck(keys):
    '''takes a list of keys to extract from each record'''
    def _pluck(record):
        return functools.reduce(lambda a, x: assoc(a, x, record[x]),
                                keys, {})
    return _pluck
