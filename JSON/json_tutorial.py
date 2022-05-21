import json

# Python object/dict
person = {"name": "John", "age": 30, "city": "New York", "state": "NY", "country": "USA", "zip": "10001", "phone": "123-456-7890","has_kids": True, "children": ["Mary", "Mark", "Bob", "Linda"]}

################ Serialization (Python to JSON) ##################


# personJSON = json.dumps(person, indent=4, sort_keys=true) 

### Notes
# Using indent=4 to make the JSON more readable
# Using separators not reccomended for JSON, default is ',' and ':'
# Using sort_keys=true to sort the keys in the JSON in alphabetical order

# print(personJSON)

# Dumping to file

# Here we use dump instead of dumps because we are writing to a file not a string

# with open("person.json", "w") as f:
#     json.dump(person, f, indent=4, sort_keys=true)



# Serializing from a class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_person = Person("John", 30)
# my_personJSON = json.dumps(my_person, indent=4, sort_keys=True) # TypeError: <__main__.Person object at 0x7f8b8b8b9c10> is not JSON serializable

# Fixing the above error

# Method 1: Create a custom encoder
def encode_person(obj):
    if isinstance(obj, Person):
        return {"name": obj.name, "age": obj.age}
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

# serialize the object
my_personJSON = json.dumps(my_person, default=encode_person, indent=4, sort_keys=True)
# default=encode is a custom encoder
print(my_personJSON) # {"name": "John", "age": 30}

# Method 2: Use a custom encoder
class person_encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
        return json.JSONEncoder.default(self, obj)

my_personJSON = json.dumps(my_person, cls=person_encoder, indent=4, sort_keys=True)
print(my_personJSON) # {"name": "John", "age": 30}
# Or
my_personJSON = person_encoder().encode(my_person) # This is the same as the above
print(my_personJSON) # {"name": "John", "age": 30}


################ Deserialization (JSON to Python) ################

# load json from file
with open("person.json", "r") as f:
    person = json.load(f) 
    # If we were to use loads, we would have to use the with statement/string
    # person = json.loads(f)
    # In this case its from a file, so we use load()

    print(person) # {"name": "John", "age": 30}
    print(type(person))# <class 'dict'>


# Deserialize from a custom object

def person_decoder(dict):
    if Person.__name__ in dict:
        return Person(**dict)
    return dict

decoded_user = json.loads(my_personJSON, object_hook=person_decoder)
print(decoded_user) # <__main__.Person object at 0x7f8b8b8b9c10>
print(type(decoded_user)) # <class '__main__.Person'>
print(decoded_user.name) # John