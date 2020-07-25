import pickle as pk

list = [(1,2,3), 'manish', [12,12,3]]

# with open('./data.pkl', 'wb') as f:
#     pk.dump(list,f)
#     print('completed dumping via pickle')

with open('./data.pkl', 'rb') as f:
    response = pk.load(f)
    print(response)

