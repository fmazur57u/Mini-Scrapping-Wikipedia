import re
from fectcher import télécharger_contenu
from collections import Counter


def extraction_date(text):
    dates = re.findall(r"\b((?:1|2)\d{3})\b", text)
    return dates


def extraction_ref(text):
    base_url = "https://fr.wikipedia.org"
    refs = re.findall(r'href="([^"]+)"', text)
    relatif_ref = []
    for ref in refs:
        if ref.startswith("http"):
            relatif_ref.append(ref)

        if ref.startswith("/"):
            relatif_ref.append(base_url + ref)
    return Counter(relatif_ref).keys()
