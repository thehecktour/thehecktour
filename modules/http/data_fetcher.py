import requests
import pandas as pd
from io import StringIO

class DataFetcher:
    def __init__(self, csv_url, json_url):
        self.csv_url = csv_url
        self.json_url = json_url
        self.data_csv = None
        self.data_json = None

    def fetch_csv(self):
        response = requests.get(self.csv_url)
        response.raise_for_status()

        csv_data = StringIO(response.text)
        self.data_csv = pd.read_csv(csv_data)

    def fetch_json(self):
        response = requests.get(self.json_url)
        response.raise_for_status()

        self.data_json = response.json()
