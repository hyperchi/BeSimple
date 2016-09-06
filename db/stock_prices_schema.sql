# All stock price info will go to this table

START TRANSACTION;

CREATE TABLE stock_prices
(
    rowid VARCHAR(30),
    ticker VARCHAR(20),
    UTCtime DATETIME,
    market_price DOUBLE(8,4),
    volume INT
);

COMMIT;