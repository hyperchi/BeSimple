# All indexing stocks will be added to this table
START TRANSACTION;

CREATE TABLE stocks
(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	ticker VARCHAR(20),
	exchange VARCHAR(20),
 market_segment VARCHAR(20)
);

COMMIT;

# data filling

START TRANSACTION;

INSERT INTO stocks (id, ticker, exchange, market_segment) VALUES(1, 'GOOGL', 'NASDAQ', 'IT');

COMMIT;