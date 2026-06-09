# Read a configuration JSON file and update its key-value pairs dynamically

import json

config_file = 'config.json'

try:
    with open(config_file, 'r') as file:
        # json.load() parses the text file into a standard Python dictionary
        config_data = json.load(file)
        print(f"Current Settings: {config_data}")
except FileNotFoundError:
    print(f"Error: Could not find '{config_file}'. Please create the file first.")
    exit()

key_to_update = input("Which setting would you like to change?: ").strip()
if key_to_update in config_data:
    current_value = config_data[key_to_update]
    new_value = input(f"Current value for {key_to_update} is '{current_value}', Enter new value: ").strip()
    if isinstance(current_value, int):
        config_data[key_to_update] = int(new_value)
    elif isinstance(current_value, bool):
        config_data[key_to_update] = bool(new_value)
    else:
        config_data[key_to_update] = new_value
    print(f"{key_to_update} is set to {new_value}")

else:
    print(f"{key_to_update} does not exist.")

with open(config_file, 'w') as file:
    # json.dump() takes a python dictionary and turns it back into the string inside the file.
    # indent = 4 makes the saved JSON file easy for humans to read.
    json.dump(config_data, file, indent=4)

print(f"Successfully saved changes to {config_file}!")