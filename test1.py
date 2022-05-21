# Write a function which return list of even numbers
# Example: 
# arr = [1,2,3,4,5,"Jack", "John", "Peter"]
# result = [2,4]



# Using 'requests' lib make a GET request and print response's body
# Site for testing - https://randomuser.me/


arr = [1,2,3,4,5,"Jack", "John", "Peter"]


def even_nbrs(x):
    result = []

    for i in x:
        if isinstance(i, int):
            if i % 2 == 0:
                result.append(i)

    return result

print(even_nbrs(arr))

