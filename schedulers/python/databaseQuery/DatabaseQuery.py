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
                  "Exchange": "Exchange",
                  "IPOyear" : "IPOyear",
                  "Sector"  : "Sector",
                  "Industry": "Industry"
                }

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
		                Exchange as {Exchange},\
		                IPOyear  as {IPOyear},\
		                Sector   as {Sector},\
                        Industry as {Industry}\
		                FROM stocks".format(id=stocks_attributes['id'],
                                            ticker=stocks_attributes["Symbol"],
                                            exchange=stocks_attributes["Exchange"],
                                            IPOyear=stocks_attributes['IPOyear'],
                                            Sector=stocks_attributes['Sector'],
                                            Industry=stocks_attributes['Industry'])
        query_data = QueryData(query, stocks_attributes)
        return query_data

    @staticmethod
    def insert_stocks(data):
        """
        call this function to insert data into stocks
        """
        """
        :return:
        """
        pass