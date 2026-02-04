import re
from collections import Counter
from logging import Logger
from typing import List, Dict


def extraction_date(text: str, log: Logger) -> List[str]:
    dates = re.findall(r"\b((?:1|2)\d{3})\b", text)
    log.debug(f"Nombre de candidats années avant filtre est {len(dates)}")
    if len(dates) == 0:
        log.warning("Aucun nombre à 4 chiffres trouvé.")
    return dates


def extraction_ref(text: str, log: Logger) -> List[str]:
    base_url = "https://fr.wikipedia.org"
    refs = re.findall(r'href="([^"]+)"', text)
    relatif_ref = []
    for ref in refs:
        if ref.startswith("http"):
            relatif_ref.append(ref)

        if ref.startswith("/"):
            relatif_ref.append(base_url + ref)
    log.debug(f"{len(refs)} référence ont été trouvé.")
    log.info(f"Il y a {len(Counter(relatif_ref).keys())} url uniques.")
    if not refs:
        log.warning("Aucune référence n'a été trouveé.")
    return list(Counter(relatif_ref).keys())
