import MySQLdb

class QueryData(object):
    """
    This object will be used in Database Query as query objects
    """
    def __init__(self, query_string, query_attributes):
        self.query_string = query_string
        self.query_attributes = query_attributes
    def query_string(self):
        return self.query_string
    def query_attributes(self):
        return self.query_attributes

class DatabaseQuery(object):
    """
    this is a class containing off database related queries
    """
    @staticmethod
    def stocks_schema():
        return {
                  "id"      : "id",
                  "Symbol"  : "Symbol",
                  "Name"    : "Name",
                  "Exchange": "Exchange",
                  "IPOyear" : "IPOyear",
                  "Sector"  : "Sector",
                  "Industry": "Industry"
                }
    @staticmethod
    def stocks_fields():
        return ["id", "Symbol", "Name", "Exchange", "IPOyear", "Sector", "Industry"]

    @staticmethod
    def get_stocks():
        """
        get stocks from stocks table
        @ param void
        @ return object QueryData
        """

        stocks_attributes = DatabaseQuery.stocks_schema()
        query = "SELECT id       as       {id},\
		                Symbol   as   {Symbol},\
                        Name     as   {Name},\
		                Exchange as {Exchange},\
		                IPOyear  as {IPOyear},\
		                Sector   as {Sector},\
                        Industry as {Industry}\
		                FROM stocks".format(id=stocks_attributes['id'],
                                            Symbol=stocks_attributes["Symbol"],
                                            Name=stocks_attributes["Name"],
                                            Exchange=stocks_attributes["Exchange"],
                                            IPOyear=stocks_attributes['IPOyear'],
                                            Sector=stocks_attributes['Sector'],
                                            Industry=stocks_attributes['Industry'])
        query_data = QueryData(query, stocks_attributes)
        return query_data

class ConnectDB(object):
    def __init__(self):
        self.host = "localhost"
        self.username = "winstonchi"
        self.db_name = "besimple"
        self.stocks_table_attributes = DatabaseQuery.stocks_fields()

    # getter function to retrieve data from db
    def basic_getter(self, query):
        try:
            db = MySQLdb.connect(host=self.host,
                                 user=self.username,
                                 db=self.db_name)

            db_cursor = db.cursor()
            db_cursor.execute(query)
            rows = db_cursor.fetchall()
            db.close()
            return rows
        except MySQLdb.Error, e:
            print("something went wrong: {}".format(e))

   # setter function to retrieve data from db
    def basic_setter(self, query):
        try:
            db = MySQLdb.connect(host=self.host,
                                 user=self.username,
                                 db=self.db_name)
            db.autocommit = True
            db_cursor = db.cursor()
            db_cursor.execute(query)
            db.commit()
            db.close()
        except MySQLdb.Error, e:
            print("something went wrong: {}".format(e))

    def get_stock_info(self, ticker="*"):
        query = "SELECT * FROM stocks " \
                "    WHERE Symbol={open_quote}{Symbol}{close_quote}"\
                     .format(open_quote="'", Symbol=ticker, close_quote="'")
        #print self.stocks_table_attributes
        #print self.basic_getter(query)
        return zip(self.stocks_table_attributes, self.basic_getter(query)[0])

    def get_stock_recent_price(self):
        pass

    def get_sector_company_list(self):
        pass
