import csv

def get_csv_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    #skip headers of the csv file
    next(reader)
    #add rows from the reader to the list
    for row in reader:
        rows.append(row)
    return rows
