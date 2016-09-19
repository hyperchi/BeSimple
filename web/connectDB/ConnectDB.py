from flaskext.mysql import MySQL
import json
# a kinda dup from db should figure out how to solve this in the future
class DBSchema(object):
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
    def get_stocks_query():
        """
        get stocks from stocks table
        @ param void
        @ return string Query
        """

        stocks_attributes = DBSchema.stocks_schema()
        return  "SELECT id       as       {id},\
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

class ConnectDB:
    def __init__(self, app):
        self.username = "winstonchi"
        self.db_name = "besimple"
        self.localhost = "localhost"

        self.mysql = MySQL()

        # MySQL configurations
        app.config['MYSQL_DATABASE_USER'] = self.username
        app.config['MYSQL_DATABASE_DB'] = self.db_name
        app.config['MYSQL_DATABASE_HOST'] = self.localhost
        self.mysql.init_app(app)

    def username(self):
        return self.username

    def db_name(self):
        return self.db_name

    def localhost(self):
        return self.localhost

    def mysql(self):
        return self.mysql

    def setup_connection(self):
        return self.mysql.connect()

    # this is a general one for getting data
    def execute_query(self, query):
        connection = self.setup_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        print cursor.co
        return cursor.fetchall()