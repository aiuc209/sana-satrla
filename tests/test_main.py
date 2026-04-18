import pytest
from datetime import datetime

def convert_date(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return date.strftime("%d-%B, %Y")

@pytest.mark.parametrize("date_str, expected", [
    ("2025-04-18", "18-April, 2025"),
    ("2022-01-01", "01-January, 2022"),
    ("1999-12-31", "31-December, 1999")
])
def test_convert_date(date_str, expected):
    assert convert_date(date_str) == expected
