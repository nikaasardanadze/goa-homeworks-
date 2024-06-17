# student = {
#     "name": "nikoloz sardanadze",
#     "age": 20,
#     "height": "175cm",
#     "studies at": "goa"
# }

# print(student)


student = {
    "name": "nikoloz sardanadze",
    "age": 20,
    "height": "175cm",
    "studies at": "goa"
}

result = []

for key, value in student.items():
    result.append(f'{key}: {value}')

print(result)
