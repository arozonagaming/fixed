# Path to your JSON file
file_path = 'static/secret_key.txt'

# Open and read the JSON file
with open(file_path, 'r') as file:
    print(file.read())