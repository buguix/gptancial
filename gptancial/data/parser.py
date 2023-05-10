"""Utils module."""
import json
import time
import urllib3

from gptancial.config import FMP_API_KEY

FMP_API_URL = "https://financialmodelingprep.com/api/"

def fmp_json_parser(path, api_version = "v4", retry: int = 0):
    http_manager = urllib3.PoolManager()
    base_url = f"{FMP_API_URL}{api_version}{path}"
    api_part = f"apikey={FMP_API_KEY}"
    full_url = f"{base_url}{'?' if '?' not in base_url else '&'}{api_part}"
    response = http_manager.request("GET", full_url, timeout=20)
    data = json.loads(response.data.decode("utf-8"))
    err = data.get("Error Message") if isinstance(data, dict) else None
    if err:
        if err.startswith("Too Many Requests"):
            if retry < 3:
                time.sleep(25)
                return fmp_json_parser(path, retry + 1, api_version=api_version)
        raise Exception(f"Exception on FMP API: {err}")

    return data
