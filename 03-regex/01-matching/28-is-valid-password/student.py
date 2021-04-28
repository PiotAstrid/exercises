# Write your code here
import re
def is_valid_password(string):
    yes = [
        r'.{8,}',
        r'[0-9]',
        r'[a-z]',
        r'[A-Z]',
        r'[-+/.*@]',
]
    no = [
        r'(.)\1{2}',
        r'(.)(.*\1){3}'
    ]
    return all(re.search(regex, string) for regex in yes) and not any(re.search(regex, string) for regex in no)