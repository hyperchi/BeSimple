from __future__ import print_function

from flask import Flask, render_template, request
from BusinessLogic import BusinessLogic
import logging
from logging.handlers import RotatingFileHandler
import sys

app = Flask(__name__)
business_logic = BusinessLogic.BusinessLogic()



@app.route('/')
def main(info=""):
    return render_template('index.html', info=info)

@app.route('/', methods=['POST'])
def main_post():
    text = request.form['text']
    stock_info = business_logic.get_stock_info_request(text)
    print("hello", file=sys.stderr)
    company_list = business_logic.get_sector_company_list_request()
    #for row in company_list:
    print(company_list, file=sys.stderr)

    return render_template("index.html", info=stock_info)

if __name__ == "__main__":
    handler = RotatingFileHandler('../logs/main.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True)