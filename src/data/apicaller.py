import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import certifi
from configurations import FMPAPI
import pandas as pd


class APICaller:
    def __init__(self, api_calls=None, headers=None):
        self.api_calls = api_calls
        self.headers = headers if headers else {}
        self.api_key = FMPAPI

    def get_single_data(self, api_type, params=None):
        if api_type not in self.api_calls:
            raise KeyError("Invalid API key")

        base_url = self.api_calls[api_type]

        if params:
            query_string = urlencode(params)
            url = f'{base_url}{query_string}{self.api_key}'
        else:
            url = f'{base_url}{self.api_key}'

        request = Request(url, headers=self.headers)
        with urlopen(request) as response:
            data = response.read()
            return json.loads(data)
    
    def get_json_data(self, api):
        return urlopen(api, cafile=certifi.where())
        
    def get_csv_data(self, api):
        return  pd.read_csv(api,sep=',')
    
    def set_api_calls(self,newcalls):
        self.api_calls = newcalls

    def format_url(self,format,url=''):
        return url.format(format)