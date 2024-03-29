''' Javascript Object Notation '''
import json
from urllib.request import urlopen

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)

print(data)
print(type(data))

for person in data['people']:
    print(person['name'])
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)

with open('states.json', 'r') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)