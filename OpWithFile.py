myFile = input("Enter file name: ")
print("Available operation: ")
fileOpp = (['Add', 'Remove', 'Change', "Sum"])
print(fileOpp)
operation = input("Input operation: ")

with open(myFile, "r") as f:
    f.read()
    f.close()
    if operation == 'Add':
        with open(myFile, 'a') as f:
            newItem = input("New Item: ")
            f.write("\n" + newItem)
            f.close
    elif operation == 'Change':
        with open(myFile, 'r') as f:
            old_data = f.read()
            itemOld = input("Old item: ")
            itemNew = input("New item: ")
            new_data = old_data.replace(itemOld, itemNew)
            with open(myFile, 'w') as f:
                f.write(new_data)
                f.close()
    elif operation == 'Remove': 
        with open(myFile, 'w') as f:
            f.write('')
            f.close()
    elif operation == 'Sum':
        f = open(myFile, 'r')
        total_count = sum(int(x) for x in f if x.strip().isdigit()) 
        print(total_count)

newFile = open(myFile, 'r')
result = newFile.read()
newFile.close()
print(result)

