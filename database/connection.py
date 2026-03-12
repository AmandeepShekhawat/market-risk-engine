import psycopg2

def get_connection():
    conn = psycopg2.connect(host="localhost",
                            database="market_risk_engine",
                            user="postgres",
                            password="Jry@7267",
                            port="5432"
                            )
    
    return conn

