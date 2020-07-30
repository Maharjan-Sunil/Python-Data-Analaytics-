import json
def read_json_file():
    with open('data.json') as f:
        response =  json.loads(f.read())
        print(response['name'])

# def dump_json_file(response):
#     with open('data.json','w') as f:
#         json.dump(response,f)
#         print('finish ...')

# response = {
#     'name' :'Manish',
#     'age' : 15
# }


#dump_json_file(response)
read_json_file()