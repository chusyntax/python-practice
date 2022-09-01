# Checks if password has ever been hacked

import requests  # Allows us to make requests like a browser
import hashlib  # Gives ability to SHA1 hash passwords
import sys

# Use K-anonymity ~ Allows someone to recieve info about us yet still not know who we are
# K-anonymity uses the first 5 charcters of the hash of your password

# Hash function ~ A function that generates value of fixed length for each input that it gets
# They are one way
# It is idempotent ~ The same input will always give the same output


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    # The hash/password we'll be searching
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching{res.status_code} check api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':')
              for line in hashes.text.splitlines())  # Converts hash into tuple
    for h, count in hashes:  # Do  this as we have a tuple, so now breaking tuple into 2 values
        if h == hash_to_check:  # Checks if tails are the same
            return count  # Basically return how many times password got leaked
    return 0


def pwned_api_check(password):  # Checks if password exists in API response

    # Converts given password to SHA1 standards
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # The tail is everything after first 5 characters
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(first5_char, tail)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f'{password} was found {count} times. You should probably not use it for better security!')
        else:
            print(f'{password} was not found. You can use it!')
    return 'Done!'


# Done so that it will accept any amount of arguments after the first one
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
