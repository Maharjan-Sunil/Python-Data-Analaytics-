thisdict = {
    'a': [{
        "brand": "Ford",
        "model": "Mustang",
        "number": 14
    },
        {
        "brand": "Ford",
            "model": "Mustang",
            "number": 16
    }
    ],
    'b': [{
        "brand": "Ford",
        "model": "Mustang",
        "number": 1964
    }]
}

sum_by_key = []
for key, value in thisdict.items():
  total = sum([data['number'] for data in value])
  sum_by_key.append((key, total))

for key, data in sum_by_key:
    print(f'key: {key}, value: {data}')
