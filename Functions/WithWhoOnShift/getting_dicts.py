import re


def get_persons_dict(row_idx, date_range, date):
    dates_dict = {}

    match = date_range.isin([date]).any(axis=0)
    column = date_range.columns[match]
    i = row_idx[0]
    j = column[0]

    hours = date_range.loc[i, j]
    time_form = re.compile(r'^\d{2}-\d{2}$')
    if isinstance(hours, str):
        if time_form.match(hours):
            dates_dict[date.date()] = hours
        else:
            dates_dict[date.date()] = "Wolne"
    else:
        dates_dict[date.date()] = "Wolne"

    return dates_dict

def get_day_dict(names, date_range, date):
    peoples_dicts = {}
    for n in names:
        match = date_range.astype(str).isin([n]).any(axis=1)
        row = date_range.index[match]

        persons_dict = get_persons_dict(row, date_range, date)
        peoples_dicts[n] = persons_dict

    sorted_dict = dict(
        sorted(peoples_dicts.items(), key=lambda x: list(x[1].values())[0])
    )
    return sorted_dict
