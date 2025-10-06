import datetime
from Functions.WithWhoOnShift.getting_structures import find_date_range, find_existing_days, find_names
from Functions.WithWhoOnShift.getting_dicts import get_day_dict


def print_output(day, peoples_dict):
    ###
    print(f"{day.day}/{day.month}")
    print("=====================")
    for key in peoples_dict:
        print(key)
        print(peoples_dict[key][day])
        print("--------")
    print("=====================")
    ###

def get_month_dict(mattering_dates, schedule, name, test=False):
    month_dict = {}
    dates = find_existing_days(schedule)
    date = min(dates)
    date_range = find_date_range(date, schedule)
    days_in_range = find_existing_days(date_range)

    names = find_names(date_range, name)
    for d in mattering_dates:
        d = datetime.datetime.combine(d, datetime.time(0, 0, 0) )
        if d not in days_in_range:
            date_range = find_date_range(d, schedule)
            days_in_range = find_existing_days(date_range)

        peoples_dict = get_day_dict(names, date_range, d)
        month_dict[d.date()] = peoples_dict
        if test:
            print_output(d, peoples_dict)

    return month_dict
