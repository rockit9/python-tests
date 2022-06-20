# Write a function which return list of even numbers
# Example: 
# arr = [1,2,3,4,5,"Jack", "John", "Peter"]
# result = [2,4]



# Using 'requests' lib make a GET request and print response's body
# Site for testing - https://randomuser.me/
from pprint import pprint

arr = [1,2,3,4,5,"Jack", "John", "Peter"]


def even_nbrs(array):
    """
    The function filters passed list and saves only even numbers.
    :param array: list List may include any data types
    :return: list List includes only even numbers
    """
    result = []

    for i in array:
        if isinstance(i, int):
            if i % 2 == 0:
                result.append(i)

    return result

# print(even_nbrs(arr))


# import requests
#
# URL = 'https://randomuser.me/api/?format=json'
#
# r = requests.get(url=URL)
#
# data = r.json()
# # pprint(r.content)
# pprint(data)


import requests

URL = 'https://randomuser.me/api/?format=json'

r = requests.get(url=URL)

data = r.json()

print(data)