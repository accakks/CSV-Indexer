import csv
import sys


input_csv = sys.argv[1] if len(sys.argv) > 1 else 'input1.csv'
matching_type = sys.argv[2].casefold() if len(sys.argv) > 2 else 'same_contact'

# Check args


def check_arg1(input_csv):
    if input_csv.endswith('.csv'):
        pass
    else:
        raise TypeError('File not csv type')


def check_arg2(matching_type):
    matching_types = ('same_email', 'same_phone_number', 'same_contact')
    if matching_type not in matching_types:
        raise ValueError(
            'Invalid matching type, Enter from (same_email, same_phone_number, same_contact)')


def check_fieldnames(fieldnames):
    if 'Email' not in fieldnames or 'Phone' not in fieldnames:
        raise AttributeError(
            'Missing Fields! Email and Phone fields must be present in input csv')

# if matching type = same_email


def same_email(read_input, Id):
    Emails = []
    counter = 0
    Id_val = 1

    for row in read_input:
        if row['Email'] == '':
            Id.append(Id_val)
            Id_val += 1
            counter += 1
        else:
            if row['Email'] not in Emails:
                Id.append(Id_val)
                Emails.append(row['Email'])
                Id_val += 1
                counter += 1
            else:
                index = Emails.index(row['Email'])
                Id.append(Id[index])
                counter += 1

    return Id

# if matching_type = same_phone_number


def same_phone_number(read_input, Id):
    Phone_nos = []
    counter = 0
    Id_val = 1

    for row in read_input:
        if row['Phone'] == '':
            Id.append(Id_val)
            Id_val += 1
            counter += 1
        else:
            if row['Phone'] not in Phone_nos:
                Id.append(Id_val)
                Phone_nos.append(row['Phone'])
                Id_val += 1
                counter += 1
            else:
                index = Phone_nos.index(row['Phone'])
                Id.append(Id[index])
                counter += 1

    return Id

# if matching_type = same_contact


def same_contact(input_file, read_input, Id):
    Id_phone = same_phone_number(read_input, Id)
    input_file.seek(0)
    next(read_input)
    Id_email = same_email(read_input, Id)

    Id_contact = []
    count = 0
    for i, j in zip(Id_phone, Id_email[int(len(Id_email)/2):]):
        if i == 1 and j == 1:
            Id_contact.append(i)
        else:
            if min(i, j) == Id_contact[min(i, j)-1] or min(i, j) - Id_contact[count - 1] == 1 or min(i, j) in Id_contact:
                Id_contact.append(min(i, j))
            else:
                Id_contact.append(count - 1)
        count += 1

    return Id_contact

# Record linkage function


def record_linkage(input_csv, matching_type):
    check_arg1(input_csv)
    check_arg2(matching_type)

    with open(input_csv, 'r') as input_file, open('output1.csv', 'w+') as output_file:
        read_input = csv.DictReader(input_file)
        check_fieldnames(read_input.fieldnames)  # check missing fieldnames
        read_input.fieldnames = read_input.fieldnames + ['Id']
        Id = []

        if matching_type == 'same_email':
            Id = same_email(read_input, Id)

        if matching_type == 'same_phone_number':
            Id = same_phone_number(read_input, Id)

        if matching_type == 'same_contact':
            Id = same_contact(input_file, read_input, Id)

       # Write into output.csv
        output_fieldnames = read_input.fieldnames
        write_output = csv.DictWriter(
            output_file, fieldnames=output_fieldnames)

        write_output.writeheader()

        row_no = 0
        input_file.seek(0)
        next(read_input)  # fixed read_input multiple looping

        for row in read_input:
            row['Id'] = Id[row_no]
            row_no += 1
            write_output.writerow(row)


record_linkage(input_csv, matching_type)
