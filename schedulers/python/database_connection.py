#!/usr/bin/python
"""
This script will be used for database connections
1. get stock names for query
2. call api to get stock info
3. save data into database
"""
import MySQLdb
import quandl
from databaseQuery import DatabaseQuery as dbQuery

def get_stock_names(query):
    try:
        db = MySQLdb.connect(host="localhost",
                             user="winstonchi",
                             db="besimple")

        db_cursor = db.cursor()
        db_cursor.execute(query)
        rows = db_cursor.fetchall()
        db.close()
        return rows
    except MySQLdb.Error, e:
        print("something went wrong: {}".format(e))

def read_stock_info_from_quandl(query):
    data = get_stock_names(query.query_string)
    print data

def main():
    query = dbQuery.DatabaseQuery.get_stocks()
    read_stock_info_from_quandl(query)

if __name__ == "__main__":
    main()