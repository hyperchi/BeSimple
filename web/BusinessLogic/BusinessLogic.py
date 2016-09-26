from ConnectDB import ConnectDB

class BusinessLogic(object):
    def __init__(self):
        self.db = ConnectDB.ConnectDB()

    def get_stock_info_request(self, ticker):
        return self.db.get_stock_info(ticker)
