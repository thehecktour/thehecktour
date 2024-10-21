from fastapi import FastAPI
from modules.http.data_fetcher import DataFetcher
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

csv_url = os.getenv("CSV_URL")
json_url = os.getenv("JSON_URL")

data_fetcher = DataFetcher(csv_url, json_url)
data_fetcher.fetch_csv()
data_fetcher.fetch_json()

@app.get("/api/v1/users/csv")
def get_csv_data():
    if data_fetcher.data_csv is not None:
        return data_fetcher.data_csv.to_dict(orient="records")
    else:
        return {"error": "CSV data not found"}, 404

@app.get("/api/v1/users/json")
def get_json_data():
    if data_fetcher.data_json is not None:
        return data_fetcher.data_json
    else:
        return {"error": "JSON data not found"}, 404
