def build_phonebook(n):
    def get_input():
        return input().strip().split(' ')
    if not 1 <= n <= 10 ** 5:
        raise ValueError('n should be between 1 and 10^5')
    else:
        return {get_input()[0]: get_input()[1] for _ in range(n)}


def search_phonebook(query_value, phonebook):
    return phonebook.get(query_value, None)

n = int(input().strip())  # number of contacts
phonebook = build_phonebook(n)
query_number = 1
test_query_number = 1 <= query_number <= 10 ** 5

while test_query_number:
    q = input().strip()
    if q:
        if search_phonebook(q, phonebook):
            print('{}={}'.format(q, phonebook[q]))
        else:
            print('Not found')
    else:
        break
    query_number += 1


# functional version:
def build_phonebook(n):
    def get_contact():
        return input().strip().split(' ')

    if not 1 <= n <= pow(10, 5):
        raise ValueError('n should be between 1 and 10^5')
    else:
        return {get_contact()[0]: get_contact()[1] for _ in range(n)}


def run_step(state):
    return {'query_number': state['query_number'] + 1,
    'test_query_number': 1 <= state['query_number'] <= pow(10, 5),
    'query_value': input().strip()}


def search_result(query_value, phonebook):
    if query_value:
        if phonebook.get(query_value, None):
            return 'Phone number of {} is {}'.format(query_value, phonebook[query_value])
        else:
            return 'Not found'
    else:
        raise 'No query'


def querying(phonebook, state):
    if state['test_query_number']:
        search_result(state['query_value'], phonebook)
        querying(phonebook, run_step(state))

start_state = {'query_number': 1, 'test_query_number': True)}
querying(build_phonebook(int(input().strip())), run_step(start_state))
