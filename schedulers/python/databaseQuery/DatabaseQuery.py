class DatabaseQuery(object):
    """
    this is a class containing off database related queries
    """
    @staticmethod
    def get_stocks():
        """
        get stocks from stocks table
        """
        query = "SELECT id       as       id,\
		                ticker   as   ticker,\
		                exchange as exchange\
		                FROM stocks"
        return query