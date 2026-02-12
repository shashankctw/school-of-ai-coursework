def write_items_to_file(items, filename):
    with open(filename, 'w') as file:
        for item in items:
            file.write(f"{item}\n")
            
def read_items_from_file(filename):
    try:
        with open(filename, 'r') as file:
            item = file.readline()
            print(f"Items in the file:")
            for item in file:
                print(item.strip())
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        
items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
write_items_to_file(items, 'sample.txt')
read_items_from_file('sample.txt')