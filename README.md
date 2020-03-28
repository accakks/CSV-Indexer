# CSV Indexing

The goal of this project is to identify rows in a CSV file that may represent the same person based on a provided Matching Type and index them accordingly.

## Usage

```
$ python solution.py input_file matching_type
```
* Input_file should be csv. [default input1.csv]

* Matching types can be:
   1. one that matches records with the same email address (same_email)
   2. one that matches records with the same phone number (same_phone_number)
   3. one that matches records with the same email address OR the same phone number (same_contact) [default]

You will receive your output in output1.csv

(Find my outputs of each case in "My Output" folder)

## Running Tests

* ```$ python test_solution_unit.py```
* ```$ python test_solution_integration.py```

