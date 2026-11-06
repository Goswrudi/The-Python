
import random
import string


def chars():
    chars = string.ascii_letters + string.digits + string.punctuation
    user_chars = ''.join(random.choices (chars , k=15))
    return user_chars


def nums1():
    user_num = random.randint(-20, 100)
    return str(user_num)


def password():
    password = chars() + nums1()
    return password

print(f'Genrated password is : {password()}')