from logging import Logger
import requests


def télécharger_contenu(url: str, log: Logger):
    headers = {"User-Agent": "Cours-DataScience-Client", "Accept": "application/json"}
    response = requests.get(url, headers=headers)
    log.debug(f"GET url={response.url} headers={response.headers}")
    log.info(f"Status de la requête get={response.status_code}")
    log.info(f"La taille du contenue est={len(response.text)}")
    if response.status_code == 429:
        log.warning("Le code de status est 429. Veuillez recommencer.")
    return response.text
