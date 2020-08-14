from collections import namedtuple, defaultdict, counter
# dict_data = {
#     "name":"manish",
#     "age":15
# }
dict_data = defaultdict(lambda: "kalimati")

print(dict_data["address"])

data = namedtuple("data_name", ['name', 'address'])

obj = data("manish", "kalimati")
print(obj.name)
