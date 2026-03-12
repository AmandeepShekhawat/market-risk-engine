from database.connection import get_connection

def load_prices(df):

    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO price (symbol, date, open, high, low, close, volume)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (symbol, date) DO NOTHING;
    """

    for row in df.itertuples(index=False):
        cursor.execute(query,(
            row.symbol,
            row.date,
            row.open,
            row.high,
            row.low,
            row.close,
            row.volume
        ))

    conn.commit()
    cursor.close()
    conn.close()

