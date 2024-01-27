if __name__ == '__main__':
    # User input to get the number of data entries
    n = int(input().strip())

    contacts = {}  # Initialize an empty dictionary to store contact information
    data = []  # Initialize an empty list to store data entries

    # Input loop to gather data entries
    while n > 0:
        data.append(input().strip())  # Collect each data entry
        n -= 1

    # Loop to populate the dictionary with contact information
    for d in data:
        splitdata = d.split()
        contacts[splitdata[0]] = splitdata[1]  # Use the name as the key and the number as the value

    # Query loop to access values using query names
    while True:
        try:
            q = input().strip()

            # Exit loop if an empty string is entered
            if q == '':
                break

            # Check if the query name exists in the dictionary
            if contacts.get(q):
                print(f'{q}={contacts.get(q)}')
            else:
                print('Not found')
        except EOFError:
            break
