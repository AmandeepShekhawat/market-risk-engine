CREATE TABLE price (
    date DATE not null,
    symbol TEXT not null,
    
    open NUMERIC (12,4),
    high NUMERIC (12,4),
    low NUMERIC (12,4),
    close NUMERIC (12,4),

    volume BIGINT,

    PRIMARY KEY (symbol,date)
);