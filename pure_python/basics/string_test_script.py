import string
import random
import unicodedata

# string = input('Enter some string with few words\n')
# print(string)
# generated_array = string.split()
# print(generated_array)


x = ''

print(bool(x))


def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


x = random_string(10)
y = u'Málaga'


def remove_diacritical_from_string(input_string: str):
    norm = unicodedata.normalize('NFD', input_string)
    return ''.join([x for x in norm if not unicodedata.combining(x)])


print(remove_diacritical_from_string(x))
print(remove_diacritical_from_string(y))
