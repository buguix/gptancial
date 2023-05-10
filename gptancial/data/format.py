"""Format."""
from typing import Any
from typing import List
from typing import Dict

def transform_one_line_by_date(data: List[Dict[str, Any]], map_names: str, records: int, title: str) -> str:
    return "\n".join(
        [
            f"{title} for {data[i].get('date')}: " + " | ".join([f"{map_names.get(k)}={try_to_float(v)}" for k, v in data[i].items() if k in map_names])
            for i in range(records)
        ]
    )

def transform_multiple_lines_by_date(data: List[Dict[str, Any]], map_names: Dict[str, str], records: int, title: str) -> str:
    data_str = {
        f"{title} for {data[i].get('date')}:": "\n".join([f"{map_names.get(k)}={try_to_float(v)}" for k, v in data[i].items() if k in map_names])
        for i in range(records)
    }
    return "\n\n".join(["\n".join([k, v]) for k, v in data_str.items()])


def try_to_float(n: Any, decimals: int = 4) -> str:
    try:
        data = float(n)
        data = round(data, decimals)
        if data > 1_000:
            return f"{str(round(data / 1_000, 2))}K"
        return str(data)
    except:
        pass
    return n
