from ConnectDB import ConnectDB

class BusinessLogic(object):
    def __init__(self):
        self.db = ConnectDB.ConnectDB()

    def get_stock_info_request(self, ticker="*"):
        return self.db.get_stock_info(ticker)

    def get_sector_company_list_request(self, sector="*"):
        tuple_data = self.db.get_sector_company_list(sector)
        # hardcode position here bad design but let it work first
        sector_symbol = {}
        for row in tuple_data:
            if row[0] not in sector_symbol:
                sector_symbol[row[0]] = [row[1]]
            else:
                sector_symbol[row[0]].append(row[1])
        return sector_symbol
