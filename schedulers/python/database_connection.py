#!/usr/bin/python
"""
This script will be used for database connections
1. get stock names for query
2. call api to get stock info
3. save data into database
"""
import MySQLdb
from databaseQuery import DatabaseQuery as dbQuery

def get_stock_names(query):
    try:
        db = MySQLdb.connect(host="localhost",
                             user="winstonchi",
                             db="besimple")

        db_cursor = db.cursor()
        db_cursor.execute(query)
        rows = db_cursor.fetchall()
        print rows
        db.close()
    except MySQLdb.Error, e:
        print("something went wrong: {}".format(e))

def main():
    query = dbQuery.DatabaseQuery.get_stocks()
    get_stock_names(query.query_string)

if __name__ == "__main__":
    main()