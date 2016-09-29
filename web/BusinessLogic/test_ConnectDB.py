from ConnectDB import ConnectDB

def main():
    db = ConnectDB.ConnectDB()
    # test get all stock
    all_stock = db.get_stock_info('AAPL')
    for row in all_stock:
        print row
    all_sector_list = db.get_sector_company_list()

    for row in all_sector_list:
        print row


if __name__ == "__main__":
    main()