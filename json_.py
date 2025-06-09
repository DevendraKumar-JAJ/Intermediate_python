# Import the json module
import json
# Define a dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Convert the dictionary to a JSON string
json_data = json.dumps(data,indent=4,separators=(':','='),sort_keys=True)

# Print the JSON string
print(json_data)

with open('pers.json','w')as file:
    json.dump(json_data,file,separators=(':','='),indent=4)


data = {
    "name": "John Doe",
    "age": 50,
    "city": "New York"
}


json_data = json.dumps(data,indent=4,separators=(':','='),sort_keys=True)
with open('pers.txt','w')as file:
    json.dump(json_data,file,separators=(':','='),indent=4)