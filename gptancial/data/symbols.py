"""Symbols Data."""
from typing import Any
from typing import Dict
from typing import List

from .parser import fmp_json_parser


def get_symbols() -> List[Dict[str, Any]]:
    sp500 = fmp_json_parser(path="/sp500_constituent", api_version="v3")
    return [{"value": entry.get("symbol"), "label": entry.get("name") + " - " + entry.get("symbol")} for entry in sp500]
