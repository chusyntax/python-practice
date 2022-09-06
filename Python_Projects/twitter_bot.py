def pwned_api_check(password):  # Checks if password exists in API response

    # Converts given password to SHA1 standards
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # The tail is everything after first 5 characters
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(first5_char, tail)
    return get_password_leaks_count(response, tail)
