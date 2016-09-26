from flask import Flask, render_template
#from connectDB import ConnectDB
from BusinessLogic import BusinessLogic
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

#db_connection = ConnectDB.ConnectDB(app)

# get_stocks_query = ConnectDB.DBSchema.get_stocks_query()
# data = db_connection.execute_query(get_stocks_query)
#
# info = data
# for row in data:
#     for elem in row:
#         print elem
@app.route('/')



def main():

 #   get_stocks_query = ConnectDB.DBSchema.get_stocks_query()
  #  data = db_connection.execute_query(get_stocks_query)

    # just a test to test if data is actually generated
   # for row in data:
        #app.logger.warning(row)
    #    for elem in row:
     #       print elem
    business_logic = BusinessLogic.BusinessLogic()
    stock_info = business_logic.get_stock_info_request("AAPL")
    test = "test text"
    data = stock_info
    return render_template('index.html', info=data, test=test)

if __name__ == "__main__":
    handler = RotatingFileHandler('../logs/main.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    # run app
    app.run(debug=True)