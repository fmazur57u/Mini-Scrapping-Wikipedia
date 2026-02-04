from collections import Counter
from logging import Logger
from typing import List


def filter_date(dates_str: List[str], log: Logger) -> List[int]:
    dates = [int(date) for date in dates_str]
    log.debug(f"Nombre de dates avant filtre: {len(dates)}.")
    filter_date = list(filter(lambda date: 1000 <= date <= 2100, dates))
    if not filter_date:
        log.warning("Il ne reste aucune année aprés le filtre.")
    log.debug(f"Nombre de dates aprés filtre: {len(filter_date)}.")
    filter_date.sort()
    log.info(f"Nombre d'année finale: {len(filter_date)}")
    log.info(f"Année min: {min(filter_date)}, Année max: {max(filter_date)}")
    return filter_date


def calcul_occurence_par_année(filter_date: List[int], log: Logger) -> Counter:
    occurences = Counter(filter_date)
    if not occurences:
        log.warning("Dictionnaire d’occurrences vide.")
    return occurences
