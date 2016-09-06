# All indexing stocks will be added to this table
START TRANSACTION;

CREATE TABLE stocks
(
	id VARCHAR(20) NOT NULL PRIMARY KEY,
	ticker VARCHAR(20),
	exchange VARCHAR(20)
);

COMMIT;

# data filling

START TRANSACTION;

INSERT INTO stocks (id, ticker, exchange) VALUES(1, 'GOOGL', 'NASDAQ');

COMMIT;