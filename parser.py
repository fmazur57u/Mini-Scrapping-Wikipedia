import re


def extraction_date(text):
    dates = re.findall(r"\b((?:1|2)\d{3})\b", text)
    return dates
