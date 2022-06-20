# Write a function which return list of even numbers
# Example: 
# arr = [1,2,3,4,5,"Jack", "John", "Peter"]
# result = [2,4]



# Using 'requests' lib make a GET request and print response's body
# Site for testing - https://randomuser.me/
from pprint import pprint

# arr = [1,2,3,4,5,"Jack", "John", "Peter"]


# def even_nbrs(array):
#     """
#     The function filters passed list and saves only even numbers.
#     :param array: list List may include any data types
#     :return: list List includes only even numbers
#     """
#     result = []
#
#     for i in array:
#         if isinstance(i, int):
#             if i % 2 == 0:
#                 result.append(i)
#
#     return result

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


# import requests
#
# URL = 'https://randomuser.me/api/?format=json'
#
# r = requests.get(url=URL)
#
# data = r.json()
#
# print(data)


# import requests
#
# URL = 'https://gorest.co.in/public/v2/comments'
#
# headers = {
#     'Authorization': 'Bearer 54f310c260611d515ac709f5140d8300f08fce58e42dfac4cb6bf0df4f5eef57'
# }
#
# body = {
#         "id": 1276,
#         "post_id": 1269,
#         "name": "lkldak. Kin Reddy",
#         "email": "sen_kin_reddy@pfannerstill-harber.biz",
#         "body": "Sed consequatur doloremque. Doloribus harum repudiandae. Soluta quis aperiam."
# }
#
# r = requests.post(url=URL, headers=headers, params=body)
#
# print(r.status_code)
#
# print(r.json())


# import requests
#
# URL = 'https://gorest.co.in/public/v2/comments/1276'
#
# header = {
#         'Authorization': 'Bearer 54f310c260611d515ac709f5140d8300f08fce58e42dfac4cb6bf0df4f5eef57'
# }
#
# body = {
#         'age': '27.02.1995'
# }
#
# r = requests.put(url=URL, data=body, headers=header)
#
# print(r.status_code)
#
# print(r.json())



# import requests
#
# URL = 'https://gorest.co.in/public/v2/comments/1278'
#
# header = {
#         'Authorization': 'Bearer 54f310c260611d515ac709f5140d8300f08fce58e42dfac4cb6bf0df4f5eef57'
# }
#
# body = {
#         "name": "lkldak. Kin Reddy"
# }
#
# r = requests.delete(url=URL, data=body, headers=header)
#
# print(r.status_code)



# new branch
import requests

URL = "https://gorest.co.in/public/v2/posts"

r = requests.get(url=URL)

data = r.json()

print(data)