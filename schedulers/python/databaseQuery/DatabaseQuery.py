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
    def get_stocks():
        """
        get stocks from stocks table
        @ param void
        @ return object QueryData
        """
        attributes = {"id" : "id",
                      "ticker" : "ticker",
                      "exchange" : "exchange",
                      "market_segment": "marketSegment"}

        query = "SELECT id       as       {id},\
		                ticker   as   {ticker},\
		                exchange as {exchange},\
		                market_segment as {market_segment}\
		                FROM stocks".format(id=attributes["id"],
                                            ticker=attributes["ticker"],
                                            exchange=attributes["exchange"],
                                            market_segment=attributes['market_segment'])
        query_data = QueryData(query, attributes)
        return query_data