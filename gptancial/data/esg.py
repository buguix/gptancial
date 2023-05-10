"""Fundamentals Data."""
from typing import Any
from typing import List
from typing import Dict
from typing import Optional

from .parser import fmp_json_parser
from .format import transform_one_line_by_date

def get_esg_score(symbol: str, records: int = 10, details: bool = False) -> str:
    data = fmp_json_parser(path=f"/esg-environmental-social-governance-data?symbol={symbol}", api_version="v4")
    if details:
        map_names = {
            "environmentalScore": "Environmental",
            "socialScore": "Social",
            "governanceScore": "Governance",
            "ESGScore": "ESG",
        }
    else:
        map_names = {"ESGScore": "Score"}

    return transform_one_line_by_date(data=data, map_names=map_names, records=records, title="ESG Score")

