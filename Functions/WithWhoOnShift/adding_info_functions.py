
import datetime

# def format_date_format(date):
def find_date_range(date, schedule):

    mask = schedule.isin([date]).any(axis=1)

    date_row_idx = schedule.index[mask].tolist()[0]
    all_dates_row_idx = sorted(
        idx for idx, row in schedule.iterrows()
        if any(isinstance(val, datetime.datetime) for val in row)
    )

    h = all_dates_row_idx.index(date_row_idx)
    try:
        next_date_row_idx = all_dates_row_idx[h + 1] - 1
        dates_between = schedule.loc[date_row_idx:next_date_row_idx].dropna(how="all").dropna(axis=1, how="all")

    except IndexError:
        dates_between = schedule.loc[date_row_idx:].dropna(how="all").dropna(axis=1, how="all")

    return dates_between

def find_existing_days(schedule):
    dates = [schedule.loc[idx, col] for idx, row in schedule.iterrows()\
                    for col in schedule.columns\
                    if isinstance(schedule.loc[idx, col], datetime.datetime)]
    return dates

