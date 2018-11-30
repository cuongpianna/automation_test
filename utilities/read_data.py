import csv


def get_csv_data(file_name):
    """
       read test data from csv and return as list

       @type file_name: string
       @param file_name: some csv path string
       @return list
    """
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows
