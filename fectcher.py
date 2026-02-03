import requests
from typing import Dict, List


def télécharger_contenu(url: str):
    headers = {"User-Agent": "Cours-DataScience-Client", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.text
