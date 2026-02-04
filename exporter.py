import json
from typing import Dict, List, Union
from logging import Logger


def save_json(
    data: Dict[str, List[Union[int, List[Union[str, int]], str]]], log: Logger
) -> None:
    with open(file="outpout.json", mode="w", encoding="utf-8") as f:
        log.debug(f"Chemin du fichier de sortie: {f.name}.")
        log.debug(
            f"Nombre d'année: {len(data["sorted_years"])} et Nombre d'url: {len(data["urls"])}"
        )
        json.dump(data, f, indent=2, sort_keys=True, ensure_ascii=False)
        log.info("Fichier JSON écrit avec succès")
