from collections import Counter


def filter_date(dates_str):
    dates = [int(date) for date in dates_str]
    filter_date = list(filter(lambda date: 1000 <= date <= 2100, dates))
    filter_date.sort()
    return filter_date


def calcul_occurence_par_année(filter_date):
    return Counter(filter_date)
