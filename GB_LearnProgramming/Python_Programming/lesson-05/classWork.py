import json

dict_tmp = {
    1: 123,
    2: 123.456,
    3: "new",
    4: True,
    5: None,
    6: [1,2,3],
    7: {1: '2'}
    }

with open('json1.json', 'w') as file_write:
    json.dump(dict_tmp, file_write, indent=1)
    
with open('json1.json', 'r') as file_read:
    dict_new = json.load(file_read)
