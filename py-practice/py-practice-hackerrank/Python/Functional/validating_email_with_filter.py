# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter

import re

email_pattern = '^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{,3}$'
email_regex = re.compile(email_pattern)
N = int(input().strip())
emails = tuple(input().strip() for _ in range(N))
valid_emails = filter(email_regex.match, emails)

print(sorted(valid_emails))
