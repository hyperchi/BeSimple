import csv
import MySQLdb
from databaseQuery import DatabaseQuery

"""
This file is used for populated stocks data
one off run
"""

def open_file(file_name):
    db = MySQLdb.connect(host="localhost",
                         user="winstonchi",
                         db="besimple")

    db_cursor = db.cursor()
    db.autocommit = True

    attributes = DatabaseQuery.DatabaseQuery.stocks_schema()
    with open(file_name) as infile:
        data = csv.reader(infile, delimiter=',')
        row_count = 0
        header = []
        for row in data:
            if (row_count == 0):
                header = row
            else:
                data_record = {'Exchange' : (file_name.split('.'))[0]}
                for index, field in enumerate(header):
                    if field in attributes:
                        data_record[field] = row[index]
                query = DatabaseQuery.DatabaseQuery.get_insert_stocks_query(data_record)
                try:
                    db_cursor.execute(query)
                    db.commit()
                except MySQLdb.Error, e:
                    print("something went wrong: {}".format(e))
                    pass
            row_count += 1
    db.close()

def main():
    """
    import three main exchange stocks to stocks table
    """
    file_names = ["nysdaq.csv", "nyse.csv", "amex.csv"]
    for file_name in file_names:
        open_file(file_name)

if __name__ == "__main__":
    main()