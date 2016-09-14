# All indexing stocks will be added to this table
START TRANSACTION;

CREATE TABLE stocks
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Symbol                         VARCHAR(20),
    Name                           VARCHAR(120),
    Exchange                       VARCHAR(20),
    IPOyear                        VARCHAR(20),
    Sector                         VARCHAR(50),
    Industry                       VARCHAR(120)
);

COMMIT;