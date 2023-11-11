import csv

# We will use the csv module to work with a CSV file instead of pandas

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # next(csv_reader)                  # This will skip the first row

    # for line in csv_reader:
    #     print(line[1])

    # Saving data from one csv to another and changing the delimiter
    with open('new_names.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)


with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)

# Using dictionary reader method

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line['email'])

    # With DictWriter we need to mention the fieldnames and using this, we can leave out any column that we do not need
    with open('new_names.csv', 'w', newline='') as new_file:
        # fieldnames = ['first_name', 'last_name', 'email']
        fieldnames = ['first_name', 'last_name']       # Without email column

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']                           # Part of creating new csv without email
            csv_writer.writerow(line)