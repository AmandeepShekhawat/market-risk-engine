from data_pipeline.fetch_prices import fetch_prices, transform_prices
from data_pipeline.load_prices import load_prices

def run():

    print("Fetching prices")

    raw_data = fetch_prices()

    print(raw_data.columns)

    print("Transforming data")

    transformed_data = transform_prices(raw_data)

    print(transformed_data.head())
    print(transformed_data.dtypes)

    print("Loading data")

    load_prices(transformed_data)

    print("Pipeline Completed")

if __name__ == "__main__":
    run()