from logger_config import *
from exporter import *
from analyzer import *
from fectcher import *
from parser import *


def main(url):
    log = logger()
    text = télécharger_contenu(url, log)
    dates_str = extraction_date(text, log)
    sorted_years = filter_date(dates_str, log)
    top_frequent_years_dict = calcul_occurence_par_année(sorted_years, log)
    sorted_items = sorted(
        top_frequent_years_dict.items(), key=lambda item: item[1], reverse=True
    )
    top_frequent_years = [[f"{year}", occurences] for year, occurences in sorted_items]
    urls = extraction_ref(text, log)
    final_json = {
        "sorted_years": sorted_years,
        "top_frequent_years": top_frequent_years,
        "urls": urls,
    }
    save_json(final_json, log)


main("https://fr.wikipedia.org/wiki/Intelligence_artificielle")
